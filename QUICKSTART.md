# Quick Start Guide

Get MediDoc AI running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- 8GB RAM minimum
- Internet connection (for cloud features)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/medidoc-ai.git
cd medidoc-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit with your API keys
nano .env  # or use any text editor
```

Add your API keys:
```
ERNIE_API_KEY=your_key_here
BAIDU_API_KEY=your_key_here
```

### 4. Run the Demo

```bash
python scripts/demo.py
```

This will showcase all three main scenarios:
- Emergency fast registration
- Multi-disciplinary consultation
- Remote rural healthcare (offline mode)

## Running the Web Service

```bash
python src/web/app.py
```

Visit: http://localhost:5000

## Running Tests

```bash
pytest tests/ -v
```

## Edge Device Setup

For RDK X5 deployment:

```bash
# Run setup script
bash scripts/setup.sh

# Start edge service
python src/edge/edge_device.py
```

## Common Issues

### Issue: PaddleOCR not found
**Solution:** Install PaddleOCR separately
```bash
pip install paddlepaddle paddleocr
```

### Issue: ERNIE API authentication failed
**Solution:** Check your API keys in `.env` file

### Issue: Out of memory on edge device
**Solution:** Use quantized models (INT8/INT4)

## Next Steps

1. Read the [Architecture Documentation](docs/ARCHITECTURE.md)
2. Check the [API Documentation](docs/API.md)
3. Review [Deployment Guide](docs/DEPLOYMENT.md)
4. Explore the [TODO list](TODO.md) for contribution ideas

## Getting Help

- Open an issue on GitHub
- Check existing documentation in `docs/`
- Review test files for usage examples

---

**Ready to go!** 🚀
