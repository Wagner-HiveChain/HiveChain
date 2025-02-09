# api_caller.py
"""
Module: api_caller.py
Responsibility:
  - Abstract the API call logic so that the rest of the pipeline remains agnostic
    to the underlying API details.
  - Retrieve model configuration from the global configuration.
  - Securely set up API keys and endpoints based on the model type.
  - Clamp parameters (e.g., temperature, max_tokens) using configuration limits.
  - Execute a one-shot call (or chat session call) using the structured prompt.
  
TODO:
  - Enhance error handling and support for additional model types as needed.
  - Adapt the API call to any future changes in the underlying API interface.
"""

import os
import openai
from hivechain.hivechain_core import get_config

def call_api(structured_prompt: dict, model_name: str, temperature: float = None, max_tokens: int = None) -> dict:
    """
    Given a structured prompt and model configuration, perform the API call.
    
    Args:
        structured_prompt (dict): The dictionary with at least a "prompt" key.
        model_name (str): The name of the model to use (must be present in the configuration).
        temperature (float, optional): Override the default temperature.
        max_tokens (int, optional): Override the default max tokens.
        
    Returns:
        dict: The raw API response as returned by the backend service.
    """
    config = get_config()
    model_cfg = config["models"].get(model_name)
    if model_cfg is None:
        raise ValueError(f"Model '{model_name}' is not defined in the configuration.")
    
    # Set temperature and max_tokens, using model defaults if not provided.
    temperature = temperature if temperature is not None else model_cfg.get("default_temperature", 0.7)
    max_tokens  = max_tokens  if max_tokens  is not None else model_cfg.get("default_max_tokens", 1000)
    
    # Validate and clamp parameters using the limits defined in the configuration.
    limits = config.get("parameter_limits", {})
    if "temperature" in limits:
        minT = limits["temperature"].get("min", 0.0)
        maxT = limits["temperature"].get("max", 1.0)
        if temperature < minT or temperature > maxT:
            print(f"Clamping temperature to [{minT}, {maxT}]")
            temperature = max(min(temperature, maxT), minT)
    if "max_tokens" in limits:
        minN = limits["max_tokens"].get("min", 1)
        maxN = limits["max_tokens"].get("max", 2048)
        if max_tokens < minN or max_tokens > maxN:
            print(f"Clamping max_tokens to [{minN}, {maxN}]")
            max_tokens = max(min(max_tokens, maxN), minN)
    
    # Set up API keys and endpoints based on the model type.
    if model_cfg["type"] == "openai":
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_base = "https://api.openai.com/v1"
    elif model_cfg["type"] == "deepseek":
        openai.api_key = os.getenv("DEEPSEEK_API_KEY")
        openai.api_base = model_cfg.get("api_base", "https://api.deepseek.com")
    else:
        raise NotImplementedError(f"Model type '{model_cfg['type']}' is not supported.")
    
    # Build the request payload.
    # Here, we assume the structured prompt has a key "prompt" that contains the text.
    messages = [{"role": "user", "content": structured_prompt["prompt"]}]
    
    # Call the API using the new OpenAI client interface.
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model=model_cfg["engine"],  # e.g., "gpt-4o"
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    # Extract the generated text (if needed).
    generated_text = response.choices[0].message.content
    # You can choose to return the full response or just the generated text.
    return response

# For local testing, you can uncomment the block below:
# if __name__ == "__main__":
#     # Simulate a structured prompt from the input formatter.
#     test_prompt = {"prompt": "Tell me a joke about programming.", "fallback": False, "details": "Standard formatting applied."}
#     try:
#         result = call_api(test_prompt, model_name="openai")
#         print(result)
#     except Exception as e:
#         print("Error during API call:", e)
