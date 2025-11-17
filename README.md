# Chatterbox TTS Audiobook Generator

A Python script for generating high-quality audiobooks from text files using Chatterbox TTS with voice cloning support.

## ✨ Features

- 🎙️ **Voice Cloning**: Clone any voice with just 6-10 seconds of audio
- 📚 **Smart Text Processing**: Automatically splits text at sentence boundaries
- 🔊 **High Quality Output**: 24kHz professional audio quality
- ⚡ **GPU Accelerated**: Fast processing on NVIDIA GPUs (RTX 3060 recommended)
- 🎨 **Emotion Control**: Natural emotional expression from Chatterbox TTS
- 🌍 **Multilingual**: Supports 23 languages
- 💾 **Chunk Management**: Optionally save individual chunks for debugging
- 🔧 **Flexible**: Command-line interface with many options

## 🚀 Quick Start

### 1. Install Dependencies
```bash
# Install PyTorch with CUDA support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Install Chatterbox TTS
pip install chatterbox-tts

# Install other dependencies
pip install tqdm
```

### 2. Basic Usage
```bash
# Generate with default voice
python audiobook_generator.py example_book.txt -o audiobook.wav

# Generate with voice cloning
python audiobook_generator.py example_book.txt -o audiobook.wav -v voice_reference.wav
```

## 📖 Documentation

See [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) for:
- Complete installation instructions
- Detailed usage examples
- Voice cloning tips
- Troubleshooting guide
- Processing tips for long books

## 💻 System Requirements

- **GPU**: NVIDIA RTX 3060 or better (6GB+ VRAM)
- **RAM**: 16GB+ recommended
- **Python**: 3.10 or 3.11
- **CUDA**: 11.8 or 12.x
- **Storage**: ~5-10GB for models and outputs

## 📝 Command-Line Options

```
usage: audiobook_generator.py [-h] [-o OUTPUT] [-v VOICE] [-c CHUNK_SIZE]
                              [-s SILENCE] [--save-chunks] [--device {cuda,cpu}]
                              input_file

positional arguments:
  input_file            Path to input text file (.txt)

optional arguments:
  -h, --help            Show help message
  -o, --output          Output audio file path (default: audiobook.wav)
  -v, --voice           Reference audio for voice cloning
  -c, --chunk-size      Max characters per chunk (default: 500)
  -s, --silence         Silence between chunks in seconds (default: 0.5)
  --save-chunks         Save individual chunk audio files
  --device              Device: cuda or cpu (default: cuda)
```

## 🎯 Example Usage

```bash
# Basic audiobook generation
python audiobook_generator.py my_book.txt

# With voice cloning and custom settings
python audiobook_generator.py my_book.txt \
  -o "My_Audiobook.wav" \
  -v narrator_voice.wav \
  -c 800 \
  -s 0.7

# Save individual chunks for debugging
python audiobook_generator.py my_book.txt \
  -o output.wav \
  --save-chunks

# Run on CPU (slower)
python audiobook_generator.py my_book.txt \
  --device cpu
```

## 📊 Expected Performance (RTX 3060)

- **Processing Speed**: ~5-10 seconds per chunk
- **100k word book**: ~2-3 hours total processing time
- **VRAM Usage**: 6-8GB
- **Output Quality**: 24kHz, professional audiobook quality

## 🎤 Voice Cloning Tips

1. **Use 6-10 seconds** of clear reference audio
2. **No background noise** - clean speech only
3. **Single speaker** - one voice at a time
4. **Natural emotion** - helps the model learn expression
5. **Good sources**: Audiobook samples, voice actor demos, LibriVox

## 📁 File Structure

```
TTS/
├── audiobook_generator.py    # Main script
├── INSTALLATION_GUIDE.md     # Complete guide
├── README.md                 # This file
├── requirements.txt          # Dependencies
└── example_book.txt          # Test file
```

## 🔧 Troubleshooting

### CUDA Out of Memory
- Reduce chunk size: `-c 300`
- Close other GPU applications
- Use CPU mode: `--device cpu`

### Poor Voice Cloning
- Use longer reference (10-15 seconds)
- Ensure reference is clean and clear
- Add natural emotion to reference

### Slow Processing
- Ensure GPU is being used: `nvidia-smi`
- Close unnecessary applications
- Consider processing in chapters

See [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) for more troubleshooting.

## 📄 License

This script uses Chatterbox TTS which is licensed under MIT License by Resemble AI.

## 🙏 Credits

- **Chatterbox TTS**: Resemble AI (https://github.com/resemble-ai/chatterbox)
- **PyTorch**: Facebook AI Research
- Script by: Claude Code

## 📞 Support

For Chatterbox TTS issues: https://github.com/resemble-ai/chatterbox/issues

---

**Ready to create your audiobook?** See [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) to get started!
