@echo off
setlocal enabledelayedexpansion

REM Set title for the console window
title Image to PNG Converter

echo ===================================
echo    Image to PNG Converter Tool
echo ===================================
echo.

REM Check if Python is installed
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in the PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Check if Pillow is installed
python -c "import PIL" > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Pillow library...
    python -m pip install Pillow
    if %errorlevel% neq 0 (
        echo Error: Failed to install Pillow. Please run 'pip install Pillow' manually.
        pause
        exit /b 1
    )
    echo Pillow installed successfully.
    echo.
)

REM Check if pillow-avif-plugin is installed (for AVIF support)
python -c "from pillow_avif import AvifImagePlugin" > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing pillow-avif-plugin for AVIF support...
    python -m pip install pillow-avif-plugin
    if %errorlevel% neq 0 (
        echo Warning: Failed to install pillow-avif-plugin. AVIF files may not be supported.
        echo You can install it manually with 'pip install pillow-avif-plugin'
    ) else (
        echo pillow-avif-plugin installed successfully.
    )
    echo.
)

REM Prompt user for input directory
set /p "INPUT_DIR=Enter the path to your images folder: "

REM Check if the directory exists
if not exist "%INPUT_DIR%" (
    echo Error: The directory does not exist. Please enter a valid path.
    pause
    exit /b 1
)

REM Ask for output directory (optional)
echo.
echo Enter the path for converted images (leave blank to use the same folder):
set /p "OUTPUT_DIR="

REM Ask if user wants to process subdirectories
echo.
set /p "RECURSIVE=Process subdirectories? (y/n): "

REM Prepare command
set "CMD=python image_converter.py "%INPUT_DIR%""

REM Add output directory if provided
if not "%OUTPUT_DIR%"=="" (
    if not exist "%OUTPUT_DIR%" (
        echo Creating output directory: %OUTPUT_DIR%
        mkdir "%OUTPUT_DIR%"
    )
    set "CMD=!CMD! -o "%OUTPUT_DIR%""
)

REM Add recursive flag if selected
if /i "%RECURSIVE%"=="y" (
    set "CMD=!CMD! -r"
)

echo.
echo Running command: !CMD!
echo.

REM Execute the command
%CMD%

echo.
echo Conversion completed!
pause