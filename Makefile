# MediDoc AI Makefile
# Common development tasks

.PHONY: help install test demo clean run-web run-edge lint format

help:
	@echo "MediDoc AI - Available Commands"
	@echo "================================"
	@echo "make install    - Install dependencies"
	@echo "make test       - Run tests"
	@echo "make demo       - Run demo scenarios"
	@echo "make run-web    - Start web service"
	@echo "make run-edge   - Start edge device"
	@echo "make lint       - Run code linting"
	@echo "make format     - Format code"
	@echo "make clean      - Clean temporary files"

install:
	pip install -r requirements.txt
	@echo "✓ Dependencies installed"

test:
	pytest tests/ -v --cov=src
	@echo "✓ Tests complete"

demo:
	python scripts/demo.py

run-web:
	python src/web/app.py

run-edge:
	python src/edge/edge_device.py

lint:
	flake8 src/ tests/
	@echo "✓ Linting complete"

format:
	black src/ tests/
	isort src/ tests/
	@echo "✓ Code formatted"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov
	@echo "✓ Cleaned temporary files"

setup:
	bash scripts/setup.sh
	@echo "✓ Setup complete"
