# openai_provider.py
"""
Module: openai_provider.py
Responsibility:
  - Adapter for OpenAI.
  - Implements generate_text(prompt, params) using OpenAI's API.
  - Uses environment variable OPENAI_API_KEY and standard OpenAI endpoint.
  
Keywords: adapter, abstraction, OpenAI.
"""

import os
import openai

def generate_text(prompt: str, params: dict) -> dict:
    """
    Calls the OpenAI API to generate text based on the prompt.
    
    Args:
        prompt (str): The input prompt.
        params (dict): Parameters including:
                       - "engine": model identifier (default "gpt-3.5-turbo")
                       - "temperature": generation temperature (default 0.7)
                       - "max_tokens": maximum tokens (default 1000)
    
    Returns:
        dict: The API response.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_base = "https://api.openai.com/v1"
    
    messages = [{"role": "user", "content": prompt}]
    
    response = openai.OpenAI().chat.completions.create(
        model=params.get("engine", "gpt-3.5-turbo"),
        messages=messages,
        temperature=params.get("temperature", 0.7),
        max_tokens=params.get("max_tokens", 1000)
    )
    
    return response

# For local testing, you might add:
# if __name__ == "__main__":
#     test_params = {"engine": "gpt-3.5-turbo", "temperature": 0.7, "max_tokens": 1000}
#     print(generate_text("Tell me a joke about programming.", test_params))
