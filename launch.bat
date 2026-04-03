@echo off
cd /d "%~dp0"
set HF_HUB_OFFLINE=1
start "TTS Server" "D:\Program Files\Python\python.exe" app.py

:wait
timeout /t 2 /nobreak >nul
powershell -Command "try { $c = New-Object System.Net.Sockets.TcpClient('localhost', 7860); $c.Close(); exit 0 } catch { exit 1 }" >nul 2>&1
if errorlevel 1 goto wait

start "" http://127.0.0.1:7860
