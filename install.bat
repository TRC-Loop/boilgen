@echo off
echo 🚀 Installing Boilgen...

set INSTALL_DIR=%USERPROFILE%\.boilgen
set BIN_DIR=%USERPROFILE%\AppData\Local\bin
set REPO_URL=https://github.com/TRC-Loop/boilgen.git

:: Check for Git
where git >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo ❌ Git is not installed. Install it first!
    exit /b 1
)

:: Check for Python
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo ❌ Python is not installed. Install it first!
    exit /b 1
)

:: Clone or update repository
if exist "%INSTALL_DIR%" (
    echo 🔄 Updating existing Boilgen installation...
    cd /d "%INSTALL_DIR%" && git pull
) else (
    echo 📥 Downloading Boilgen...
    git clone "%REPO_URL%" "%INSTALL_DIR%"
)

:: Ensure BIN_DIR exists
if not exist "%BIN_DIR%" mkdir "%BIN_DIR%"

:: Create a batch wrapper
(
echo @echo off
echo python "%INSTALL_DIR%\src\boilgen.py" %%*
) > "%BIN_DIR%\boilgen.bat"

:: Add to PATH if not already there
setx PATH "%BIN_DIR%;%PATH%" /M

echo 🎉 Installation complete! Restart your terminal and run 'boilgen help' to get started.
