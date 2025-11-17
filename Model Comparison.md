# Comprehensive TTS Models Research for Audiobook Generation (2025)

## Research Overview
This document provides detailed comparisons of the best local/open-source TTS models for audiobook generation in 2025, based on comprehensive web research conducted in November 2025.

---

## 1. Dia 1.6B

### Pre-made Voices
- **Count**: No fixed pre-made voices
- **Selection**: Zero-shot voice cloning - user provides reference audio
- **Preview**: No pre-made voice library to preview

### Voice Cloning
- **Support**: Yes (zero-shot)
- **Audio Needed**: 5-10 seconds for best results
- **Quality**: Can clone specific vocal characteristics using audio prompting feature

### Emotional Expressiveness
- **Rating**: 9/10
- **Details**: Highly realistic dialogue generation in one pass; models non-verbal vocalizations natively; emotion and tone control via audio conditioning; outperforms ElevenLabs in early benchmarks for naturalness and expressiveness

### Non-verbal Sounds
- **Support**: Yes
- **Details**: Can synthesize coughing, laughter, and other non-verbal vocalizations natively

### Speed/Performance
- **Rating**: Fast
- **Details**: Real-time synthesis on consumer-grade devices including MacBooks; optimized inference pipelines

### Audio Quality
- **Rating**: 9.5/10 - Ultra-realistic
- **Characteristics**: 44.1 kHz sampling rate; highly realistic dialogue; superior naturalness

### Hardware Requirements
- **GPU Required**: Yes (NVIDIA with CUDA)
- **VRAM**: ~10GB for full version
- **RAM**: Not specified (standard requirements)
- **Model Size**: 1.6 billion parameters
- **CPU Support**: Planned but not yet available

### Setup Difficulty
- **Rating**: Medium
- **Details**: Straightforward pip install process; requires CUDA-enabled NVIDIA GPU; automatic model download from Hugging Face; some technical knowledge required

### Documentation Quality
- **Rating**: Good
- **Details**: Available on GitHub, Hugging Face, and official website (dia-tts.com); active community; demo page available

### License
- **License**: Apache 2.0
- **Commercial Use**: Yes, free for personal and commercial purposes

### Best For
- Ultra-realistic dialogue generation
- Audiobook narration requiring emotional depth
- Projects needing non-verbal sound synthesis
- Real-time voice applications
- Zero-shot voice cloning with minimal audio

### Limitations
- English-only currently
- Requires ~10GB VRAM
- No CPU support yet
- No pre-made voice library
- Relatively new (released April 2025)

---

## 2. XTTS-v2 (Coqui TTS)

### Pre-made Voices
- **Count**: No fixed pre-made voices
- **Selection**: Zero-shot voice cloning based on user's reference audio
- **Preview**: No pre-made library

### Voice Cloning
- **Support**: Yes (zero-shot)
- **Audio Needed**: 6-10 seconds (6 seconds minimum, 10 seconds recommended)
- **Quality**: 85-95% similarity with just 10 seconds of audio

### Emotional Expressiveness
- **Rating**: 7/10
- **Details**: Emotion and style transfer supported through reference audio; can convey sadness, excitement, anger; no explicit emotion tags; expressiveness comes from reference audio characteristics

### Non-verbal Sounds
- **Support**: Limited
- **Details**: Not a primary feature; emotional transfer possible through audio cloning

### Speed/Performance
- **Rating**: Medium-Fast
- **Details**: Sub-200ms latency for real-time applications; ~2-3GB VRAM usage during operation; DeepSpeed support for 2-4x faster processing with CUDA 11.8+

### Audio Quality
- **Rating**: 8/10 - High quality
- **Characteristics**: Natural sounding; good for multilingual applications; streaming mode available (uses +2GB VRAM)

### Hardware Requirements
- **GPU Required**: Recommended (can run on CPU but slower)
- **VRAM**: 4GB minimum, 6GB+ recommended for real-time (8GB for fine-tuning, 12GB+ ideal)
- **RAM**: 16GB minimum, 24GB+ recommended for fine-tuning
- **Model Size**: ~2GB
- **CPU Support**: Yes (slower performance)

### Setup Difficulty
- **Rating**: Medium
- **Details**: Standard Python/pip installation; requires PyTorch setup; well-documented but company closed in December 2024 (open-source continues)

### Documentation Quality
- **Rating**: Good
- **Details**: Extensive documentation available; community maintained after Coqui closure; Hugging Face model page; active GitHub discussions

### License
- **License**: Mozilla Public License 2.0 (MPL-2.0)
- **Commercial Use**: Yes, with conditions

### Best For
- Multilingual projects (17 languages supported)
- Voice cloning with minimal audio samples
- Real-time applications with low latency
- Projects requiring style/emotion transfer
- Commercial applications with reasonable hardware

### Limitations
- Company shut down December 2024 (community maintained)
- Emotion control less granular than some alternatives
- Fine-tuning requires significant VRAM (12GB+)
- No explicit emotion tagging system
- Limited non-verbal sound generation

---

## 3. Fish Speech V1.5

### Pre-made Voices
- **Count**: No fixed pre-made voices
- **Selection**: Zero-shot voice cloning with user reference audio
- **Preview**: No pre-made library

### Voice Cloning
- **Support**: Yes (instant high-quality cloning)
- **Audio Needed**: 10-30 seconds for quality output; 30-45 seconds ideal (2-3 clips of 15-20s); 30-180 minutes for advanced training
- **Quality**: High-quality instant voice cloning with <150ms latency

### Emotional Expressiveness
- **Rating**: 9/10
- **Details**: Extensive emotional control with 50+ emotions and tone markers; supports angry, sad, excited, surprised, satisfied, delighted, scared, worried, upset, nervous, frustrated, depressed, empathetic, embarrassed, disgusted, moved, proud, relaxed, grateful, confident, interested, curious, confused, joyful, and many more; can include subtle cues like laughter or crying; matches emotion of provided speaker recording

### Non-verbal Sounds
- **Support**: Yes
- **Details**: Supports laughter, crying, and other emotional markers; over 50 emotion and tone markers including non-verbal cues

### Speed/Performance
- **Rating**: Fast
- **Details**: <150ms latency; real-time factor approximately 1:7 on Nvidia RTX 4090; real-time synthesis capability

