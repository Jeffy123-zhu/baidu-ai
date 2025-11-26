import os
from typing import Dict, List, Optional
from paddleocr import PaddleOCR
from loguru import logger
import cv2
import numpy as np


class MedicalDocumentProcessor:
    
    def __init__(self, config: Dict):
        self.config = config
        self.ocr = PaddleOCR(
            use_angle_cls=True,
            lang=config.get('lang', 'ch'),
            use_gpu=config.get('use_gpu', True),
            show_log=False
        )
        logger.info("MedicalDocumentProcessor initialized")
    
    def process_pdf(self, pdf_path: str) -> Dict:
        logger.info(f"Processing PDF: {pdf_path}")
        
        images = self._pdf_to_images(pdf_path)
        
        results = {
            'raw_text': '',
            'structured_data': {},
            'tables': [],
            'confidence': 0.0
        }
        
        total_confidence = 0
        text_blocks = []
        
        for idx, image in enumerate(images):
            logger.debug(f"Processing page {idx + 1}/{len(images)}")
            
            ocr_result = self.ocr.ocr(image, cls=True)
            
            if not ocr_result or not ocr_result[0]:
                continue
            
            for line in ocr_result[0]:
                text = line[1][0]
                confidence = line[1][1]
                text_blocks.append(text)
                total_confidence += confidence
        
        results['raw_text'] = '\n'.join(text_blocks)
        results['confidence'] = total_confidence / len(text_blocks) if text_blocks else 0
        results['structured_data'] = self._structure_medical_text(results['raw_text'])
        
        logger.info(f"Processing complete. Confidence: {results['confidence']:.2%}")
        return results
    
    def process_image(self, image_path: str) -> Dict:
        logger.info(f"Processing image: {image_path}")
        
        image = cv2.imread(image_path)
        ocr_result = self.ocr.ocr(image, cls=True)
        
        text_blocks = []
        confidences = []
        
        if ocr_result and ocr_result[0]:
            for line in ocr_result[0]:
                text = line[1][0]
                confidence = line[1][1]
                text_blocks.append(text)
                confidences.append(confidence)
        
        raw_text = '\n'.join(text_blocks)
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0
        
        return {
            'raw_text': raw_text,
            'structured_data': self._structure_medical_text(raw_text),
            'confidence': avg_confidence
        }
    
    def _pdf_to_images(self, pdf_path: str) -> List[np.ndarray]:
        logger.warning("PDF to image conversion not implemented")
        return []
    
    def _structure_medical_text(self, text: str) -> Dict:
        structured = {
            'patient_info': {},
            'chief_complaint': '',
            'medical_history': {},
            'examination_results': {},
            'diagnosis': '',
            'treatment_plan': ''
        }
        
        lines = text.split('\n')
        
        for line in lines:
            line_lower = line.lower()
            
            if '姓名' in line or 'name' in line_lower:
                structured['patient_info']['name'] = self._extract_value(line)
            elif '年龄' in line or 'age' in line_lower:
                structured['patient_info']['age'] = self._extract_value(line)
            elif '性别' in line or 'gender' in line_lower:
                structured['patient_info']['gender'] = self._extract_value(line)
            elif '主诉' in line or 'chief complaint' in line_lower:
                structured['chief_complaint'] = self._extract_value(line)
            elif '诊断' in line or 'diagnosis' in line_lower:
                structured['diagnosis'] = self._extract_value(line)
        
        return structured
    
    def _extract_value(self, line: str) -> str:
        if ':' in line:
            return line.split(':', 1)[1].strip()
        elif '：' in line:
            return line.split('：', 1)[1].strip()
        return line.strip()
    
    def to_markdown(self, processed_data: Dict) -> str:
        md_lines = ["# Medical Record\n"]
        
        structured = processed_data.get('structured_data', {})
        
        if structured.get('patient_info'):
            md_lines.append("## Patient Information\n")
            for key, value in structured['patient_info'].items():
                md_lines.append(f"- **{key.title()}**: {value}")
            md_lines.append("")
        
        if structured.get('chief_complaint'):
            md_lines.append("## Chief Complaint\n")
            md_lines.append(structured['chief_complaint'])
            md_lines.append("")
        
        if structured.get('diagnosis'):
            md_lines.append("## Diagnosis\n")
            md_lines.append(structured['diagnosis'])
            md_lines.append("")
        
        md_lines.append("## Full Document Text\n")
        md_lines.append("```")
        md_lines.append(processed_data.get('raw_text', ''))
        md_lines.append("```")
        
        return '\n'.join(md_lines)


if __name__ == "__main__":
    config = {'lang': 'ch', 'use_gpu': False}
    processor = MedicalDocumentProcessor(config)
    logger.info("Document processor ready")
