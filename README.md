# Local TTS

A general-purpose local text-to-speech tool powered by [Chatterbox](https://github.com/resemble-ai/chatterbox) with a Gradio web UI.

## Features

- High-quality speech synthesis
- Voice cloning from a short reference clip (30+ seconds recommended)
- Exaggeration, guidance, and temperature controls

## Requirements

- **OS:** Windows or Linux
- **GPU:** NVIDIA with 6GB+ VRAM
- **Python:** 3.10, 3.11, or 3.12 ([download](https://www.python.org/downloads/))
- **RAM:** 16GB recommended
- **Storage:** ~5GB free (model + dependencies)

> **Does not work on:** macOS (no CUDA), AMD GPUs, or Python 3.9 / 3.13+

## Setup

**1. Find your CUDA version**

Open a terminal and run:
```
nvidia-smi
```
Look for "CUDA Version" in the top right corner.

**2. Install PyTorch with CUDA**

Replace `cu128` with the version matching your GPU:

| CUDA Version | Command |
|---|---|
| 12.8 | `pip install torch==2.8.0+cu128 torchaudio==2.8.0+cu128 --index-url https://download.pytorch.org/whl/cu128 --no-cache-dir` |
| 12.6 | `pip install torch==2.8.0+cu126 torchaudio==2.8.0+cu126 --index-url https://download.pytorch.org/whl/cu126 --no-cache-dir` |
| 12.4 | `pip install torch==2.8.0+cu124 torchaudio==2.8.0+cu124 --index-url https://download.pytorch.org/whl/cu124 --no-cache-dir` |
| 12.1 | `pip install torch==2.8.0+cu121 torchaudio==2.8.0+cu121 --index-url https://download.pytorch.org/whl/cu121 --no-cache-dir` |
| 11.8 | `pip install torch==2.8.0+cu118 torchaudio==2.8.0+cu118 --index-url https://download.pytorch.org/whl/cu118 --no-cache-dir` |

**3. Install dependencies**
```
pip install -r requirements.txt
```

The Chatterbox model (~3GB) downloads automatically from HuggingFace on first launch.

## Usage

**Windows:** Double-click **`launch.bat`**. The browser opens automatically once the server is ready. To stop, close the terminal window.

**Linux:** Run `python app.py` and open **http://127.0.0.1:7860** in your browser.

## Controls

| Control | Description |
|---|---|
| **Text** | Any text to synthesize |
| **Voice Reference** | Audio clip to clone a specific voice. Without one, the model's built-in default voice is used. There is only one built-in voice. |
| **Exaggeration** | Emotional intensity — 0.35 = calm, 0.5 = default, 0.75 = expressive, 1.0+ = dramatic |
| **Guidance** | Pacing — lower = faster/more creative, higher = more controlled. Reduce when raising exaggeration. |
| **Temperature** | Randomness — lower = more consistent delivery, higher = more varied prosody |
| **Post-processing** | Adds subtle grain and early reflections for a more natural sound |

Generated audio is automatically saved to the `out/` folder with timestamped filenames. You can also download a copy to your downloads folder via the UI.

