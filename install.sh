#!/bin/bash

echo "🚀 Installing Boilgen..."

# Define installation path
INSTALL_DIR="$HOME/.boilgen"
BIN_DIR="$HOME/.local/bin"
REPO_URL="https://github.com/TRC-Loop/boilgen.git"

# Ensure necessary dependencies are installed
command -v git >/dev/null 2>&1 || { echo "❌ Git is not installed. Install it first!"; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "❌ Python3 is not installed. Install it first!"; exit 1; }

# Clone or update repository
if [ -d "$INSTALL_DIR" ]; then
    echo "🔄 Updating existing Boilgen installation..."
    cd "$INSTALL_DIR" && git pull
else
    echo "📥 Downloading Boilgen..."
    git clone "$REPO_URL" "$INSTALL_DIR"
fi

# Create symlink
mkdir -p "$BIN_DIR"
ln -sf "$INSTALL_DIR/src/boilgen.py" "$BIN_DIR/boilgen"
chmod +x "$BIN_DIR/boilgen"

# Add to PATH if needed
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo "export PATH=\"$BIN_DIR:\$PATH\"" >> "$HOME/.bashrc"
    echo "export PATH=\"$BIN_DIR:\$PATH\"" >> "$HOME/.zshrc"
    echo "✅ Added Boilgen to PATH. Restart your terminal or run 'source ~/.bashrc' (or ~/.zshrc) to apply changes."
fi

echo "🎉 Installation complete! You can now run 'boilgen'. Try 'boilgen help' to get started."