### Audio Quality
- **Rating**: 9/10 - State-of-the-art
- **Characteristics**: #2 ranked on TTS-Arena (as "Anonymous Sparkle"); trained on 1 million+ hours of audio data (300K+ hours each for English and Chinese, 100K+ for Japanese)

### Hardware Requirements
- **GPU Required**: Yes (Nvidia, Apple Silicon, or CPU)
- **VRAM**: 12GB recommended for optimal performance
- **RAM**: Standard requirements
- **Model Size**: Not specified (uses updated vocoder)
- **CPU Support**: Yes (slower)

### Setup Difficulty
- **Rating**: Easy-Medium
- **Details**: Gradio-based web UI; compatible with Chrome, Firefox, Edge; pretrained models open source; easy self-hosting or cloud options

### Documentation Quality
- **Rating**: Good
- **Details**: GitHub repository with comprehensive guides; web UI; cloud deployment options; active development

### License
- **License**: Not explicitly stated (open-source on GitHub)
- **Commercial Use**: Appears to be permitted (community contributions welcome)

### Best For
- Multilingual projects (13 languages: English, Chinese, Japanese, Korean, and dialects)
- Projects requiring extensive emotional control (50+ emotions)
- High-quality voice cloning with minimal latency
- Applications needing non-verbal sound synthesis
- Audiobooks requiring emotional depth and variety

### Limitations
- 12GB VRAM recommended (may limit some hardware)
- Requires quality audio samples (MP3 192kbps+, no background noise)
- Single speaker per clip with steady volume/tone/emotion
- Limited information on licensing terms

---

## 4. Bark

### Pre-made Voices
- **Count**: 100+ speaker presets
- **Selection**: Yes, can choose from library of speaker presets across supported languages
- **Preview**: Yes, presets available; community shares presets on Discord

### Voice Cloning
- **Support**: No traditional voice cloning
- **Audio Needed**: N/A - uses prompt-based generation with presets
- **Quality**: Cannot clone custom voices; relies on built-in presets

### Emotional Expressiveness
- **Rating**: 8/10
- **Details**: Generative nature allows emotionally expressive speech naturally; tries to match tone, pitch, emotion, and prosody of given preset; proficiency in emulating nonverbal communications adds emotional depth and realism

### Non-verbal Sounds
- **Support**: Yes (Major Strength)
- **Details**: Produces laughing, sighing, crying, and other nonverbal communications; use annotations like [laughs], [sighs], etc. in text prompts; can generate music and background noise

### Speed/Performance
- **Rating**: Slow
- **Details**: Significantly higher latency; cannot process beyond 50 words at a time; generative model can deviate from script; not suitable for real-time applications

### Audio Quality
- **Rating**: 8/10 - High quality, expressive
- **Characteristics**: Fully generative text-to-audio model; highly realistic multilingual speech; rich emotional depth; can produce music and sound effects

### Hardware Requirements
- **GPU Required**: Yes (can run on CPU but very slow)
- **VRAM**: Full version: ~12GB; Small version: 8GB; Minimum: ~2GB (with CPU offloading)
- **RAM**: Standard requirements
- **Model Size**: Two versions - suno/bark (large) and suno/bark-small
- **CPU Support**: Yes (use SUNO_OFFLOAD_CPU=True, but extremely slow)

### Setup Difficulty
- **Rating**: Medium
- **Details**: Python package installation via pip; environment variables for small models/CPU offloading; well-documented on GitHub

### Documentation Quality
- **Rating**: Good
- **Details**: Comprehensive GitHub documentation; Hugging Face model pages; community Discord; multiple tutorials available

### License
- **License**: MIT License
- **Commercial Use**: Yes, fully permitted

### Best For
- Non-verbal sound generation (laughs, sighs, crying)
- Emotionally expressive content
- Projects with 100+ preset voices across languages
- Creative audio with music and sound effects
- Multilingual applications (prompts in various languages)
- Non-real-time audiobook generation

### Limitations
- No custom voice cloning capability
- Very slow processing (minutes per sentence on GPU)
- Cannot process more than 50 words at once
- Generative nature can deviate from script
- Requires 8-12GB VRAM for best performance
- Not suitable for real-time applications
- Unpredictable output (fully generative)

---

## 5. Piper TTS

### Pre-made Voices
- **Count**: 30+ languages with multiple voices per language
- **Selection**: Yes, can choose from available voice models
- **Preview**: Yes, voice samples available at rhasspy.github.io/piper-samples/
- **Details**: English (US) has most extensive selection; organized hierarchically by language, speaker/dataset, and quality level; exact count varies as new voices added to repository

### Voice Cloning
- **Support**: Yes (through training/fine-tuning)
- **Audio Needed**: ~1300 phrases for fine-tuning, ~13,000 for training from scratch; recent advances allow fine-tuning from single phrase using advanced techniques
- **Quality**: Good with proper training data; can create custom voice models

### Emotional Expressiveness
- **Rating**: 5/10
- **Details**: Basic prosody; less emotionally expressive than neural generative models; focuses on speed and efficiency over expressiveness

### Non-verbal Sounds
- **Support**: No
- **Details**: Standard speech synthesis only

### Speed/Performance
- **Rating**: Very Fast
- **Details**: Fastest TTS option; processes short texts in under a second; real-time factor (RTF) values < 1.0; optimized for Raspberry Pi 4; AI-based but incredibly fast

### Audio Quality
- **Rating**: 7/10 - Good quality, efficient
- **Characteristics**: Uses ONNX models trained with VITS; quality levels from x_low to high (16kHz to 22.05kHz); balances file size, speed, and quality

### Hardware Requirements
- **GPU Required**: No
- **VRAM**: N/A (CPU-based)
- **RAM**: 2GB+ (runs on Raspberry Pi 4)
- **Model Size**: Varies by quality level (optimized for small size)
- **CPU Support**: Yes (primary mode)

### Setup Difficulty
- **Rating**: Easy
- **Details**: Simple installation; runs on weak hardware; optimized for embedded devices; Piper Recording Studio available for dataset creation

### Documentation Quality
- **Rating**: Good
- **Details**: VOICES.md file with complete list; GitHub documentation; OpenHAB integration docs; voice samples online; note: development moved to github.com/OHF-Voice/piper1-gpl (original archived Oct 2025)

