# config_handler.py
import json
import os
from dotenv import load_dotenv

def load_config(config_path="config.json"):
    """Load configuration from a JSON file and environment variables."""
    load_dotenv()  # Load environment variables from .env file
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        raise RuntimeError("Error loading configuration file.")

    # Inject API keys from environment variables
    for model_name, model_data in config.get("models", {}).items():
        env_key = f"{model_name.upper()}_API_KEY"
        model_data["api_key"] = os.getenv(env_key, "")
    
    return config
