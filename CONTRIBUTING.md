# Contributing to MediDoc AI

Thanks for your interest in contributing! This project was developed for the ERNIE AI Challenge, but we welcome improvements and suggestions.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/medidoc-ai.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Run tests: `pytest tests/`
6. Commit: `git commit -m "Add: your feature description"`
7. Push: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small

## Testing

Please add tests for new features:

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_agents.py -v

# Check coverage
pytest --cov=src tests/
```

## Areas for Contribution

- [ ] Improve OCR accuracy for handwritten text
- [ ] Add more specialist agent types
- [ ] Enhance web UI/UX
- [ ] Optimize edge device performance
- [ ] Add more language support
- [ ] Improve documentation

## Questions?

Open an issue or reach out to the maintainers.

---

*Note: This is a competition project. Major architectural changes should be discussed first.*
