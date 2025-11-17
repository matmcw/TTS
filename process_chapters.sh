#!/bin/bash
# Batch script to process multiple chapter files
# Place all chapter files as chapter_01.txt, chapter_02.txt, etc.
# Place your voice reference as voice_reference.wav

echo "========================================"
echo "Chatterbox TTS Batch Audiobook Generator"
echo "========================================"
echo ""

# Check if voice_reference.wav exists
if [ ! -f "voice_reference.wav" ]; then
    echo "WARNING: voice_reference.wav not found!"
    echo "Processing will use default voice."
    echo ""
    VOICE_ARG=""
else
    echo "Using voice reference: voice_reference.wav"
    echo ""
    VOICE_ARG="-v voice_reference.wav"
fi

# Create output directory
mkdir -p output

# Process each chapter file
for file in chapter_*.txt; do
    if [ -f "$file" ]; then
        echo "========================================"
        echo "Processing: $file"
        echo "========================================"

        # Get filename without extension
        filename=$(basename "$file" .txt)

        python audiobook_generator.py "$file" -o "output/${filename}.wav" $VOICE_ARG -c 800 -s 0.7

        echo ""
        echo "Completed: $file"
        echo "Output: output/${filename}.wav"
        echo ""
    fi
done

echo "========================================"
echo "All chapters processed!"
echo "Output files are in the 'output' folder"
echo "========================================"
