@echo off
REM Batch script to process multiple chapter files
REM Place all chapter files as chapter_01.txt, chapter_02.txt, etc.
REM Place your voice reference as voice_reference.wav

echo ========================================
echo Chatterbox TTS Batch Audiobook Generator
echo ========================================
echo.

REM Check if voice_reference.wav exists
if not exist "voice_reference.wav" (
    echo WARNING: voice_reference.wav not found!
    echo Processing will use default voice.
    echo.
    set VOICE_ARG=
) else (
    echo Using voice reference: voice_reference.wav
    echo.
    set VOICE_ARG=-v voice_reference.wav
)

REM Create output directory
if not exist "output" mkdir output

REM Process each chapter file
for %%f in (chapter_*.txt) do (
    echo ========================================
    echo Processing: %%f
    echo ========================================
    python audiobook_generator.py "%%f" -o "output\%%~nf.wav" %VOICE_ARG% -c 800 -s 0.7
    echo.
    echo Completed: %%f
    echo Output: output\%%~nf.wav
    echo.
)

echo ========================================
echo All chapters processed!
echo Output files are in the 'output' folder
echo ========================================
pause
