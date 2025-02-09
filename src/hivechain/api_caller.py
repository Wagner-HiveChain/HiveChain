# api_caller.py
"""
Module: api_caller.py
Responsibility:
  - Abstract the API call logic so that the rest of the pipeline remains agnostic
    to the underlying API details.
  - Retrieve model configuration from the global configuration.
  - Securely set up API keys and endpoints based on the model type.
  - Clamp parameters (e.g., temperature, max_tokens) using configuration limits.
  - Delegate the API call to the appropriate provider adapter.
  
TODO:
  - Enhance error handling and support for additional model types as needed. #Placeholder
  - Adapt the API call to any future changes in the underlying API interface. #Placeholder
"""

import os
from hivechain.hivechain_core import get_config

def call_api(structured_prompt: dict, model_name: str, temperature: float = None, max_tokens: int = None) -> dict:
    """
    Given a structured prompt and model configuration, delegate the API call to the appropriate provider adapter.
    
    Args:
        structured_prompt (dict): The dictionary with at least a "prompt" key.
        model_name (str): The name of the model to use (must be present in the configuration under the default provider).
        temperature (float, optional): Override the default temperature.
        max_tokens (int, optional): Override the default max tokens.
        
    Returns:
        dict: The raw API response as returned by the provider adapter.
    """
    # Retrieve the global configuration.
    config = get_config()
    
    # Determine the default provider (e.g., "openai") from the configuration.
    provider_name = config.get("default_provider", "openai")
    provider_cfg = config["providers"].get(provider_name)
    if provider_cfg is None:
        raise ValueError(f"Provider '{provider_name}' is not configured in the configuration.")
    
    # Retrieve the model configuration from the provider's models.
    model_cfg = provider_cfg["models"].get(model_name)
    if model_cfg is None:
        raise ValueError(f"Model '{model_name}' is not defined under provider '{provider_name}'.")
    
    # Set temperature and max_tokens using defaults if not provided.
    temperature = temperature if temperature is not None else model_cfg.get("default_temperature", 0.7)
    max_tokens  = max_tokens if max_tokens is not None else model_cfg.get("default_max_tokens", 1000)
    
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
    
    # Set up API keys and endpoints based on provider type.
    if model_cfg["type"] == "openai":
        import openai
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_base = "https://api.openai.com/v1"
    elif model_cfg["type"] == "deepseek":
        import openai
        openai.api_key = os.getenv("DEEPSEEK_API_KEY")
        openai.api_base = model_cfg.get("api_base", "https://api.deepseek.com")
    else:
        raise NotImplementedError(f"Model type '{model_cfg['type']}' is not supported in the adapter layer.")
    
    # Build the request payload.
    # Assumes structured_prompt contains a key "prompt" with the text.
    messages = [{"role": "user", "content": structured_prompt["prompt"]}]
    
    # Delegate the API call to the appropriate provider adapter.
    # For this version, we assume the default provider is "openai" or "deepseek".
    if model_cfg["type"] == "openai":
        from hivechain.provider_adapters.openai_provider import generate_text as provider_generate
    elif model_cfg["type"] == "deepseek":
        from hivechain.provider_adapters.deepseek_provider import generate_text as provider_generate
    else:
        raise NotImplementedError(f"Provider adapter for model type '{model_cfg['type']}' is not implemented.")
    
    response = provider_generate(structured_prompt["prompt"], {
        "engine": model_cfg["engine"],
        "temperature": temperature,
        "max_tokens": max_tokens,
        **({"api_base": model_cfg.get("api_base")} if model_cfg["type"] == "deepseek" else {})
    })
    
    # Placeholder: Additional error handling can be added here if needed. #Placeholder
    
    return response

# For local testing, you can uncomment the block below:
# if __name__ == "__main__":
#     # Simulate a structured prompt from the input formatter.
#     test_prompt = {"prompt": "Tell me a joke about programming.", "fallback": False, "details": "Standard formatting applied."}
#     try:
#         result = call_api(test_prompt, model_name="gpt-4o-mini")
#         print(result)
#     except Exception as e:
#         print("Error during API call:", e)