### License
- **License**: MIT-style open source (now part of Open Home Foundation as piper1-gpl)
- **Commercial Use**: Yes

### Best For
- Fast, low-latency applications
- Embedded devices and Raspberry Pi projects
- Privacy-conscious/offline applications
- Projects with limited hardware resources
- Smart home integrations (OpenHAB, etc.)
- Applications requiring many language options
- Custom voice creation with training

### Limitations
- Lower emotional expressiveness than neural models
- No non-verbal sound support
- No zero-shot voice cloning (requires training)
- Voice training requires significant dataset
- Original repository archived (moved to OHF-Voice)
- Quality lower than state-of-the-art neural models
- Not ideal for audiobook narration requiring emotion

---

## 6. Tacotron 2

### Pre-made Voices
- **Count**: 1 (original female speaker model)
- **Selection**: Limited; primarily single-speaker base model
- **Preview**: Based on professional female speaker from original training

### Voice Cloning
- **Support**: Yes (with modifications and fine-tuning)
- **Audio Needed**: 1-2 hours of audio for robust voice cloning; 24.6 hours for full training (original model)
- **Quality**: Good with proper training; can achieve high similarity with sufficient data

### Emotional Expressiveness
- **Rating**: 6/10
- **Details**: Prosody encoders can be added to enhance emotional information; supports speech style control and prosody control; Coqui TTS implementation supports emotional synthesis; less natural than modern alternatives

### Non-verbal Sounds
- **Support**: No
- **Details**: Standard speech synthesis only

### Speed/Performance
- **Rating**: Medium-Slow
- **Details**: Autoregressive architecture makes inference slower; training takes considerable time depending on hardware; not suitable for real-time applications

### Audio Quality
- **Rating**: 8/10 - High quality, natural
- **Characteristics**: MOS score of 4.53/5; highly natural sounding; fluid intonation; well-suited for offline content like audiobooks

### Hardware Requirements
- **GPU Required**: Recommended (can train on Google Colab free GPUs)
- **VRAM**: 8GB+ for training
- **RAM**: 8GB+ recommended
- **Model Size**: Moderate (mel-spectrogram generator + vocoder like HiFi-GAN)
- **CPU Support**: Yes (very slow for training, acceptable for inference)

### Setup Difficulty
- **Rating**: Medium-Hard
- **Details**: Requires high-quality microphone (~$50+); PyTorch setup required; separate vocoder needed (HiFi-GAN, WaveGlow); multiple components to configure

### Documentation Quality
- **Rating**: Good
- **Details**: Original Google paper; PyTorch implementations; numerous community tutorials; well-established architecture

### License
- **License**: Various (depends on implementation; original by Google)
- **Commercial Use**: Generally yes (verify specific implementation)

### Best For
- Offline content like audiobook narration where quality is essential
- Batch processing where latency is not critical
- Research and educational purposes
- Projects with ample training time and data
- Single-speaker high-quality synthesis

### Limitations
- Cannot precisely control and synthesize diverse speech samples
- Slower inference due to autoregressive architecture
- Speaker characteristics (d-vector) cannot capture full voice information
- Requires significant training data (1-2 hours minimum)
- Setup requires multiple components (TTS + vocoder)
- Limited emotional control compared to modern models
- No zero-shot voice cloning
- Training can take hours to days depending on hardware

---

## 7. StyleTTS2

### Pre-made Voices
- **Count**: No fixed pre-made voices
- **Selection**: Zero-shot synthesis with reference audio
- **Preview**: No pre-made library

### Voice Cloning
- **Support**: Yes (zero-shot)
- **Audio Needed**: 5-10 seconds of reference voice
- **Quality**: Remarkably captures speaker's timbre, prosody, and pronunciation; human-level quality

### Emotional Expressiveness
- **Rating**: 9/10
- **Details**: Embedding_scale parameter controls emotional intensity (higher = more emotional); can synthesize expressive speech in varied emotions without explicit emotion labels; distinct speaker clusters show wide stylistic diversity; emotion-based clusters allow manipulating emotional tone regardless of reference audio; probabilistic models generate more expressive speech than deterministic ones

### Non-verbal Sounds
- **Support**: Limited
- **Details**: Not a primary feature; focuses on speech synthesis

### Speed/Performance
- **Rating**: Fast
- **Details**: Memory footprint of just 2GB VRAM; inference in ~2-3 seconds on RTX 3050M; faster than other diffusion models (requires only style vector to sample whole speech)

### Audio Quality
- **Rating**: 9.5/10 - Human-level
- **Characteristics**: 24kHz sample rate; uses large Speech Language Models (WavLM) as discriminators; captures accents, emotions, and tones effectively; comparable to human speech

### Hardware Requirements
- **GPU Required**: Yes (T4, RTX 3050M or better)
- **VRAM**: Inference: 2GB; Training: 24GB (RTX 3090 recommended); max_length=500 (6.25s) uses almost all VRAM on 24GB GPU
- **RAM**: Standard requirements
- **Model Size**: Compact (2GB VRAM for inference)
- **CPU Support**: Not recommended

### Setup Difficulty
- **Rating**: Medium-Hard
- **Details**: Python >= 3.9 required (supports 3.9, 3.10); requires multiple dependencies (SoundFile, torchaudio, torch, transformers, phonemizer, etc.); GPL-licensed packages separate from main repo (MIT-licensed inference available)

### Documentation Quality
- **Rating**: Good
- **Details**: Comprehensive GitHub repository (github.com/yl4579/StyleTTS2); research paper available; pip installable package; community tutorials

### License
- **License**: Inference with MIT libraries available; full version depends on GPL-licensed packages
- **Commercial Use**: Yes with MIT-licensed version; verify GPL implications

### Best For
- Human-level text-to-speech quality
- Zero-shot voice cloning with minimal audio
- Emotionally expressive content
- Projects requiring varied emotional tones
- Audiobook narration with emotional depth
- Low VRAM requirements (2GB inference)

### Limitations
- Training requires 24GB VRAM (RTX 3090-level GPU)
- Limited non-verbal sound support
- Setup complexity with multiple dependencies
- Licensing complexity (GPL vs MIT versions)
- Pre-trained model usage requires informing listeners
- Python version restricted to 3.9-3.10
- Out of memory issues during SLM adversarial training

