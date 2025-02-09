# config_validator.py
"""
Module: config_validator.py
Description:
  Validate the structure and contents of config.json at startup.
  Checks for required keys and proper types, providing clear error messages if any
  requirements are not met.
  
#Placeholder: Consider integrating JSON Schema validation in the future for more robust checks.
"""

def validate_config(config: dict) -> bool:
    """
    Validates the configuration dictionary.
    
    Args:
        config (dict): The configuration dictionary loaded from config.json.
    
    Returns:
        bool: True if the configuration is valid.
    
    Raises:
        ValueError: If any required key is missing or has an incorrect type.
    """
    # Check for required top-level keys.
    required_top_keys = ["default_provider", "providers", "parameter_limits", "features"]
    for key in required_top_keys:
        if key not in config:
            raise ValueError(f"Missing top-level key: '{key}' in configuration.")

    # Validate default_provider is a string.
    if not isinstance(config["default_provider"], str):
        raise ValueError("The 'default_provider' should be a string.")

    # Validate that providers is a dictionary.
    providers = config["providers"]
    if not isinstance(providers, dict):
        raise ValueError("The 'providers' key should be an object (dict).")

    # Check each provider.
    for provider_name, provider_conf in providers.items():
        if not isinstance(provider_conf, dict):
            raise ValueError(f"Provider '{provider_name}' should be a dict.")
        if "api_key_env" not in provider_conf:
            raise ValueError(f"Provider '{provider_name}' missing 'api_key_env'.")
        if "models" not in provider_conf:
            raise ValueError(f"Provider '{provider_name}' missing 'models' key.")
        models = provider_conf["models"]
        if not isinstance(models, dict):
            raise ValueError(f"'models' under provider '{provider_name}' should be a dict.")
        for model_name, model_conf in models.items():
            # Check required keys for each model.
            required_model_keys = ["engine", "type", "default_temperature", "max_token_input", "max_token_output", "per_token"]
            for key in required_model_keys:
                if key not in model_conf:
                    raise ValueError(f"Model '{model_name}' under provider '{provider_name}' is missing key: '{key}'.")
            # Validate that per_token is a dictionary.
            per_token = model_conf["per_token"]
            if not isinstance(per_token, dict):
                raise ValueError(f"'per_token' for model '{model_name}' under provider '{provider_name}' should be a dict.")
            for token_key in ["input", "cached_input", "output"]:
                if token_key not in per_token:
                    raise ValueError(f"'per_token' for model '{model_name}' missing key '{token_key}'.")

    # Validate parameter_limits.
    parameter_limits = config["parameter_limits"]
    if not isinstance(parameter_limits, dict):
        raise ValueError("'parameter_limits' should be a dict.")
    for param in ["temperature", "max_tokens"]:
        if param not in parameter_limits:
            raise ValueError(f"Missing '{param}' in 'parameter_limits'.")
        limits = parameter_limits[param]
        if not isinstance(limits, dict):
            raise ValueError(f"'{param}' in 'parameter_limits' should be a dict.")
        for bound in ["min", "max"]:
            if bound not in limits:
                raise ValueError(f"'{param}' in 'parameter_limits' is missing '{bound}'.")

    # Validate features.
    features = config["features"]
    if not isinstance(features, dict):
        raise ValueError("'features' should be a dict.")
    for feature in ["use_memory", "use_retrieval"]:
        if feature not in features:
            raise ValueError(f"Missing feature flag: '{feature}' in 'features'.")

    return True

# For local testing: Run this module directly to validate config.json.
if __name__ == "__main__":
    import json
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config_data = json.load(f)
        if validate_config(config_data):
            print("Configuration is valid.")
    except Exception as e:
        print("Configuration validation error:", e)
