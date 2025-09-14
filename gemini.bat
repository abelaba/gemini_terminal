@echo off
:: Check if first argument is empty
if "%~1"=="" (
    echo Usage: %~nx0 ^<text^>
    echo.
    exit /b 1
)

:: Combine all arguments into one variable
set text=%*

:: Run Python script with arguments
python gemini.py "%text%"