---

## 8. Parler-TTS

### Pre-made Voices
- **Count**: 4 consistent voices (Expresso variant: Jerry, Thomas, Elisabeth, Talia)
- **Selection**: Can specify via text description or use named voices in Expresso
- **Preview**: Yes, through text-based voice descriptions and named Expresso voices

### Voice Cloning
- **Support**: No traditional voice cloning
- **Audio Needed**: N/A - uses text descriptions to control voice characteristics
- **Quality**: N/A (prompt-based control, not cloning)

### Emotional Expressiveness
- **Rating**: 8/10
- **Details**: Parler-TTS Expresso provides superior control over emotions (happy, confused, laughing, sad); precise control via text prompts for emotions, tones, speech rates; enhanced emotional features compared to original model; users can explicitly specify emotions and vocal characteristics

### Non-verbal Sounds
- **Support**: Limited
- **Details**: Parler-TTS Expresso supports laughing as explicit emotion; focuses on emotional speech rather than diverse non-verbal sounds

### Speed/Performance
- **Rating**: Medium
- **Details**: Performance depends on model variant; mini (880M) faster than large (2.3B); batch-size 1 runs on 8GB VRAM; considerable time on CPU-only

### Audio Quality
- **Rating**: 8/10 - High quality, controllable
- **Characteristics**: Trained on 45K hours of audio data; natural-sounding speech; controllable via text prompts (gender, background noise, pitch, speaking rate, reverberation)

### Hardware Requirements
- **GPU Required**: Recommended
- **VRAM**: Mini: 8GB+ for batch-size 1; Large: 12GB+ recommended (4GB minimum with Q4 quantization)
- **RAM**: 8GB+ system RAM
- **Model Size**: Mini: 880M parameters; Large: 2.2-2.3B parameters
- **CPU Support**: Yes (very slow)

### Setup Difficulty
- **Rating**: Easy-Medium
- **Details**: Fully open-source with straightforward installation; available on Hugging Face; permissive license allows easy deployment

### Documentation Quality
- **Rating**: Good
- **Details**: Comprehensive GitHub repository (github.com/huggingface/parler-tts); Hugging Face model cards; training/inference code available; community examples

### License
- **License**: Permissive open-source (Apache 2.0)
- **Commercial Use**: Yes

### Best For
- Text-based voice control without audio samples
- Projects requiring emotional speech control
- Applications needing precise control over voice characteristics
- Multilingual projects (trained on diverse data)
- Users without reference audio for voice cloning
- Consistent named voices (Expresso variant)

### Limitations
- No traditional voice cloning capability
- Limited non-verbal sounds (mainly laughing)
- Requires text-based descriptions rather than audio
- Mini training required 1.5 days on 4x8 H100 GPUs
- Large model (2.3B) requires significant VRAM
- CPU-only inference very slow
- Less suitable for projects requiring voice matching

---

## 9. CosyVoice

### Pre-made Voices
- **Count**: Unknown (not specified)
- **Selection**: Supports built-in pre-configured speech generation
- **Preview**: Likely available through demo interface

### Voice Cloning
- **Support**: Yes (zero-shot)
- **Audio Needed**: 3-10 seconds (official recommendation); real-time voice cloning with low latency
- **Quality**: Supervised semantic tokens significantly outperform unsupervised tokens for content consistency and speaker similarity

### Emotional Expressiveness
- **Rating**: 8/10
- **Details**: Supports adjustable emotion expression; granular emotional controls and accent adjustments; fine-grained control over emotions and prosody via rich text or natural language input; can provide instructions for tone, emotion, and style

### Non-verbal Sounds
- **Support**: Not specified
- **Details**: No explicit information found; focuses on speech synthesis with emotional control

### Speed/Performance
- **Rating**: Fast
- **Details**: Real-time voice cloning with low latency; perfect for interactive applications; efficient real-time processing

### Audio Quality
- **Rating**: 8/10 - High quality
- **Characteristics**: Multilingual large voice generation; trained on extensive data; natural speech synthesis

### Hardware Requirements
- **GPU Required**: No strict requirement (runs on ordinary PC)
- **VRAM**: Not specified (300M-500M parameter models suggest modest requirements)
- **RAM**: Standard PC RAM sufficient
- **Model Size**: CosyVoice-300M (300 million), CosyVoice2-0.5B (500 million)
- **CPU Support**: Yes (slower inference)

### Setup Difficulty
- **Rating**: Medium
- **Details**: Requires Python 3.10; Conda installation recommended; recursive clone needed for submodules; pretrained models must be downloaded; supports command-line and web interfaces; Docker deployment available

### Documentation Quality
- **Rating**: Good
- **Details**: GitHub repository with full-stack ability (github.com/FunAudioLLM/CosyVoice); demo interface available; multiple deployment options

### License
- **License**: Apache 2.0
- **Commercial Use**: Yes; promotes wide usability and community-driven improvements

### Best For
- Multilingual projects (Chinese, English, Japanese, Korean, Cantonese, Sichuanese, Shanghainese, Tianjinese, Wuhanese, etc.)
- Real-time interactive applications
- Natural language-controlled speech synthesis
- Projects requiring emotional control
- Voice cloning with minimal audio (3-10s)
- Users with modest hardware (runs on ordinary PCs)

### Limitations
- No explicit non-verbal sound support mentioned
- Specific VRAM requirements unclear
- Longer audio samples consume more inference performance
- Less information available compared to other models
- Smaller parameter count than some competitors

---

## 10. MaskGCT

### Pre-made Voices
- **Count**: No fixed pre-made voices
- **Selection**: Zero-shot voice cloning with reference audio
- **Preview**: No pre-made library

### Voice Cloning
- **Support**: Yes (zero-shot)
- **Audio Needed**: 3 seconds for ultra-realistic cloning
- **Quality**: Reproduces tone, pacing, stylistic detail, and emotional nuance; human-level similarity; achieves SOTA results

### Emotional Expressiveness
- **Rating**: 9/10
- **Details**: Supports emotion control; trained on 100,000 hours of in-the-wild Emilia dataset with richly diverse multilingual speech; exceeds human-level performance in some benchmarks; emotional nuance accurately reproduced

