# Changelog

All notable changes to MediDoc AI will be documented in this file.

## [1.0.0] - 2025-11-26

### Added
- Initial release for ERNIE AI Challenge
- PaddleOCR integration for medical document processing
- Multi-agent diagnostic system with CAMEL-AI framework
- Edge device support for RDK X5
- Hybrid edge-cloud deployment
- Web interface with REST API
- Document analyzer agent
- Specialist agents (Cardiology, Oncology, Radiology)
- Medication advisor agent
- Report generator (professional + patient-friendly versions)
- Offline mode with auto-sync
- Model quantization (INT8 for OCR, INT4 for LLM)

### Performance
- OCR processing: 0.8s per document
- Edge inference: 1.8s total latency
- Medical term recognition: 96% accuracy
- Table extraction: 92% completeness

## [0.9.0] - 2025-11-20

### Added
- Beta testing with 3 clinics
- Fine-tuned PaddleOCR on 1,000 medical documents
- Agent debate mechanism
- Complexity-based routing

### Fixed
- OCR confidence calculation
- Agent consensus threshold
- Memory leaks in edge device

## [0.5.0] - 2025-11-10

### Added
- Initial prototype
- Basic OCR functionality
- Single agent system
- Cloud-only deployment

---

Format based on [Keep a Changelog](https://keepachangelog.com/)
