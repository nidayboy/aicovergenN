@echo off
title AICoverGen WebUI
cd /d "%~dp0"

echo ====================================================
echo Starting AICoverGen WebUI...
echo ====================================================

REM Ensure FFmpeg and SoX are in PATH
set "PATH=C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin;C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\ChrisBagwell.SoX_Microsoft.Winget.Source_8wekyb3d8bbwe\sox-14.4.2;%PATH%"

REM Launch WebUI
.venv\Scripts\python.exe src\webui.py %*

if %ERRORLEVEL% neq 0 (
    echo.
    echo An error occurred while running AICoverGen.
    pause
)
