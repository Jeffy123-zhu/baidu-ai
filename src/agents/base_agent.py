from typing import Dict, List, Optional
from abc import ABC, abstractmethod
import erniebot
from loguru import logger


class BaseAgent(ABC):
    
    def __init__(self, name: str, role: str, model: str = "ernie-4.5-8b"):
        self.name = name
        self.role = role
        self.model = model
        self.conversation_history = []
        logger.info(f"Initialized {name} agent with role: {role}")
    
    @abstractmethod
    def get_system_prompt(self) -> str:
        pass
    
    def analyze(self, data: Dict) -> Dict:
        system_prompt = self.get_system_prompt()
        user_message = self._format_input(data)
        
        try:
            response = erniebot.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.3,
                top_p=0.9
            )
            
            result = response.get_result()
            self.conversation_history.append({
                "input": user_message,
                "output": result
            })
            
            return self._parse_response(result)
            
        except Exception as e:
            logger.error(f"Error in {self.name} analysis: {e}")
            return {"error": str(e)}
    
    def revise(self, other_opinions: Dict[str, Dict]) -> Dict:
        revision_prompt = self._create_revision_prompt(other_opinions)
        
        try:
            response = erniebot.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.get_system_prompt()},
                    {"role": "user", "content": revision_prompt}
                ],
                temperature=0.4
            )
            
            return self._parse_response(response.get_result())
            
        except Exception as e:
            logger.error(f"Error in {self.name} revision: {e}")
            return {}
    
    @abstractmethod
    def _format_input(self, data: Dict) -> str:
        pass
    
    @abstractmethod
    def _parse_response(self, response: str) -> Dict:
        pass
    
    def _create_revision_prompt(self, other_opinions: Dict) -> str:
        prompt = "Based on the following opinions from other specialists:\n\n"
        
        for agent_name, opinion in other_opinions.items():
            prompt += f"**{agent_name}**:\n{opinion.get('summary', '')}\n\n"
        
        prompt += "\nPlease revise your analysis considering these perspectives. "
        prompt += "Maintain your expertise while addressing any conflicts or gaps."
        
        return prompt


class DocumentAnalyzerAgent(BaseAgent):
    
    def __init__(self):
        super().__init__(
            name="Document Analyzer",
            role="Medical Record Analyst"
        )
    
    def get_system_prompt(self) -> str:
        return """You are an experienced medical record analyst. Your task is to extract 
structured information from medical documents including:
1. Patient basic information (age, gender, ID)
2. Chief complaint and present illness history
3. Past medical history
4. Examination results
5. Current medications

Output the information in a clear, structured JSON format."""
    
    def _format_input(self, data: Dict) -> str:
        raw_text = data.get('raw_text', '')
        return f"""Please analyze the following medical record and extract structured information:

{raw_text}

Provide the output in JSON format with keys: patient_info, chief_complaint, 
medical_history, examination_results, current_medications."""
    
    def _parse_response(self, response: str) -> Dict:
        return {
            "summary": response,
            "structured_data": {},
            "confidence": 0.9
        }


class SpecialistAgent(BaseAgent):
    
    def __init__(self, specialty: str, model: str = "ernie-4.5-8b"):
        super().__init__(
            name=f"{specialty} Consultant",
            role=f"{specialty} Specialist",
            model=model
        )
        self.specialty = specialty
    
    def _format_input(self, data: Dict) -> str:
        return f"""Patient case for {self.specialty} consultation:

Patient Information: {data.get('patient_info', {})}
Chief Complaint: {data.get('chief_complaint', '')}
Medical History: {data.get('medical_history', {})}
Examination Results: {data.get('examination_results', {})}

Please provide:
1. Possible diagnoses in your specialty
2. Recommended additional tests
3. Initial treatment suggestions
4. Risk assessment"""
    
    def _parse_response(self, response: str) -> Dict:
        return {
            "specialty": self.specialty,
            "summary": response,
            "diagnoses": [],
            "recommendations": [],
            "risk_level": "medium"
        }


class CardiologyAgent(SpecialistAgent):
    
    def __init__(self):
        super().__init__("Cardiology", model="ernie-cardiology")
    
    def get_system_prompt(self) -> str:
        return """You are a cardiology specialist with expertise in cardiovascular diseases.
Analyze cases for:
- Coronary artery disease
- Heart failure
- Arrhythmias
- Hypertension
- ECG interpretation

Provide evidence-based recommendations following current guidelines."""


class OncologyAgent(SpecialistAgent):
    
    def __init__(self):
        super().__init__("Oncology", model="ernie-oncology")
    
    def get_system_prompt(self) -> str:
        return """You are an oncology specialist with expertise in cancer diagnosis and treatment.
Analyze cases for:
- Tumor staging
- Pathology report interpretation
- Treatment options (surgery, chemo, radiation)
- Prognosis assessment

Provide comprehensive cancer care recommendations."""


class RadiologyAgent(SpecialistAgent):
    
    def __init__(self):
        super().__init__("Radiology", model="ernie-radiology")
    
    def get_system_prompt(self) -> str:
        return """You are a radiology specialist expert in medical imaging interpretation.
Analyze imaging reports for:
- CT/MRI findings
- X-ray abnormalities
- Ultrasound results
- Location and severity of abnormalities

Provide detailed imaging analysis and follow-up recommendations."""


if __name__ == "__main__":
    analyzer = DocumentAnalyzerAgent()
    cardio = CardiologyAgent()
    logger.info("Agents initialized")
