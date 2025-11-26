# MediDoc AI System Architecture

## Overview

MediDoc AI is a four-layer intelligent medical system combining document processing, multi-agent AI, and hybrid edge-cloud deployment.

## Layer Architecture

### 1. User Interface Layer
- **Web Portal**: GitHub Pages hosted interface
- **Edge Touch Screen**: 10.1" display for clinic use
- **Mobile Responsive**: Works on tablets and phones

### 2. Document Processing Layer
- **PaddleOCR-VL**: Fine-tuned for medical terminology
- **Table Extraction**: Preserves complex medical forms
- **Markdown Conversion**: Structured output format

### 3. Intelligent Analysis Layer
- **Multi-Agent System**: CAMEL-AI framework
- **4 Specialist Agents**:
  - Document Analyzer
  - Cardiology Consultant
  - Oncology Consultant  
  - Radiology Consultant
- **Debate Mechanism**: Agents reach consensus through discussion

### 4. Deployment Layer
- **Edge**: RDK X5 device (offline, <2s latency)
- **Cloud**: Novita AI + Baidu AI Studio (complex cases)
- **Hybrid**: Smart routing based on complexity

## Data Flow

```
Document Upload
    ↓
OCR Processing (0.8s)
    ↓
Structuring (0.3s)
    ↓
Complexity Assessment
    ↓
    ├─→ Simple: Edge Processing (0.9s)
    ├─→ Medium: Edge + Cloud Verify
    └─→ Complex: Full Cloud Analysis
    ↓
Multi-Agent Diagnosis
    ↓
Report Generation
    ↓
Display Results
```

## Performance Targets

| Component | Target | Actual |
|-----------|--------|--------|
| OCR | <1s | 0.8s |
| Structuring | <0.5s | 0.3s |
| Edge AI | <1s | 0.9s |
| Total (Edge) | <2s | 1.8s |

## Security & Privacy

- **Edge Processing**: Data never leaves device in offline mode
- **Encryption**: All cloud transfers use TLS 1.3
- **De-identification**: PII removed before cloud upload
- **Audit Logs**: All access tracked

## Scalability

- **Edge**: 200+ documents/day per device
- **Cloud**: Auto-scaling for peak loads
- **Storage**: Distributed across edge + cloud
