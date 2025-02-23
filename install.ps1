Write-Host "🚀 Installing Boilgen..." -ForegroundColor Green

$INSTALL_DIR = "$env:USERPROFILE\.boilgen"
$BIN_DIR = "$env:USERPROFILE\AppData\Local\bin"
$REPO_URL = "https://github.com/TRC-Loop/boilgen.git"

# Check for Git
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git is not installed. Install it first!" -ForegroundColor Red
    exit 1
}

# Check for Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python is not installed. Install it first!" -ForegroundColor Red
    exit 1
}

# Clone or update repository
if (Test-Path $INSTALL_DIR) {
    Write-Host "🔄 Updating existing Boilgen installation..."
    Set-Location $INSTALL_DIR
    git pull
} else {
    Write-Host "📥 Downloading Boilgen..."
    git clone $REPO_URL $INSTALL_DIR
}

# Ensure BIN_DIR exists
if (!(Test-Path $BIN_DIR)) {
    New-Item -ItemType Directory -Path $BIN_DIR | Out-Null
}

# Create a batch wrapper
$boilgen_cmd = "@echo off`npython `"$INSTALL_DIR\src\boilgen.py`" %*"
Set-Content "$BIN_DIR\boilgen.bat" $boilgen_cmd

# Add to PATH
$path = [System.Environment]::GetEnvironmentVariable("Path", "User")
if ($path -notlike "*$BIN_DIR*") {
    [System.Environment]::SetEnvironmentVariable("Path", "$BIN_DIR;$path", "User")
    Write-Host "✅ Added Boilgen to PATH. Restart your terminal to apply changes." -ForegroundColor Yellow
}

Write-Host "🎉 Installation complete! Run 'boilgen help' to get started." -ForegroundColor Green
