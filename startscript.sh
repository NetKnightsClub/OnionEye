#!/bin/bash

echo "👁️‍🗨️ Starting OnionEye setup..."


OS=$(awk -F= '/^ID=/{print $2}' /etc/os-release | tr -d '"')
echo "Detected OS: $OS"

if command -v tor >/dev/null 2>&1; then
    echo "Tor is already installed."
else
    echo "Tor is NOT installed."
    if [[ "$OS" == "debian" || "$OS" == "ubuntu" ]]; then
        echo "Installing Tor for Debian/Ubuntu..."
        sudo apt update && sudo apt install -y tor
    elif [[ "$OS" == "arch" || "$OS" == "endeavouros" ]]; then
        echo "Installing Tor for Arch..."
        sudo pacman -Sy --noconfirm tor
    elif [[ "$OS" == "fedora" ]]; then
        echo "Installing Tor for Fedora..."
        sudo dnf install -y tor
    else
        echo "Unsupported OS for automatic Tor install, please install Tor manually."
        exit 1
    fi
fi

if [[ "$OS" == "debian" || "$OS" == "ubuntu" || "$OS" == "arch" || "$OS" == "endeavouros" || "$OS" == "fedora" ]]; then
    if systemctl is-enabled tor >/dev/null 2>&1; then
        echo "Tor service is enabled."
    else
        echo "Enabling Tor service..."
        sudo systemctl enable tor
    fi

    if systemctl is-active tor >/dev/null 2>&1; then
        echo "Tor service is running."
    else
        echo "Starting Tor service..."
        sudo systemctl start tor
    fi
else
    echo "Unsupported OS for automatic Tor service management. Please start Tor manually."
fi

# Check if Tor Browser is installed (default path)
TOR_BROWSER_PATH="$HOME/tor-browser_en-US/Browser/start-tor-browser"
if [ -x "$TOR_BROWSER_PATH" ]; then
    echo "Tor Browser found."
else
    echo "⚠️  Tor Browser not found in $TOR_BROWSER_PATH"
    echo "Please download and install Tor Browser manually from https://torproject.org/"
fi

echo "Setting up Python virtual environment..."

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Running OnionEye..."
python run.py
echo "👁️‍🗨️ OnionEye setup complete!"
