import os
from typing import List, Dict, Any, Optional
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LLMEngine:
    """Handles interaction with LLM providers."""

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model

    async def get_completion(self, prompt: str, system_prompt: str = "You are a cybersecurity expert assistant.") -> str:
        """
        Get a completion from the LLM.
        
        Args:
            prompt: The user prompt.
            system_prompt: The system instruction.
            
        Returns:
            The LLM's response as a string.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
