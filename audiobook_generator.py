"""
Chatterbox TTS Audiobook Generator
Generates audiobooks from text files with voice cloning support.
"""

import os
import re
import argparse
from pathlib import Path
from typing import List, Optional
import torchaudio as ta
from tqdm import tqdm
import torch

try:
    from chatterbox.tts import ChatterboxTTS
except ImportError:
    print("ERROR: chatterbox-tts not installed. Run: pip install chatterbox-tts")
    exit(1)


class AudiobookGenerator:
    def __init__(self, device: str = "cuda", voice_reference: Optional[str] = None):
        """
        Initialize the audiobook generator.

        Args:
            device: Device to run on ('cuda' or 'cpu')
            voice_reference: Path to reference audio for voice cloning
        """
        print(f"Loading Chatterbox TTS model on {device}...")
        self.model = ChatterboxTTS.from_pretrained(device=device)
        self.voice_reference = voice_reference
        self.sample_rate = self.model.sr
        print(f"Model loaded successfully! Sample rate: {self.sample_rate} Hz")

    def split_text_into_chunks(self, text: str, max_chars: int = 500) -> List[str]:
        """
        Split text into manageable chunks at sentence boundaries.

        Args:
            text: Input text to split
            max_chars: Maximum characters per chunk

        Returns:
            List of text chunks
        """
        # Split by sentences (periods, exclamation marks, question marks)
        sentences = re.split(r'(?<=[.!?])\s+', text)

        chunks = []
        current_chunk = ""

        for sentence in sentences:
            # If adding this sentence exceeds max_chars, save current chunk
            if len(current_chunk) + len(sentence) > max_chars and current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = sentence
            else:
                current_chunk += " " + sentence if current_chunk else sentence

        # Add the last chunk
        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def generate_audio_chunk(self, text: str) -> torch.Tensor:
        """
        Generate audio for a single text chunk.

        Args:
            text: Text to convert to speech

        Returns:
            Audio tensor
        """
        if self.voice_reference:
            return self.model.generate(text, audio_prompt_path=self.voice_reference)
        else:
            return self.model.generate(text)

    def merge_audio_chunks(self, audio_chunks: List[torch.Tensor],
                          silence_duration: float = 0.5) -> torch.Tensor:
        """
        Merge multiple audio chunks with silence between them.

        Args:
            audio_chunks: List of audio tensors
            silence_duration: Duration of silence between chunks (seconds)

        Returns:
            Merged audio tensor
        """
        import torch

        # Create silence tensor
        silence_samples = int(self.sample_rate * silence_duration)
        silence = torch.zeros(1, silence_samples)

        # Merge chunks with silence
        merged = []
        for i, chunk in enumerate(audio_chunks):
            merged.append(chunk)
            # Add silence between chunks (but not after the last one)
            if i < len(audio_chunks) - 1:
                merged.append(silence)

        return torch.cat(merged, dim=1)

    def generate_audiobook(self, input_file: str, output_file: str,
                          chunk_size: int = 500,
                          silence_duration: float = 0.5,
                          save_chunks: bool = False) -> None:
        """
        Generate an audiobook from a text file.

        Args:
            input_file: Path to input text file
            output_file: Path to output audio file
            chunk_size: Maximum characters per chunk
            silence_duration: Silence between chunks (seconds)
            save_chunks: If True, save individual chunk audio files
        """
        # Read input text
        print(f"\nReading text from: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        print(f"Total characters: {len(text):,}")
        print(f"Total words: {len(text.split()):,}")

        # Split into chunks
        print(f"\nSplitting text into chunks (max {chunk_size} chars)...")
        chunks = self.split_text_into_chunks(text, max_chars=chunk_size)
        print(f"Created {len(chunks)} chunks")

        # Generate audio for each chunk
        print(f"\nGenerating audio chunks...")
        audio_chunks = []
        chunk_dir = None

        if save_chunks:
            chunk_dir = Path(output_file).parent / f"{Path(output_file).stem}_chunks"
            chunk_dir.mkdir(exist_ok=True)
            print(f"Saving chunks to: {chunk_dir}")

        for i, chunk in enumerate(tqdm(chunks, desc="Processing chunks")):
            try:
                audio = self.generate_audio_chunk(chunk)
                audio_chunks.append(audio)

                # Optionally save individual chunks
                if save_chunks:
                    chunk_file = chunk_dir / f"chunk_{i+1:04d}.wav"
                    ta.save(str(chunk_file), audio, self.sample_rate)

            except Exception as e:
                print(f"\nERROR processing chunk {i+1}: {e}")
                print(f"Chunk text: {chunk[:100]}...")
                continue

        if not audio_chunks:
            print("\nERROR: No audio chunks were generated!")
            return

        # Merge chunks
        print(f"\nMerging {len(audio_chunks)} audio chunks...")
        merged_audio = self.merge_audio_chunks(audio_chunks, silence_duration)

        # Save final audiobook
        print(f"Saving audiobook to: {output_file}")
        ta.save(output_file, merged_audio, self.sample_rate)

        # Calculate duration
        duration_seconds = merged_audio.shape[1] / self.sample_rate
        duration_minutes = duration_seconds / 60
        print(f"\n✓ Audiobook generated successfully!")
        print(f"  Duration: {duration_minutes:.1f} minutes ({duration_seconds:.1f} seconds)")
        print(f"  Output: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate audiobooks from text files using Chatterbox TTS"
    )
    parser.add_argument(
        "input_file",
        help="Path to input text file (.txt)"
    )
    parser.add_argument(
        "-o", "--output",
        default="audiobook.wav",
        help="Output audio file path (default: audiobook.wav)"
    )
    parser.add_argument(
        "-v", "--voice",
        help="Path to reference audio for voice cloning (.wav, .mp3, etc.)"
    )
    parser.add_argument(
        "-c", "--chunk-size",
        type=int,
        default=500,
        help="Maximum characters per chunk (default: 500)"
    )
    parser.add_argument(
        "-s", "--silence",
        type=float,
        default=0.5,
        help="Silence duration between chunks in seconds (default: 0.5)"
    )
    parser.add_argument(
        "--save-chunks",
        action="store_true",
        help="Save individual chunk audio files"
    )
    parser.add_argument(
        "--device",
        choices=["cuda", "cpu"],
        default="cuda",
        help="Device to run on (default: cuda)"
    )

    args = parser.parse_args()

    # Check input file exists
    if not os.path.exists(args.input_file):
        print(f"ERROR: Input file not found: {args.input_file}")
        exit(1)

    # Check voice reference if provided
    if args.voice and not os.path.exists(args.voice):
        print(f"ERROR: Voice reference file not found: {args.voice}")
        exit(1)

    # Create output directory if needed
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Initialize generator
    generator = AudiobookGenerator(
        device=args.device,
        voice_reference=args.voice
    )

    # Generate audiobook
    generator.generate_audiobook(
        input_file=args.input_file,
        output_file=args.output,
        chunk_size=args.chunk_size,
        silence_duration=args.silence,
        save_chunks=args.save_chunks
    )


if __name__ == "__main__":
    main()
