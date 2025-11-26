"""
Unit tests for OCR document processor
"""

import pytest
from src.ocr.document_processor import MedicalDocumentProcessor


def test_processor_initialization():
    """Test processor can be initialized"""
    config = {'lang': 'ch', 'use_gpu': False}
    processor = MedicalDocumentProcessor(config)
    assert processor is not None


def test_structure_medical_text():
    """Test text structuring"""
    config = {'lang': 'ch', 'use_gpu': False}
    processor = MedicalDocumentProcessor(config)
    
    sample_text = """
    姓名: 张三
    年龄: 65
    性别: 男
    主诉: 胸闷气短3天
    """
    
    structured = processor._structure_medical_text(sample_text)
    assert 'patient_info' in structured
    assert 'chief_complaint' in structured


def test_to_markdown():
    """Test markdown conversion"""
    config = {'lang': 'ch', 'use_gpu': False}
    processor = MedicalDocumentProcessor(config)
    
    data = {
        'raw_text': 'Test document',
        'structured_data': {
            'patient_info': {'name': 'Test', 'age': '65'},
            'chief_complaint': 'Test complaint'
        }
    }
    
    markdown = processor.to_markdown(data)
    assert '# Medical Record' in markdown
    assert 'Patient Information' in markdown


if __name__ == "__main__":
    pytest.main([__file__, '-v'])
