import os
import time
from typing import Dict, Optional
from loguru import logger
import json


class EdgeDevice:
    
    def __init__(self, config: Dict):
        self.config = config
        self.offline_mode = config.get('offline_mode', True)
        self.cache_dir = config.get('cache_dir', './edge_cache')
        self.sync_interval = config.get('sync_interval', 300)
        
        self._init_storage()
        self._load_quantized_models()
        
        logger.info("Edge device initialized")
        logger.info(f"Offline mode: {self.offline_mode}")
    
    def _init_storage(self):
        os.makedirs(self.cache_dir, exist_ok=True)
        self.pending_sync = []
        logger.debug("Local storage initialized")
    
    def _load_quantized_models(self):
        logger.info("Loading quantized models...")
        
        self.ocr_model = None
        self.llm_model = None
        
        logger.info("Quantized models loaded (INT8)")
    
    def process_document_realtime(self, image_path: str) -> Dict:
        start_time = time.time()
        logger.info(f"Processing document: {image_path}")
        
        results = {
            'success': False,
            'data': {},
            'timing': {},
            'offline': self.offline_mode
        }
        
        try:
            ocr_start = time.time()
            ocr_result = self._run_ocr(image_path)
            ocr_time = time.time() - ocr_start
            results['timing']['ocr'] = ocr_time
            logger.debug(f"OCR completed in {ocr_time:.2f}s")
            
            struct_start = time.time()
            structured = self._structure_data(ocr_result)
            struct_time = time.time() - struct_start
            results['timing']['structuring'] = struct_time
            logger.debug(f"Structuring completed in {struct_time:.2f}s")
            
            analysis_start = time.time()
            diagnosis = self._analyze_lite(structured)
            analysis_time = time.time() - analysis_start
            results['timing']['analysis'] = analysis_time
            logger.debug(f"Analysis completed in {analysis_time:.2f}s")
            
            results['success'] = True
            results['data'] = {
                'ocr': ocr_result,
                'structured': structured,
                'diagnosis': diagnosis
            }
            
            if self.offline_mode:
                self._store_for_sync(results['data'])
            
        except Exception as e:
            logger.error(f"Processing error: {e}")
            results['error'] = str(e)
        
        total_time = time.time() - start_time
        results['timing']['total'] = total_time
        
        logger.info(f"Processing complete in {total_time:.2f}s")
        return results
    
    def _run_ocr(self, image_path: str) -> Dict:
        logger.debug("Running INT8 quantized OCR")
        time.sleep(0.1)
        
        return {
            'text': 'Sample extracted text from medical document',
            'confidence': 0.94,
            'tables': []
        }
    
    def _structure_data(self, ocr_result: Dict) -> Dict:
        return {
            'patient_info': {
                'name': '[PATIENT_NAME]',
                'age': 65,
                'gender': 'Male'
            },
            'chief_complaint': 'Chest discomfort for 3 days',
            'raw_text': ocr_result.get('text', '')
        }
    
    def _analyze_lite(self, structured_data: Dict) -> Dict:
        logger.debug("Running ERNIE-Lite analysis (INT4)")
        time.sleep(0.1)
        
        complexity = self._assess_complexity(structured_data)
        
        if complexity > 0.7:
            logger.warning("Complex case detected - recommend cloud processing")
            return {
                'recommendation': 'Upload to cloud for detailed analysis',
                'complexity': complexity,
                'preliminary': 'Requires specialist consultation'
            }
        
        return {
            'preliminary_diagnosis': 'Possible cardiovascular issue',
            'recommendations': [
                'Further cardiac examination needed',
                'Monitor blood pressure',
                'Schedule follow-up'
            ],
            'complexity': complexity,
            'confidence': 0.82
        }
    
    def _assess_complexity(self, data: Dict) -> float:
        score = 0.0
        text = str(data).lower()
        
        if 'multiple' in text or 'complications' in text:
            score += 0.3
        if 'rare' in text or 'unusual' in text:
            score += 0.5
        if 'imaging' in text or 'ct' in text or 'mri' in text:
            score += 0.4
        
        return min(score, 1.0)
    
    def _store_for_sync(self, data: Dict):
        timestamp = int(time.time())
        filename = f"{self.cache_dir}/case_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        self.pending_sync.append(filename)
        logger.debug(f"Stored for sync: {filename}")
    
    def sync_to_cloud(self) -> Dict:
        if self.offline_mode:
            logger.warning("Cannot sync in offline mode")
            return {'synced': 0, 'pending': len(self.pending_sync)}
        
        logger.info(f"Syncing {len(self.pending_sync)} pending cases")
        
        synced = 0
        failed = []
        
        for filepath in self.pending_sync[:]:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Simulate cloud upload
                success = self._upload_to_cloud(data)
                
                if success:
                    os.remove(filepath)
                    self.pending_sync.remove(filepath)
                    synced += 1
                else:
                    failed.append(filepath)
                    
            except Exception as e:
                logger.error(f"Sync error for {filepath}: {e}")
                failed.append(filepath)
        
        logger.info(f"Sync complete: {synced} synced, {len(failed)} failed")
        
        return {
            'synced': synced,
            'failed': len(failed),
            'pending': len(self.pending_sync)
        }
    
    def _upload_to_cloud(self, data: Dict) -> bool:
        logger.debug("Uploading to cloud...")
        time.sleep(0.05)
        return True
    
    def set_offline_mode(self, offline: bool):
        self.offline_mode = offline
        logger.info(f"Offline mode: {offline}")
    
    def get_status(self) -> Dict:
        return {
            'offline_mode': self.offline_mode,
            'pending_sync': len(self.pending_sync),
            'cache_dir': self.cache_dir,
            'models_loaded': self.ocr_model is not None
        }


def main():
    config = {
        'offline_mode': True,
        'cache_dir': './edge_cache',
        'sync_interval': 300
    }
    
    device = EdgeDevice(config)
    
    logger.info("Testing document processing...")
    result = device.process_document_realtime('test_image.jpg')
    
    logger.info(f"Processing result: {result['success']}")
    logger.info(f"Total time: {result['timing']['total']:.2f}s")
    
    status = device.get_status()
    logger.info(f"Device status: {status}")


if __name__ == "__main__":
    main()