### Non-verbal Sounds
- **Support**: Not specified
- **Details**: Focus on high-quality speech synthesis; no explicit non-verbal sound mention

### Speed/Performance
- **Rating**: Fast
- **Details**: Fully non-autoregressive architecture = faster inference; does not rely on iterative prediction = simplified synthesis process

### Audio Quality
- **Rating**: 9.5/10 - State-of-the-art
- **Characteristics**: SIM-O scores: 0.728 (English), 0.777 (Chinese) approaching ground-truth; SMOS consistently above 4.1 (higher than any evaluated model, sometimes exceeding ground truth); achieves human-level similarity, naturalness, and intelligibility

### Hardware Requirements
- **GPU Required**: Yes (NVIDIA)
- **VRAM**: 16GB+ recommended; 8GB insufficient (OOM errors reported); fails with <16GB VRAM
- **RAM**: Substantial (model trained on 8x A100 80GB GPUs)
- **Model Size**: T2S-Base and T2S-Large versions; semantic codec (W2v-BERT 2.0); codebook size 8,192
- **CPU Support**: Not recommended

### Setup Difficulty
- **Rating**: Medium
- **Details**: Requires espeak-ng system dependency; Python 3.10 recommended; Conda environment setup; automatic pretrained model download from HuggingFace; multiple usage options (Jupyter, Gradio, Python script); long dependency list

### Documentation Quality
- **Rating**: Good
- **Details**: Comprehensive GitHub documentation (github.com/open-mmlab/Amphion); research paper published at ICLR 2025; multiple tutorials available

### License
- **License**: CC-BY-NC-4.0 (Creative Commons Attribution-NonCommercial 4.0)
- **Commercial Use**: No (requires separate licensing for commercial use)

### Best For
- State-of-the-art voice cloning quality
- Ultra-fast cloning with just 3 seconds audio
- Multilingual projects (English, Chinese, Japanese, French, German, Korean)
- Single voice speaking 6 languages fluently
- Emotion control in speech synthesis
- Voice conversion and speech editing
- Duration controllable speech translation
- Research and non-commercial projects

### Limitations
- Non-commercial license (CC-BY-NC-4.0)
- High VRAM requirement (16GB+ needed)
- Requires 8GB+ VRAM minimum (16GB recommended)
- Complex setup with system dependencies
- High running cost and insufficient engineering optimization
- Trained on 8x A100 GPUs (expensive training)
- No CPU-only option practical
- Commercial use requires separate licensing

---

## 11. Tortoise TTS

### Pre-made Voices
- **Count**: No fixed pre-made voices
- **Selection**: Requires training on custom voice samples
- **Preview**: N/A (custom voices only)

### Voice Cloning
- **Support**: Yes
- **Audio Needed**: ~10 samples of 10 seconds each for optimal results (~100 seconds total)
- **Quality**: Top quality; remarkable similarity with proper samples; 200-parameter autoregressive model produces richest timbre and prosody

### Emotional Expressiveness
- **Rating**: 9/10
- **Details**: Richest timbre and prosody on the market; enhanced in July 2025 for better prosody and emotion; achieves improved human-like speech generation; emphasis on quality over speed

### Non-verbal Sounds
- **Support**: Limited
- **Details**: Not a primary feature; focuses on high-quality speech synthesis

### Speed/Performance
- **Rating**: Very Slow
- **Details**: Single sentence can take minutes on fast GPU; K80: ~2 minutes per medium sentence; "insanely slow"; with optimizations: 0.25-0.3 RTF on 4GB VRAM; streaming: <500ms latency possible; 50% faster on RunPod vs local

### Audio Quality
- **Rating**: 9.5/10 - Top contender for pure quality
- **Characteristics**: Emphasis on quality; trained with focus on naturalness; ideal for offline content like audiobooks; superior audio quality but extremely slow

### Hardware Requirements
- **GPU Required**: Yes (NVIDIA required)
- **VRAM**: 4GB minimum (with optimizations); 8GB+ recommended
- **RAM**: 8GB+ recommended
- **Model Size**: ~200M parameters (autoregressive)
- **CPU Support**: Yes (extremely slow - hours to days for training)

### Setup Difficulty
- **Rating**: Medium-Hard
- **Details**: Requires conda environment with Python 3.9; PyTorch with CUDA support; high-quality microphone (~$50+) for voice cloning; multiple dependencies (numba, inflect, psutil, transformers); can train on Google Colab free GPUs

### Documentation Quality
- **Rating**: Good
- **Details**: GitHub repository (github.com/neonbjb/tortoise-tts); Coqui AI documentation; PyPI package; multiple community tutorials; established architecture

### License
- **License**: Apache License 2.0
- **Commercial Use**: Yes, completely free and open-source

### Best For
- Audiobook narration where quality is essential and latency is not critical
- Offline batch processing
- Projects with unlimited processing time
- Highest quality voice synthesis requirements
- Voice cloning with emphasis on naturalness
- Non-real-time applications

### Limitations
- Extremely slow processing (minutes per sentence)
- K80 GPU: 2 minutes per medium sentence
- Training can take hours to days without GPU
- Requires NVIDIA GPU for practical use
- Requires high-quality microphone for cloning
- Not suitable for real-time applications
- Requires ~10 samples of 10 seconds each
- Complex setup with multiple components
- Processing time makes it impractical for long content

---

## 12. GPT-SoVITS

### Pre-made Voices
- **Count**: No fixed pre-made voices
- **Selection**: Zero-shot and few-shot voice cloning
- **Preview**: N/A (uses reference audio)

### Voice Cloning
- **Support**: Yes (few-shot, as little as 1 minute)
- **Audio Needed**: 5-second sample: 80-95% similarity; 1-minute sample: close to real person effects; fine-tuned models: 1-3 seconds minimum (3+ recommended)
- **Quality**: Can achieve results very similar to ElevenLabs with fine-tuning

### Emotional Expressiveness
- **Rating**: 8/10
- **Details**: Good emotional reproduction; inference faster than real-time on RTX 4090; captures voice characteristics effectively; v2Pro surpasses v4 performance

### Non-verbal Sounds
- **Support**: Limited
- **Details**: Not a primary feature; focuses on voice cloning and TTS

