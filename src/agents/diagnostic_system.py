from typing import Dict, List, Optional
from loguru import logger
from .base_agent import (
    DocumentAnalyzerAgent,
    CardiologyAgent,
    OncologyAgent,
    RadiologyAgent
)


class MultiAgentDiagnosticSystem:
    
    def __init__(self, config: Dict):
        self.config = config
        
        self.analyzer = DocumentAnalyzerAgent()
        self.specialists = {
            'cardiology': CardiologyAgent(),
            'oncology': OncologyAgent(),
            'radiology': RadiologyAgent()
        }
        
        self.enable_debate = config.get('enable_debate', True)
        self.max_debate_rounds = config.get('max_debate_rounds', 3)
        self.consensus_threshold = config.get('consensus_threshold', 0.85)
        
        logger.info("Multi-Agent Diagnostic System initialized")
    
    def diagnose(self, document: Dict) -> Dict:
        logger.info("Starting multi-agent diagnosis")
        
        logger.info("Step 1: Document analysis")
        structured_data = self.analyzer.analyze(document)
        
        logger.info("Step 2: Determining required specialties")
        required_specialties = self._determine_specialties(structured_data)
        logger.info(f"Required specialties: {required_specialties}")
        
        logger.info("Step 3: Specialist consultation")
        specialist_opinions = {}
        for specialty in required_specialties:
            if specialty in self.specialists:
                agent = self.specialists[specialty]
                opinion = agent.analyze(structured_data)
                specialist_opinions[specialty] = opinion
                logger.debug(f"{specialty} analysis complete")
        
        if self.enable_debate and len(specialist_opinions) > 1:
            logger.info("Step 4: Agent debate for consensus")
            consensus = self._debate_and_consensus(specialist_opinions)
        else:
            consensus = self._merge_opinions(specialist_opinions)
        
        logger.info("Step 5: Generating final report")
        final_report = self._generate_report(
            structured_data,
            specialist_opinions,
            consensus
        )
        
        logger.info("Diagnosis complete")
        return final_report
    
    def _determine_specialties(self, structured_data: Dict) -> List[str]:
        specialties = []
        text = str(structured_data).lower()
        
        cardio_keywords = ['heart', 'cardiac', 'chest pain', 'ecg', 'hypertension', 
                          '心脏', '胸痛', '心电图', '高血压']
        if any(keyword in text for keyword in cardio_keywords):
            specialties.append('cardiology')
        
        onco_keywords = ['tumor', 'cancer', 'malignant', 'chemotherapy', 
                        '肿瘤', '癌', '化疗']
        if any(keyword in text for keyword in onco_keywords):
            specialties.append('oncology')
        
        radio_keywords = ['ct', 'mri', 'x-ray', 'imaging', 'scan',
                         '影像', '扫描']
        if any(keyword in text for keyword in radio_keywords):
            specialties.append('radiology')
        
        if not specialties:
            specialties.append('cardiology')
        
        return specialties
    
    def _debate_and_consensus(self, opinions: Dict[str, Dict]) -> Dict:
        """
        CAMEL-AI debate mechanism for reaching consensus
        
        Args:
            opinions: Initial opinions from all specialists
            
        Returns:
            Consensus opinion
        """
        logger.info("Starting agent debate")
        
        for round_num in range(self.max_debate_rounds):
            logger.debug(f"Debate round {round_num + 1}/{self.max_debate_rounds}")
            
            # Check for conflicts
            if not self._has_conflict(opinions):
                logger.info("Consensus reached without debate")
                break
            
            # Each agent revises opinion based on others
            revised_opinions = {}
            for agent_name, agent in self.specialists.items():
                if agent_name in opinions:
                    # Get other agents' opinions
                    other_opinions = {
                        k: v for k, v in opinions.items() 
                        if k != agent_name
                    }
                    
                    # Agent revises its opinion
                    revised = agent.revise(other_opinions)
                    revised_opinions[agent_name] = revised
            
            opinions = revised_opinions
            
            # Check if consensus reached
            if self._reached_consensus(opinions):
                logger.info(f"Consensus reached after {round_num + 1} rounds")
                break
        
        return self._merge_opinions(opinions)
    
    def _has_conflict(self, opinions: Dict[str, Dict]) -> bool:
        """Check if there are conflicting opinions"""
        # Simplified conflict detection
        # In production, would compare diagnoses and recommendations
        return len(opinions) > 1
    
    def _reached_consensus(self, opinions: Dict[str, Dict]) -> bool:
        """Check if agents have reached consensus"""
        # Simplified consensus check
        # In production, would measure opinion similarity
        return False  # Force full debate rounds for demo
    
    def _merge_opinions(self, opinions: Dict[str, Dict]) -> Dict:
        """Merge multiple specialist opinions into consensus"""
        merged = {
            'diagnoses': [],
            'recommendations': [],
            'risk_assessment': {},
            'confidence': 0.0
        }
        
        # Collect all diagnoses and recommendations
        for specialty, opinion in opinions.items():
            if 'diagnoses' in opinion:
                merged['diagnoses'].extend(opinion['diagnoses'])
            if 'recommendations' in opinion:
                merged['recommendations'].extend(opinion['recommendations'])
        
        # Calculate average confidence
        confidences = [op.get('confidence', 0.5) for op in opinions.values()]
        merged['confidence'] = sum(confidences) / len(confidences) if confidences else 0.5
        
        return merged
    
    def _generate_report(self, structured_data: Dict, 
                        specialist_opinions: Dict, 
                        consensus: Dict) -> Dict:
        """Generate final diagnostic report"""
        report = {
            'patient_data': structured_data,
            'specialist_consultations': specialist_opinions,
            'consensus_diagnosis': consensus,
            'report_versions': {
                'professional': self._generate_professional_report(
                    structured_data, specialist_opinions, consensus
                ),
                'patient_friendly': self._generate_patient_report(
                    structured_data, consensus
                )
            },
            'metadata': {
                'num_specialists': len(specialist_opinions),
                'confidence': consensus.get('confidence', 0.0),
                'debate_enabled': self.enable_debate
            }
        }
        
        return report
    
    def _generate_professional_report(self, data: Dict, opinions: Dict, 
                                     consensus: Dict) -> str:
        """Generate professional medical report"""
        report_lines = [
            "# DIAGNOSTIC REPORT (PROFESSIONAL VERSION)",
            "",
            "## Patient Information",
            f"Data: {data.get('patient_info', {})}",
            "",
            "## Specialist Consultations",
        ]
        
        for specialty, opinion in opinions.items():
            report_lines.append(f"\n### {specialty.title()}")
            report_lines.append(opinion.get('summary', 'No summary available'))
        
        report_lines.extend([
            "",
            "## Consensus Diagnosis",
            f"Confidence: {consensus.get('confidence', 0):.1%}",
            "",
            "## Recommendations",
            "- Follow-up in 2 weeks",
            "- Additional tests as needed"
        ])
        
        return '\n'.join(report_lines)
    
    def _generate_patient_report(self, data: Dict, consensus: Dict) -> str:
        """Generate patient-friendly report"""
        report_lines = [
            "# Your Health Report",
            "",
            "## What We Found",
            "Based on your examination, our medical team has reviewed your case.",
            "",
            "## What You Need to Do",
            "1. Follow the prescribed treatment plan",
            "2. Schedule a follow-up appointment",
            "3. Monitor your symptoms",
            "",
            "## Questions?",
            "Please contact your healthcare provider for any concerns."
        ]
        
        return '\n'.join(report_lines)


def main():
    """Test the diagnostic system"""
    config = {
        'enable_debate': True,
        'max_debate_rounds': 3,
        'consensus_threshold': 0.85
    }
    
    system = MultiAgentDiagnosticSystem(config)
    
    # Sample test case
    test_document = {
        'raw_text': '患者男性，65岁，主诉胸闷气短3天...',
        'confidence': 0.96
    }
    
    logger.info("Running test diagnosis")
    result = system.diagnose(test_document)
    logger.info(f"Test complete. Confidence: {result['metadata']['confidence']:.1%}")


if __name__ == "__main__":
    main()
