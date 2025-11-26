# Deployment Guide

## Edge Device Setup (RDK X5)

### Hardware Requirements
- D-Robotics RDK X5 board
- 8GB RAM minimum
- 64GB storage
- High-resolution document scanner
- 10.1" touchscreen display

### Software Installation

```bash
# 1. Install system dependencies
sudo apt update
sudo apt install python3.8 python3-pip

# 2. Clone repository
git clone https://github.com/yourusername/medidoc-ai.git
cd medidoc-ai

# 3. Install Python packages
pip3 install -r requirements.txt

# 4. Download quantized models
python scripts/download_models.py --device edge

# 5. Configure device
cp config/edge_config.yaml config/config.yaml
nano config/config.yaml  # Edit as needed

# 6. Run edge service
python src/edge/main.py
```

### Model Quantization

```bash
# Convert PaddleOCR to INT8
python scripts/quantize_ocr.py \
    --input models/paddleocr-vl \
    --output models/paddleocr-int8 \
    --format int8

# Convert ERNIE to INT4
python scripts/quantize_llm.py \
    --model ernie-4.5-8b \
    --output models/ernie-lite-int4 \
    --bits 4
```

## Cloud Deployment

### Novita AI Setup

```python
# config/cloud_config.py
NOVITA_CONFIG = {
    'api_key': 'your-api-key',
    'endpoint': 'https://api.novita.ai/v1',
    'model': 'ernie-4.5-72b',
    'timeout': 30
}
```

### Baidu AI Studio

```bash
# Set environment variables
export BAIDU_APP_ID="your-app-id"
export BAIDU_API_KEY="your-api-key"
export BAIDU_SECRET_KEY="your-secret-key"
```

## Web Interface

```bash
# Deploy to GitHub Pages
cd web
npm install
npm run build
git add dist/
git commit -m "Deploy web interface"
git push origin gh-pages
```

## Monitoring

```bash
# Check edge device status
curl http://localhost:5000/api/status

# View logs
tail -f logs/medidoc.log

# Monitor performance
python scripts/monitor.py
```
