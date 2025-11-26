#!/bin/bash
# MediDoc AI Setup Script

echo "=== MediDoc AI Setup ==="

# Create directories
echo "Creating directories..."
mkdir -p data/train data/val data/test
mkdir -p models/ocr models/llm
mkdir -p logs
mkdir -p uploads
mkdir -p edge_cache

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Copy environment file
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "Please edit .env with your API keys"
fi

# Download sample data (placeholder)
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env with your API keys"
echo "2. Run: python src/web/app.py"
echo "3. Visit: http://localhost:5000"
