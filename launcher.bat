@echo off
:: ===================================================
:: Credit By Ben Timothy
:: Project Name: Youdownneb Launcher (Auto-FFmpeg Setup)
:: Description: Setup Env, Download FFmpeg & Launch Python
:: ===================================================

title Youdownneb Launcher
cls
echo ===================================================
echo             YOUDOWNNEB LAUNCHER
echo          Developed By Ben Timothy
echo ===================================================
echo.

:: 1. Verify Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 goto :PYTHON_NOT_FOUND

:: 2. Upgrade pip and install/update yt-dlp
echo [INFO] Inspecting Python environment and requirements...
python -m pip install --upgrade pip >nul 2>&1
echo [INFO] Checking and upgrading yt-dlp...
python -m pip install --upgrade yt-dlp
echo.

:: 3. Verify and resolve FFmpeg dependency
where ffmpeg >nul 2>&1
if %errorlevel% equ 0 goto :FFMPEG_OK
if exist "ffmpeg.exe" goto :FFMPEG_OK

echo [INFO] FFmpeg is missing. It is required to merge high-res video and extract MP3.
echo [INFO] Downloading portable FFmpeg binary (approx. 60MB), please wait...
echo.

:: Fetch the stable FFmpeg essentials build zip via PowerShell
powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://github.com/GyanD/codexffmpeg/releases/download/6.0/ffmpeg-6.0-essentials_build.zip' -OutFile 'ffmpeg.zip'"

if not exist "ffmpeg.zip" (
    echo [WARNING] Automatic FFmpeg download failed. 
    echo Standard video downloads will still work, but high-res merging and MP3 conversion will fail.
    echo.
    pause
    goto :LAUNCH
)

echo [INFO] Extracting FFmpeg binaries...
powershell -Command "Expand-Archive -Path 'ffmpeg.zip' -DestinationPath 'temp_ffmpeg' -Force"

:: Move core binary executables to the current directory
xcopy "temp_ffmpeg\ffmpeg-6.0-essentials_build\bin\ffmpeg.exe" "." /y >nul 2>&1
xcopy "temp_ffmpeg\ffmpeg-6.0-essentials_build\bin\ffprobe.exe" "." /y >nul 2>&1

:: Clean up temporary ZIP and extraction directory
del ffmpeg.zip >nul 2>&1
rmdir /s /q temp_ffmpeg >nul 2>&1

echo [INFO] Portable FFmpeg successfully configured!
echo.

:FFMPEG_OK
echo [INFO] All system requirements resolved.
echo.

:LAUNCH
:: 4. Verify and execute Python application
if not exist "main.py" goto :MAIN_NOT_FOUND

echo [INFO] Launching Youdownneb App...
start "" pythonw main.py
goto :EOF

:PYTHON_NOT_FOUND
echo [ERROR] Python is not installed or not added to your system environment variables.
echo Please install Python 3.x from https://www.python.org/ and check
echo the box to "Add Python to PATH" during installation.
echo.
pause
exit /b

:MAIN_NOT_FOUND
echo [ERROR] main.py was not found in this folder.
echo Please ensure main.py is placed in the same directory as this batch file.
echo.
pause
exit /b

:EOF