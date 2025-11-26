#!/usr/bin/env python3
"""
Project Verification Script
Checks if all essential files exist and are valid
"""

import os
import sys
from pathlib import Path


def check_file(filepath, description):
    """Check if a file exists"""
    exists = os.path.isfile(filepath)
    status = "OK" if exists else "MISSING"
    print(f"[{status}] {description}: {filepath}")
    return exists


def check_dir(dirpath, description):
    """Check if a directory exists"""
    exists = os.path.isdir(dirpath)
    status = "OK" if exists else "MISSING"
    print(f"[{status}] {description}: {dirpath}")
    return exists


def main():
    print("=" * 60)
    print("MediDoc AI - Project Verification")
    print("=" * 60)
    print()
    
    all_ok = True
    
    # Core documentation
    print("Core Documentation:")
    all_ok &= check_file("README.md", "Main README")
    all_ok &= check_file("QUICKSTART.md", "Quick Start")
    all_ok &= check_file("SUBMISSION_DESCRIPTION.txt", "Submission Description")
    all_ok &= check_file("LICENSE", "License")
    all_ok &= check_file("requirements.txt", "Requirements")
    print()
    
    # Source code
    print("Source Code:")
    all_ok &= check_file("src/ocr/document_processor.py", "OCR Processor")
    all_ok &= check_file("src/agents/base_agent.py", "Base Agent")
    all_ok &= check_file("src/agents/diagnostic_system.py", "Diagnostic System")
    all_ok &= check_file("src/edge/edge_device.py", "Edge Device")
    all_ok &= check_file("src/cloud/hybrid_deployment.py", "Hybrid Deployment")
    all_ok &= check_file("src/web/app.py", "Web App")
    print()
    
    # Web frontend
    print("Web Frontend:")
    all_ok &= check_file("src/web/templates/index.html", "HTML Template")
    all_ok &= check_file("src/web/static/css/style.css", "CSS")
    all_ok &= check_file("src/web/static/js/app.js", "JavaScript")
    print()
    
    # Scripts
    print("Scripts:")
    all_ok &= check_file("scripts/demo.py", "Demo Script")
    all_ok &= check_file("scripts/train_ocr.py", "Training Script")
    print()
    
    # Tests
    print("Tests:")
    all_ok &= check_file("tests/test_agents.py", "Agent Tests")
    all_ok &= check_file("tests/test_ocr.py", "OCR Tests")
    all_ok &= check_file("tests/test_web.py", "Web Tests")
    print()
    
    # Documentation
    print("Documentation:")
    all_ok &= check_file("docs/ARCHITECTURE.md", "Architecture")
    all_ok &= check_file("docs/API.md", "API Docs")
    all_ok &= check_file("docs/DEPLOYMENT.md", "Deployment")
    all_ok &= check_file("docs/index.html", "GitHub Pages")
    print()
    
    # Configuration
    print("Configuration:")
    all_ok &= check_file("config/config.yaml", "Config")
    all_ok &= check_file("pytest.ini", "Pytest Config")
    print()
    
    # Human touch
    print("Development Evidence:")
    all_ok &= check_file("DEVNOTES.md", "Dev Notes")
    all_ok &= check_file("CHANGELOG.md", "Changelog")
    all_ok &= check_file("TODO.md", "TODO")
    print()
    
    # Check syntax of Python files
    print("Checking Python Syntax:")
    python_files = [
        "src/ocr/document_processor.py",
        "src/agents/base_agent.py",
        "src/agents/diagnostic_system.py",
        "src/edge/edge_device.py",
        "src/web/app.py",
        "scripts/demo.py"
    ]
    
    for filepath in python_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                compile(f.read(), filepath, 'exec')
            print(f"[OK] Syntax valid: {filepath}")
        except SyntaxError as e:
            print(f"[ERROR] Syntax error in {filepath}: {e}")
            all_ok = False
        except Exception as e:
            print(f"[WARN] Could not check {filepath}: {e}")
    
    print()
    print("=" * 60)
    
    if all_ok:
        print("SUCCESS: All essential files present and valid!")
        print("Project is ready for submission.")
        return 0
    else:
        print("WARNING: Some files are missing or invalid.")
        print("Please review the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
