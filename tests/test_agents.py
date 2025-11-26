"""
Unit tests for multi-agent system
"""

import pytest
from src.agents.base_agent import DocumentAnalyzerAgent, CardiologyAgent


def test_document_analyzer_init():
    """Test document analyzer initialization"""
    agent = DocumentAnalyzerAgent()
    assert agent.name == "Document Analyzer"
    assert agent.role == "Medical Record Analyst"


def test_cardiology_agent_init():
    """Test cardiology agent initialization"""
    agent = CardiologyAgent()
    assert agent.specialty == "Cardiology"
    assert "cardiology" in agent.name.lower()


def test_system_prompt():
    """Test system prompt generation"""
    agent = DocumentAnalyzerAgent()
    prompt = agent.get_system_prompt()
    assert len(prompt) > 0
    assert "medical" in prompt.lower()


if __name__ == "__main__":
    pytest.main([__file__, '-v'])
