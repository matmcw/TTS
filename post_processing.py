"""
Wind-Grain Audio Enhancer
-------------------------
This script enhances AI-generated speech by adding a subtle, airy
wind-like grain and optional tiny early reflections — without
causing muffling, underwater artifacts, or reverb smearing.

Processing Steps:
1. Normalize audio
2. Very light EQ (removes only harsh peaks, keeps audio crisp)
3. Add high-frequency wind-like grain (filtered noise)
4. Add micro-early-reflections for realism (not reverb mud)
5. Normalize again
"""

import numpy as np
import soundfile as sf
from scipy.signal import fftconvolve
import sys


# --------------------------------------------------------------
# Load WAV safely (preserves original sample format)
# --------------------------------------------------------------
def load_audio(path):
    samples, rate = sf.read(path, always_2d=False)
    samples = samples.astype(np.float32)
    return samples, rate


# --------------------------------------------------------------
# Save WAV safely without corrupting pitch or speed
# --------------------------------------------------------------
def save_audio(path, samples, rate):
    sf.write(path, samples, rate)


# --------------------------------------------------------------
# Simple normalization
# --------------------------------------------------------------
def normalize(samples):
    peak = np.max(np.abs(samples))
    if peak < 1e-9:
        return samples
    return samples / peak * 0.95


# --------------------------------------------------------------
# Very light EQ to keep audio crisp — no underwater muffling
# --------------------------------------------------------------
def apply_eq(samples, rate):
    freq = np.fft.rfftfreq(len(samples), 1.0 / rate)
    spectrum = np.fft.rfft(samples)

    # Light HF smoothing (reduces AI sharpness without muffling)
    hf_mask = 1 - 0.05 * np.exp(-(freq - 6000)**2 / (2 * 3000**2))
    spectrum *= hf_mask

    return np.fft.irfft(spectrum).astype(np.float32)


# --------------------------------------------------------------
# Wind-like grain (high-frequency filtered noise)
# --------------------------------------------------------------
def add_wind_grain(samples, rate, intensity=0.004):
    noise = np.random.normal(0, 1, len(samples)).astype(np.float32)

    # Convert noise to frequency domain
    freqs = np.fft.rfftfreq(len(noise), 1.0 / rate)
    spectrum = np.fft.rfft(noise)

    # High-pass filter (keep only >3kHz)
    hp_mask = (freqs > 3000).astype(np.float32)
    spectrum *= hp_mask

    wind_noise = np.fft.irfft(spectrum).astype(np.float32)

    return samples + wind_noise * intensity


# --------------------------------------------------------------
# Very small early reflections (NOT reverb tail)
# --------------------------------------------------------------
def apply_small_space_reflections(samples, rate):
    ir_length = int(0.03 * rate)  # 30ms
    t = np.linspace(0, 0.03, ir_length)

    # Sharp, fast-decaying reflections
    impulse = np.exp(-t * 50)
    impulse[0] = 1.0

    wet = fftconvolve(samples, impulse, mode='full')[:len(samples)]
    return (samples * 0.90 + wet * 0.10).astype(np.float32)


# --------------------------------------------------------------
# Main processing pipeline
# --------------------------------------------------------------
def enhance_audio(input_path, output_path):
    samples, rate = load_audio(input_path)

    # Downmix to mono if stereo
    if samples.ndim > 1:
        samples = samples.mean(axis=1)

    samples = normalize(samples)
    samples = apply_eq(samples, rate)
    samples = add_wind_grain(samples, rate)
    samples = apply_small_space_reflections(samples, rate)
    samples = normalize(samples)

    save_audio(output_path, samples, rate)
    print(f"Saved processed audio to: {output_path}")


# --------------------------------------------------------------
# Command-line use
# --------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python post-processing.py <input.wav> <output.wav>")
        sys.exit(1)

    enhance_audio(sys.argv[1], sys.argv[2])
