"""
Test script to verify Chatterbox TTS installation
Run this after installing to check if everything works correctly.
"""

import sys

def check_python_version():
    """Check Python version is 3.10 or 3.11"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor in [10, 11]:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} - WARNING: Recommended 3.10 or 3.11")
        return False

def check_pytorch():
    """Check PyTorch installation and CUDA availability"""
    print("\nChecking PyTorch...")
    try:
        import torch
        print(f"✓ PyTorch {torch.__version__} installed")

        if torch.cuda.is_available():
            print(f"✓ CUDA is available")
            print(f"  GPU: {torch.cuda.get_device_name(0)}")
            print(f"  CUDA Version: {torch.version.cuda}")
            print(f"  VRAM: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
            return True
        else:
            print("✗ CUDA not available - will run on CPU (slower)")
            return False
    except ImportError:
        print("✗ PyTorch not installed")
        print("  Install with: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121")
        return False

def check_chatterbox():
    """Check Chatterbox TTS installation"""
    print("\nChecking Chatterbox TTS...")
    try:
        from chatterbox.tts import ChatterboxTTS
        print("✓ Chatterbox TTS installed")
        return True
    except ImportError:
        print("✗ Chatterbox TTS not installed")
        print("  Install with: pip install chatterbox-tts")
        return False

def check_dependencies():
    """Check other dependencies"""
    print("\nChecking dependencies...")

    deps = {
        'torchaudio': 'torchaudio',
        'tqdm': 'tqdm',
    }

    all_ok = True
    for name, package in deps.items():
        try:
            __import__(package)
            print(f"✓ {name} installed")
        except ImportError:
            print(f"✗ {name} not installed")
            print(f"  Install with: pip install {package}")
            all_ok = False

    return all_ok

def test_simple_generation():
    """Test basic text-to-speech generation"""
    print("\nTesting basic TTS generation...")
    try:
        import torch
        from chatterbox.tts import ChatterboxTTS
        import torchaudio as ta

        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"  Loading model on {device}...")

        model = ChatterboxTTS.from_pretrained(device=device)
        print(f"  Model loaded (sample rate: {model.sr} Hz)")

        print("  Generating test audio...")
        text = "This is a test of the Chatterbox text to speech system."
        wav = model.generate(text)

        # Save test file
        test_file = "test_installation_output.wav"
        ta.save(test_file, wav, model.sr)

        duration = wav.shape[1] / model.sr
        print(f"✓ Test successful!")
        print(f"  Generated {duration:.1f} seconds of audio")
        print(f"  Saved to: {test_file}")
        print(f"  Listen to this file to verify audio quality")

        return True
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False

def main():
    print("=" * 60)
    print("Chatterbox TTS Installation Test")
    print("=" * 60)

    results = []

    # Run all checks
    results.append(("Python Version", check_python_version()))
    results.append(("PyTorch + CUDA", check_pytorch()))
    results.append(("Chatterbox TTS", check_chatterbox()))
    results.append(("Dependencies", check_dependencies()))

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    for name, status in results:
        status_str = "✓ PASS" if status else "✗ FAIL"
        print(f"{name:20} {status_str}")

    all_passed = all(status for _, status in results)

    if all_passed:
        print("\n✓ All checks passed! Running generation test...")
        test_result = test_simple_generation()

        if test_result:
            print("\n" + "=" * 60)
            print("🎉 SUCCESS! Installation is working correctly!")
            print("=" * 60)
            print("\nNext steps:")
            print("1. Listen to 'test_installation_output.wav'")
            print("2. If it sounds good, you're ready to generate audiobooks!")
            print("3. See QUICK_START.md for usage examples")
        else:
            print("\n" + "=" * 60)
            print("⚠️ Installation checks passed but generation test failed")
            print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("⚠️ Some checks failed - please fix the issues above")
        print("=" * 60)
        print("\nSee INSTALLATION_GUIDE.md for help")

if __name__ == "__main__":
    main()
