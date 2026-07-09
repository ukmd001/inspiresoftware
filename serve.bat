@echo off
REM Serve the Inspire Arts Software site locally for preview.
cd /d "%~dp0"
echo Inspire Arts Software - serving on http://localhost:8750
echo Press Ctrl+C to stop.
start "" http://localhost:8750
python -m http.server 8750