### Speed/Performance
- **Rating**: Fast
- **Details**: Inference faster than real-time on RTX 4090; RTF: 0.028 on 4060Ti, 0.014 on 4090; well-suited for batch processing; balanced quality and speed

### Audio Quality
- **Rating**: 8.5/10 - Very high quality
- **Characteristics**: GPT style encoder + SoVITS vocoder; used as backbone for audiobook evaluation; with fine-tuning achieves near-ElevenLabs quality

### Hardware Requirements
- **GPU Required**: Yes (NVIDIA recommended, AMD ROCm support available)
- **VRAM**: 8GB minimum (6GB+ for smooth operation); GPT has higher VRAM requirements
- **RAM**: Standard requirements
- **Model Size**: Moderate (GPT + SoVITS vocoder)
- **CPU Support**: Yes (slow)

### Setup Difficulty
- **Rating**: Medium (Complex)
- **Details**: Offers one-click installation package and manual setup; straightforward process in few steps; requires great specs and NVIDIA GPU >=6GB VRAM; complex compared to simpler alternatives

### Documentation Quality
- **Rating**: Good
- **Details**: Comprehensive GitHub repository (github.com/RVC-Boss/GPT-SoVITS); multiple forks and community packages; tutorials available; integrated tools (voice separation, ASR, text annotation)

### License
- **License**: MIT License
- **Commercial Use**: Yes, fully permitted

### Best For
- Audiobook generation (well-performed prompt-based TTS)
- Voice cloning with minimal data (1 minute)
- Chinese, English, and Japanese projects
- Multimedia content creators
- Assistive technology developers
- Balance of quality and speed
- Commercial applications

### Limitations
- Currently only supports Chinese, English, and Japanese
- Complex setup despite one-click package
- Requires >=6GB VRAM for smooth operation
- GPT component has higher VRAM requirements
- Reduce batch_size if VRAM insufficient
- v2Pro has higher VRAM usage than v2
- Not as many languages as some alternatives

---

## 13. F5-TTS

### Pre-made Voices
- **Count**: No fixed pre-made voices
- **Selection**: Zero-shot voice cloning with reference audio
- **Preview**: N/A (uses audio prompts)

### Voice Cloning
- **Support**: Yes (zero-shot)
- **Audio Needed**: As short as 10 seconds; brief audio sample sufficient
- **Quality**: Most realistic open-source zero-shot voice clone model; can replicate voice after brief sample

### Emotional Expressiveness
- **Rating**: 8/10
- **Details**: Control over speech emotions and speed; transforms static text into dynamic, expressive speech; trained on ~100,000 hours multilingual data facilitates effective generalization

### Non-verbal Sounds
- **Support**: Not specified
- **Details**: Focus on speech synthesis with emotional control

### Speed/Performance
- **Rating**: Fast
- **Details**: Real-time factor of 0.15 (faster than real-time speech); immediate voice output suitable for live applications; efficient real-time processing with Sway Sampling strategy

### Audio Quality
- **Rating**: 8.5/10 - Advanced quality
- **Characteristics**: Maintains natural intonation and clarity; supports high-quality audio outputs; 335 million parameters; advanced AI with Flow Matching and Diffusion Transformer

### Hardware Requirements
- **GPU Required**: Yes
- **VRAM**: 8-12GB (some sources say ~8GB, others 12-16GB typical)
- **RAM**: 24GB (mentioned in one source with 4GB GPU)
- **Model Size**: 335 million parameters (compact and efficient)
- **CPU Support**: Not recommended (slower processing noted)

### Setup Difficulty
- **Rating**: Easy-Medium
- **Details**: Clone GitHub repository; create Conda virtual environment; install packages and libraries; detailed installation instructions on GitHub

### Documentation Quality
- **Rating**: Good
- **Details**: Comprehensive GitHub repository (github.com/SWivid/F5-TTS); official code for research paper; detailed setup guide

### License
- **License**: Code: MIT License; Pre-trained models: CC-BY-NC (non-commercial due to Emilia training data)
- **Commercial Use**: Code yes, pre-trained models no (non-commercial license)

### Best For
- Zero-shot voice cloning with minimal audio
- Real-time/live applications (RTF 0.15)
- English and Chinese projects (more languages coming)
- Cross-lingual voice cloning (2025 research)
- Efficient processing with reasonable VRAM
- Dynamic, expressive speech synthesis

### Limitations
- Pre-trained models under non-commercial license
- Currently supports primarily English and Chinese
- Higher VRAM needs (~8-12GB)
- Slower processing compared to some alternatives
- Training can cause VRAM OOM issues
- RAM out of memory issues reported during training

---

## 14. Chatterbox (Resemble AI)

### Pre-made Voices
- **Count**: Unknown specific number
- **Selection**: Can use predefined voices or clone custom voices
- **Preview**: Likely available through web UI

### Voice Cloning
- **Support**: Yes (zero-shot, robust multilingual)
- **Audio Needed**: Just a few seconds; 10+ seconds ideal duration in WAV format with 24kHz+ sample rate
- **Quality**: First open-source TTS with emotion exaggeration control and robust multilingual zero-shot cloning

### Emotional Expressiveness
- **Rating**: 9/10
- **Details**: Emotion exaggeration control (novel feature); dial up or tone down emotional expressiveness; supports varied emotions; ideal for professional-quality audiobooks with consistent narration

### Non-verbal Sounds
- **Support**: Limited information
- **Details**: Focus on emotional speech control

### Speed/Performance
- **Rating**: Fast
- **Details**: Faster than real-time inference; alignment-informed generation; accelerated on NVIDIA (CUDA), AMD (ROCm), and Apple Silicon (MPS)

### Audio Quality
- **Rating**: 9/10 - Professional quality
- **Characteristics**: Ideal for audiobook generation; professional-quality output; consistent narration; high-quality speech synthesis

### Hardware Requirements
- **GPU Required**: Recommended (supports NVIDIA, AMD, Apple Silicon)
- **VRAM**: 6-8GB (sources vary: 6-7GB or 8GB)
- **RAM**: 8GB+ system RAM minimum
- **Model Size**: 500 million parameters (0.5B, modified Llama architecture)
- **CPU Support**: Yes (automatic fallback)

