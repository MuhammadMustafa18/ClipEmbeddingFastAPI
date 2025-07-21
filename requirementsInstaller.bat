@echo off
echo Installing Python dependencies from requirements.txt...
pip install -r requirements.txt

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Installation failed. Please check your Python and pip installation.
) ELSE (
    echo.
    echo ✅ Installation complete.
)

pause
