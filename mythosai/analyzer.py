import logging
from typing import Dict, Any, List
from .llm_engine import LLMEngine
from .threat_db import ThreatDB

class Analyzer:
    """AI-powered threat analyzer."""

    def __init__(self, llm_engine: LLMEngine):
        self.llm = llm_engine
        self.db = ThreatDB()
        self.logger = logging.getLogger(__name__)

    async def analyze_vulnerability(self, description: str) -> Dict[str, Any]:
        """
        Analyze a vulnerability description using AI.
        
        Args:
            description: A text description of the potential vulnerability.
            
        Returns:
            A dictionary containing the analysis results.
        """
        system_prompt = (
            "You are a Senior Cybersecurity Analyst. Analyze the following vulnerability description. "
            "Identify the potential threat type, severity, and provide mitigation steps. "
            "Format your response as a structured analysis."
        )
        
        prompt = f"Vulnerability Description: {description}"
        
        analysis_text = await self.llm.get_completion(prompt, system_prompt)
        
        # In a real app, we might parse the LLM response into a structured dict
        return {
            "description": description,
            "analysis": analysis_text,
            "related_threats": self.db.search_threats(description)
        }

    async def generate_security_report(self, assets: List[str]) -> str:
        """
        Generate a security report for a list of assets.
        
        Args:
            assets: A list of assets (e.g., URLs, server names).
            
        Returns:
            A formatted security report string.
        """
        prompt = f"Generate a high-level security risk assessment for the following assets: {', '.join(assets)}"
        return await self.llm.get_completion(prompt)