### Setup Difficulty
- **Rating**: Easy-Medium
- **Details**: User-friendly Web UI; flexible API endpoints (OpenAI compatible); self-host capable; straightforward setup; large audiobook-scale text processing

### Documentation Quality
- **Rating**: Good
- **Details**: GitHub repository; DigitalOcean tutorial; community resources; active development

### License
- **License**: MIT License
- **Commercial Use**: Yes

### Best For
- Audiobook generation (paste entire books)
- Professional-quality narration with consistent voices
- Emotion exaggeration control
- Multilingual projects (23 languages: Arabic, Danish, German, Greek, English, Spanish, Finnish, French, Hebrew, Hindi, Italian, Japanese, Korean, Malay, Dutch, Norwegian, Polish, Portuguese, Russian, etc.)
- Voice cloning with minimal audio
- Self-hosted solutions
- Commercial applications

### Limitations
- Released May 2025 (relatively new, less battle-tested)
- Specific voice count not documented
- Less detailed technical documentation available
- Requires 10+ seconds quality audio for best results
- Audio should be WAV format, 24kHz+, single speaker, no background noise

---

## 15. OuteTTS (0.3 - Latest)

### Pre-made Voices
- **Count**: No fixed pre-made voices
- **Selection**: Zero-shot voice cloning with reference audio
- **Preview**: N/A (uses audio prompts)

### Voice Cloning
- **Support**: Yes (zero-shot)
- **Audio Needed**: Few seconds of reference audio
- **Quality**: Can replicate new voices with just a few seconds; competitive with larger systems despite small size

### Emotional Expressiveness
- **Rating**: 8/10
- **Details**: Speed and emotion control supported; advanced speech synthesis with emotional capabilities; trained on 20,000 hours of audio

### Non-verbal Sounds
- **Support**: Limited information
- **Details**: Focus on speech synthesis

### Speed/Performance
- **Rating**: Fast
- **Details**: Designed for on-device performance; compatible with llama.cpp for real-time applications; relatively small size enables efficient processing

### Audio Quality
- **Rating**: 8/10 - Competitive quality
- **Characteristics**: Performs competitively despite small size; trained on 20,000 hours; built on LLaMa/Qwen architectures; uses audio tokens directly

### Hardware Requirements
- **GPU Required**: Recommended (NVIDIA, AMD, Vulkan, Apple Silicon)
- **VRAM**: ~1.2GB for 0.6B model (very lightweight)
- **RAM**: Standard requirements
- **Model Size**: 350M (v0.1), 500M (v0.2, v0.3), 1B (v0.3), 600M (v1.0)
- **CPU Support**: Yes (automatic fallback)

### Setup Difficulty
- **Rating**: Easy-Medium
- **Details**: Pip install with hardware-specific options (CUDA, ROCm/HIP, Vulkan, Metal); must specify installation for hardware; supports multiple backends (Transformers, llama.cpp)

### Documentation Quality
- **Rating**: Good
- **Details**: GitHub repository (github.com/edwko/OuteTTS); multiple versions documented; clear installation instructions

### License
- **License**: Apache 2.0
- **Commercial Use**: Yes

### Best For
- On-device applications (small model size)
- Real-time applications (llama.cpp compatible)
- Multilingual projects (v0.3: English, Japanese, Korean, Chinese, French, German)
- Audiobook production
- Virtual assistants
- Educational content
- Accessibility tools
- Cross-platform deployment (NVIDIA, AMD, Vulkan, Apple Silicon)

### Limitations
- Relatively new (v0.3 January 2025)
- Limited battle-testing compared to established models
- Smaller parameter count than some competitors
- Less detailed documentation on specific capabilities
- Performance may not match larger specialized models
- Novel architecture (pure language modeling) less proven

---

## Summary Comparison Table

| Model | Voices | Voice Clone | Emotion | Non-Verbal | Speed | Quality | GPU VRAM | License | Best For |
|-------|--------|-------------|---------|------------|-------|---------|----------|---------|----------|
| **Dia 1.6B** | None (zero-shot) | Yes (5-10s) | 9/10 | Yes | Fast | 9.5/10 | 10GB | Apache 2.0 | Ultra-realistic dialogue, emotional audiobooks |
| **XTTS-v2** | None (zero-shot) | Yes (6-10s) | 7/10 | Limited | Med-Fast | 8/10 | 4-6GB | MPL 2.0 | Multilingual (17 langs), real-time |
| **Fish Speech V1.5** | None (zero-shot) | Yes (10-30s) | 9/10 | Yes | Fast | 9/10 | 12GB | Open-source | 50+ emotions, multilingual (13 langs) |
| **Bark** | 100+ presets | No | 8/10 | Yes (Major) | Slow | 8/10 | 8-12GB | MIT | Non-verbal sounds, creative audio |
| **Piper TTS** | 30+ languages | Training | 5/10 | No | Very Fast | 7/10 | None (CPU) | MIT/GPL | Fast, embedded, offline, Raspberry Pi |
| **Tacotron 2** | 1 base | Yes (1-2hr) | 6/10 | No | Med-Slow | 8/10 | 8GB+ | Various | Batch processing, established architecture |
| **StyleTTS2** | None (zero-shot) | Yes (5-10s) | 9/10 | Limited | Fast | 9.5/10 | 2GB (24GB train) | MIT/GPL | Human-level quality, low VRAM inference |
| **Parler-TTS** | 4 named | No | 8/10 | Limited | Medium | 8/10 | 8-12GB | Apache 2.0 | Text-based voice control, emotions |
| **CosyVoice** | Unknown | Yes (3-10s) | 8/10 | Not specified | Fast | 8/10 | Modest | Apache 2.0 | Multilingual, real-time, modest hardware |
| **MaskGCT** | None (zero-shot) | Yes (3s) | 9/10 | Not specified | Fast | 9.5/10 | 16GB+ | CC-BY-NC-4.0 | SOTA quality, 3s cloning (non-commercial) |
| **Tortoise TTS** | None (custom) | Yes (~100s) | 9/10 | Limited | Very Slow | 9.5/10 | 4-8GB | Apache 2.0 | Highest quality, offline audiobooks |
| **GPT-SoVITS** | None (few-shot) | Yes (1min) | 8/10 | Limited | Fast | 8.5/10 | 8GB | MIT | Audiobooks, Chinese/English/Japanese |
| **F5-TTS** | None (zero-shot) | Yes (10s) | 8/10 | Not specified | Fast (0.15 RTF) | 8.5/10 | 8-12GB | MIT/CC-BY-NC | Real-time apps, English/Chinese |
| **Chatterbox** | Unknown | Yes (few sec) | 9/10 | Limited | Fast | 9/10 | 6-8GB | MIT | Audiobooks, 23 languages, emotion control |
| **OuteTTS 0.3** | None (zero-shot) | Yes (few sec) | 8/10 | Limited | Fast | 8/10 | 1.2GB | Apache 2.0 | On-device, real-time, multilingual |

