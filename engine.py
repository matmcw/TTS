"""
Core TTS engine wrapping Chatterbox.
Handles text chunking, audio generation, merging, and optional post-processing.
"""

import re
import tempfile
from pathlib import Path
from typing import Optional

import torch
import torchaudio as ta

try:
    from chatterbox.tts import ChatterboxTTS
except ImportError:
    raise ImportError("chatterbox-tts not installed. Run: pip install chatterbox-tts")


def _chunk_text(text: str, max_chars: int = 500) -> list[str]:
    """Split text on sentence boundaries."""
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    chunks = []
    current = ""
    for sentence in sentences:
        if len(current) + len(sentence) + 1 <= max_chars:
            current = (current + " " + sentence).strip()
        else:
            if current:
                chunks.append(current)
            current = sentence
    if current:
        chunks.append(current)
    return chunks if chunks else [text.strip()]


class TTSEngine:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[TTS] Loading Chatterbox on {self.device}...")
        self.model = ChatterboxTTS.from_pretrained(device=self.device)
        self.sample_rate = self.model.sr
        print(f"[TTS] Ready. Sample rate: {self.sample_rate} Hz")

    def synthesize(
        self,
        text: str,
        voice_reference: Optional[str] = None,
        exaggeration: float = 0.5,
        cfg_weight: float = 0.5,
        temperature: float = 0.8,
        chunk_size: int = 500,
        silence_duration: float = 0.3,
        post_process: bool = False,
        output_path: Optional[str] = None,
    ) -> Path:
        """
        Synthesize text to a WAV file. Returns the output path.

        Args:
            text: Text to synthesize.
            voice_reference: Path to a reference audio clip for voice cloning.
            exaggeration: Emotional intensity (0.25 = flat, 1.0+ = dramatic).
            cfg_weight: Pacing/guidance — lower is faster and more creative.
            temperature: Randomness — lower is more consistent, higher is more varied.
            chunk_size: Max characters per chunk before splitting.
            silence_duration: Seconds of silence inserted between chunks.
            post_process: Apply wind-grain audio enhancement.
            output_path: Where to write the WAV (temp file if None).
        """
        chunks = _chunk_text(text, max_chars=chunk_size)
        audio_parts = []

        for chunk in chunks:
            wav = self.model.generate(
                chunk,
                audio_prompt_path=voice_reference,
                exaggeration=exaggeration,
                cfg_weight=cfg_weight,
                temperature=temperature,
            )
            audio_parts.append(wav)

        if not audio_parts:
            raise RuntimeError("No audio was generated.")

        # Insert silence between chunks
        silence_samples = int(self.sample_rate * silence_duration)
        silence = torch.zeros(1, silence_samples)
        merged_parts = []
        for i, part in enumerate(audio_parts):
            merged_parts.append(part)
            if i < len(audio_parts) - 1:
                merged_parts.append(silence)
        combined = torch.cat(merged_parts, dim=1)

        if self.device == "cuda":
            torch.cuda.empty_cache()

        if output_path is None:
            tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
            output_path = tmp.name
            tmp.close()

        ta.save(output_path, combined, self.sample_rate)

        if post_process:
            from post_processing import enhance_audio
            enhance_audio(output_path, output_path)

        return Path(output_path)
