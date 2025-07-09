#!/bin/bash
# Setup script for background removal

echo "🌱 Setting up background removal for Sun One Organic vegetable images"
echo "================================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "✅ Python 3 found"

# Install required packages
echo "📦 Installing required packages..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Packages installed successfully"
    echo ""
    echo "🚀 Ready to remove backgrounds!"
    echo "Run the script with: python3 remove_backgrounds.py"
    echo ""
    echo "📁 Your processed images will be saved in: images/no_bg/"
else
    echo "❌ Failed to install packages. Please check your Python installation."
    exit 1
fi