---

## Top Recommendations by Use Case

### Best for Audiobook Generation (Overall):
1. **Chatterbox** - Purpose-built for audiobooks, emotion control, 23 languages, MIT license
2. **Dia 1.6B** - Ultra-realistic dialogue, emotional depth, non-verbal sounds
3. **GPT-SoVITS** - Proven for audiobooks, balanced quality/speed, MIT license
4. **StyleTTS2** - Human-level quality, low VRAM inference (2GB)
5. **Fish Speech V1.5** - 50+ emotions, excellent quality, fast processing

### Best for Voice Cloning (Minimal Audio):
1. **MaskGCT** - 3 seconds (SOTA but non-commercial)
2. **CosyVoice** - 3-10 seconds, real-time
3. **Dia 1.6B** - 5-10 seconds, ultra-realistic
4. **StyleTTS2** - 5-10 seconds, human-level
5. **OuteTTS** - Few seconds, lightweight (1.2GB VRAM)

### Best for Emotional Expressiveness:
1. **Dia 1.6B** - 9/10, non-verbal sounds
2. **Fish Speech V1.5** - 9/10, 50+ emotions
3. **StyleTTS2** - 9/10, emotion control
4. **Chatterbox** - 9/10, emotion exaggeration control
5. **MaskGCT** - 9/10, emotional nuance

### Best for Non-Verbal Sounds:
1. **Bark** - Major strength (laughs, sighs, crying, music)
2. **Dia 1.6B** - Native support (coughs, laughter)
3. **Fish Speech V1.5** - 50+ markers including laughter, crying

### Best for Limited Hardware:
1. **Piper TTS** - CPU-only, 2GB RAM, Raspberry Pi
2. **OuteTTS** - 1.2GB VRAM
3. **StyleTTS2** - 2GB VRAM inference
4. **XTTS-v2** - 4GB VRAM minimum
5. **CosyVoice** - Runs on ordinary PCs

### Best for Speed:
1. **Piper TTS** - Very fast, RTF < 1.0
2. **F5-TTS** - RTF 0.15 (faster than real-time)
3. **Chatterbox** - Faster than real-time
4. **OuteTTS** - Fast, on-device optimized
5. **Fish Speech V1.5** - <150ms latency

### Best for Commercial Use:
1. **Chatterbox** - MIT, audiobook-focused
2. **Dia 1.6B** - Apache 2.0, ultra-realistic
3. **GPT-SoVITS** - MIT, proven quality
4. **OuteTTS** - Apache 2.0, lightweight
5. **XTTS-v2** - MPL 2.0 (with conditions)

### Best for Multilingual:
1. **Chatterbox** - 23 languages
2. **XTTS-v2** - 17 languages
3. **Fish Speech V1.5** - 13 languages
4. **MaskGCT** - 6 languages (non-commercial)
5. **CosyVoice** - Chinese, English, Japanese, Korean + dialects

### Best Quality (Regardless of Speed):
1. **MaskGCT** - 9.5/10 SOTA (non-commercial)
2. **StyleTTS2** - 9.5/10 human-level
3. **Dia 1.6B** - 9.5/10 ultra-realistic
4. **Tortoise TTS** - 9.5/10 (very slow)
5. **Chatterbox** - 9/10 professional

---

## Research Methodology

This research was conducted through comprehensive web searches in November 2025, focusing on:
- Official documentation and GitHub repositories
- Recent benchmarks and comparisons
- Community feedback and discussions
- Technical specifications from model cards
- Research papers and blog posts
- User experiences and tutorials

All information represents the state of these models as of November 2025. Models continue to evolve, and specifications may change with new releases.

---

## Important Notes

1. **Hardware Requirements**: VRAM requirements are approximate and can vary based on:
   - Model variant (base vs large)
   - Batch size
   - Quantization
   - Optimization settings

2. **Licensing**: Always verify current license terms from official sources before commercial use.

3. **Performance**: Speed ratings are relative and depend on:
   - Hardware configuration
   - Model settings
   - Input length
   - Optimization techniques

4. **Model Development**: Several models mentioned have active development:
   - Piper TTS moved to OHF-Voice/piper1-gpl (archived Oct 2025)
   - Coqui AI shut down Dec 2024 (community maintains XTTS-v2)
   - New models continue to emerge

5. **Voice Quality**: "Best" quality is subjective and depends on:
   - Use case requirements
   - Language
   - Voice characteristics
   - Emotional requirements
   - Non-verbal sound needs

---

## Conclusion

For audiobook generation in 2025, the top recommendations are:

**Commercial-Ready, High Quality:**
- **Chatterbox** - Purpose-built for audiobooks, MIT licensed, 23 languages
- **Dia 1.6B** - Ultra-realistic with emotions, Apache 2.0
- **GPT-SoVITS** - Proven quality, MIT licensed, balanced speed/quality

**Maximum Quality (Speed Secondary):**
- **StyleTTS2** - Human-level quality, 2GB VRAM inference
- **MaskGCT** - SOTA quality but non-commercial license
- **Tortoise TTS** - Highest quality but very slow

**Best Balance:**
- **Fish Speech V1.5** - 50+ emotions, fast, excellent quality
- **F5-TTS** - Real-time capable, good quality, MIT code
- **CosyVoice** - Fast, multilingual, modest hardware

**Limited Hardware:**
- **Piper TTS** - CPU-only, very fast, Raspberry Pi compatible
- **OuteTTS** - 1.2GB VRAM, lightweight, Apache 2.0

The choice depends on specific requirements for licensing, hardware, speed, quality, emotional expressiveness, and language support.
