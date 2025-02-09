

# File: config.json

{
  "default_provider": "openai",
  "providers": {
    "openai": {
      "api_key_env": "OPENAI_API_KEY",
      "models": {
        "o1": {
          "engine": "o1",
          "type": "openai",
          "default_temperature": 0.7,
          "max_token_input": 200000,
          "max_token_output": 200000,
          "per_token": {
            "input": 0.015,
            "cached_input": 0.0075,
            "output": 0.060
          }
        },
        "o3-mini": {
          "engine": "o3-mini",
          "type": "openai",
          "default_temperature": 0.7,
          "max_token_input": 200000,
          "max_token_output": 200000,
          "per_token": {
            "input": 0.0011,
            "cached_input": 0.00055,
            "output": 0.0044
          }
        },
        "gpt-4o": {
          "engine": "gpt-4o",
          "type": "openai",
          "default_temperature": 0.7,
          "max_token_input": 128000,
          "max_token_output": 128000,
          "per_token": {
            "input": 0.0025,
            "cached_input": 0.00125,
            "output": 0.0100
          }
        },
        "gpt-4o-mini": {
          "engine": "gpt-4o-mini",
          "type": "openai",
          "default_temperature": 0.7,
          "max_token_input": 128000,
          "max_token_output": 128000,
          "per_token": {
            "input": 0.00015,
            "cached_input": 0.000075,
            "output": 0.0006
          }
        },
        "gpt-3.5-turbo": {
          "engine": "gpt-3.5-turbo",
          "type": "openai",
          "default_temperature": 0.7,
          "max_token_input": 4096,
          "max_token_output": 4096,
          "per_token": {
            "input": 0.0015,
            "cached_input": 0.00075,
            "output": 0.0020
          }
        }
      }
    },
    "deepseek": {
      "api_key_env": "DEEPSEEK_API_KEY",
      "models": {
        "deepseek-v3": {
          "engine": "deepseek-v3",
          "type": "deepseek",
          "default_temperature": 0.6,
          "max_token_input": 128000,
          "max_token_output": 128000,
          "per_token": {
            "input": 0.00014,
            "cached_input": 0.00007,
            "output": 0.00219
          }
        },
        "deepseek-r1": {
          "engine": "deepseek-r1",
          "type": "deepseek",
          "default_temperature": 0.6,
          "max_token_input": 64000,
          "max_token_output": 8000,
          "per_token": {
            "input": 0.00027,
            "cached_input": 0.00007,
            "output": 0.00110
          }
        }
      }
    },
    "anthropic": {
      "api_key_env": "ANTHROPIC_API_KEY",
      "models": {
        "claude-3.5-sonnet": {
          "engine": "claude-3.5-sonnet",
          "type": "anthropic",
          "default_temperature": 0.7,
          "max_token_input": 200000,
          "max_token_output": 200000,
          "per_token": {
            "input": 0.0030,
            "cached_input": 0.0003,
            "output": 0.015
          }
        },
        "claude-3.5-haiku": {
          "engine": "claude-3.5-haiku",
          "type": "anthropic",
          "default_temperature": 0.7,
          "max_token_input": 200000,
          "max_token_output": 200000,
          "per_token": {
            "input": 0.0008,
            "cached_input": 0.00008,
            "output": 0.004
          }
        },
        "claude-3-opus": {
          "engine": "claude-3-opus",
          "type": "anthropic",
          "default_temperature": 0.7,
          "max_token_input": 200000,
          "max_token_output": 200000,
          "per_token": {
            "input": 0.00375,
            "cached_input": 0.0003,
            "output": 0.015
          }
        }
      }
    },
    "google": {
      "api_key_env": "GOOGLE_API_KEY",
      "models": {
        "gemini-2.0-flash": {
          "engine": "gemini-2.0-flash",
          "type": "google",
          "default_temperature": 0.7,
          "max_token_input": 128000,
          "max_token_output": 128000,
          "per_token": {
            "input": 0.0025,
            "cached_input": 0.00125,
            "output": 0.01
          }
        }
      }
    },
    "meta": {
      "api_key_env": "none",
      "models": {
        "llama-3.1": {
          "engine": "llama-3.1",
          "type": "meta",
          "default_temperature": 0.7,
          "max_token_input": 128000,
          "max_token_output": 128000,
          "per_token": {
            "input": null,
            "cached_input": null,
            "output": null
          }
        }
      }
    },
    "huggingface": {
      "api_key_env": "none",
      "models": {
        "mistral-7b": {
          "engine": "mistral-7b",
          "type": "huggingface",
          "default_temperature": 0.5,
          "max_token_input": 8192,
          "max_token_output": 8192,
          "per_token": {
            "input": null,
            "cached_input": null,
            "output": null
          }
        }
      }
    },
    "alibaba": {
      "api_key_env": "none",
      "models": {
        "qwen-2.5-max": {
          "engine": "qwen-2.5-max",
          "type": "alibaba",
          "default_temperature": 0.7,
          "max_token_input": 8192,
          "max_token_output": 8192,
          "per_token": {
            "input": null,
            "cached_input": null,
            "output": null
          }
        }
      }
    }
  },
  "parameter_limits": {
    "temperature": {
      "min": 0.0,
      "max": 1.0
    },
    "max_tokens": {
      "min": 1,
      "max": 200000
    }
  },
  "features": {
    "use_memory": true,
    "use_retrieval": false
  }
}


# File: run.py

#!/usr/bin/env python3
# run.py
"""
Module: run.py
Responsibility:
  - Provide an interactive CLI that uses the complete HiveChain pipeline.
  - Force the use of the GPT-4o mini model.
  - Handle user conversation, exit gracefully, and print the standardized output with HiveChain metadata.
"""

import sys
from hivechain.config_handler import load_config
from hivechain.hivechain_core import init_config
from hivechain.pipeline import process_request

def main():
    # Load configuration and initialize the library.
    config = load_config()
    init_config(config)
    
    # Force using the GPT-4o mini model.
    model = "gpt-4o-mini"
    
    print("Welcome to the HiveChain GPT-4o Mini CLI!")
    print("Type your message and press Enter. Type 'exit' or 'quit' to end the conversation.\n")
    
    while True:
        try:
            prompt = input("You: ")
            if prompt.strip().lower() in ["exit", "quit"]:
                print("Exiting conversation.")
                break
            
            # Process the request through the full pipeline with metadata wrapping enabled.
            response = process_request(raw_input=prompt, model_name=model, wrap_response=True)
            
            # Print the standardized output (assuming "result" holds the generated text).
            print("GPT-4o Mini:", response.get("result", ""), "\n")
            if response.get("fallback_used", False):
                print("Warning: Fallback formatting was applied to the input.\n")
        except KeyboardInterrupt:
            print("\nConversation interrupted. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print("Error:", e, file=sys.stderr)

if __name__ == "__main__":
    main()


# File: setup.py

from setuptools import setup, find_packages
import os

# Read the long description from README.md if available
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hivechain",
    version="0.1.0",
    author="Laura Wagner",
    author_email="wagner@hivechain.dev", 
    description="HiveChain: A Modular AI Orchestration Framework for Transparent and easy to use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.hivechain.dev",
    # This will include all packages under src, including hivechain and its submodules (e.g., provider_adapters)
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    install_requires=[
        "openai",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "hivechain-run=hivechain.cli:main",
        ]
    },
)


# File: quick tools\concatenate_code.py

import os

def get_all_files(root_dir, extensions=('.py', '.json')):
    """
    Recursively collects all files ending with the specified extensions from the root_dir,
    excluding hidden directories.
    
    Args:
        root_dir (str): The root directory to search.
        extensions (tuple): File extensions to include.
        
    Returns:
        list: A list of full file paths.
    """
    all_files = []
    for subdir, dirs, files in os.walk(root_dir):
        # Exclude hidden directories (those that start with a dot)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith(extensions):
                all_files.append(os.path.join(subdir, file))
    return all_files

def main():
    # Set the project root to the directory containing this script
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    # Define the output file in the tests directory (create tests if needed)
    output_dir = os.path.join(project_root, "tests")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "combined_code.txt")
    
    # Get all .py and .json files from the project root recursively.
    files = get_all_files(project_root, ('.py', '.json'))
    
    combined_text = ""
    for file_path in files:
        rel_path = os.path.relpath(file_path, project_root)
        combined_text += f"\n\n# File: {rel_path}\n\n"
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                combined_text += f.read()
        except Exception as e:
            combined_text += f"\n# Error reading file: {e}\n"
    
    # Write the combined text to the output file.
    with open(output_file, "w", encoding="utf-8") as out_file:
        out_file.write(combined_text)
    
    print(f"Combined code has been written to:\n{output_file}")

if __name__ == "__main__":
    main()


# File: src\hivechain\agent_manager.py

# agent_manager.py
"""
Module: agent_manager.py
Description:
  Manages smart agents and multi-agent workflows.
  Defines a base Agent interface (e.g., Agent.generate(prompt, context)) and a stub implementation.
  Also provides an AgentManager to register agents and delegate tasks.
  
Key Tasks:
  - Define an Agent interface with an abstract method generate(prompt, context).
  - Provide a SimpleAgent as a stub implementation.
  - Implement an AgentManager to manage multiple agents and aggregate their responses.
  
Keywords: agents, multi-agent, coordination, plugin.

#Placeholder: Extend to support orchestration of multiple agents, task delegation strategies, and result aggregation.
"""

from abc import ABC, abstractmethod

class Agent(ABC):
    """
    Abstract base class for agents.
    Each agent should implement the generate method to produce a response given a prompt and optional context.
    """
    @abstractmethod
    def generate(self, prompt: str, context: dict = None) -> str:
        """
        Generate a response based on the provided prompt and optional context.
        
        Args:
            prompt (str): The input prompt for the agent.
            context (dict, optional): Additional context or memory for the agent.
        
        Returns:
            str: The generated response.
        """
        pass

class SimpleAgent(Agent):
    """
    A simple stub agent implementation.
    Returns a placeholder response indicating that the agent received the prompt.
    
    #Placeholder: Replace this stub with actual agent logic.
    """
    def generate(self, prompt: str, context: dict = None) -> str:
        return f"[Placeholder Response] Received prompt: {prompt}"

class AgentManager:
    """
    Manages multiple agents and orchestrates multi-agent workflows.
    """
    def __init__(self):
        self.agents = []  # List to store registered agents.
    
    def register_agent(self, agent: Agent):
        """
        Registers an agent with the manager.
        
        Args:
            agent (Agent): An instance of a subclass of Agent.
        """
        self.agents.append(agent)
    
    def delegate_task(self, prompt: str, context: dict = None) -> dict:
        """
        Delegates a task to all registered agents and aggregates their responses.
        
        Args:
            prompt (str): The task prompt.
            context (dict, optional): Additional context to pass to each agent.
        
        Returns:
            dict: A dictionary mapping agent identifiers (e.g., "agent_0") to their generated responses.
        
        #Placeholder: Enhance with logic for selecting a subset of agents, parallel execution, or more advanced aggregation.
        """
        responses = {}
        for idx, agent in enumerate(self.agents):
            responses[f"agent_{idx}"] = agent.generate(prompt, context)
        return responses

# For local testing, you can uncomment the block below:
# if __name__ == "__main__":
#     agent_manager = AgentManager()
#     agent_manager.register_agent(SimpleAgent())
#     agent_manager.register_agent(SimpleAgent())
#     result = agent_manager.delegate_task("What is the weather today?", {"location": "San Francisco"})
#     print("Agent responses:", result)


# File: src\hivechain\api_caller.py

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


# File: src\hivechain\cli.py

# cli.py
"""
Module: cli.py
Responsibility:
  - Provide a command-line interface (CLI) for interacting with the HiveChain pipeline.
  - Load configuration, initialize the library, parse user input, call the pipeline,
    and display the final output.
  - This CLI leverages the new modular pipeline approach and allows toggling metadata wrapping.
"""

import argparse
from .config_handler import load_config
from .hivechain_core import init_config
from .pipeline import process_request

def main():
    # Load configuration (from config.json, .env, etc.)
    config = load_config()
    # Initialize the library's configuration (immutable by default)
    init_config(config)
    
    parser = argparse.ArgumentParser(description="HiveChain AI Conversation CLI")
    parser.add_argument("prompt", type=str, help="User prompt for the AI model")
    parser.add_argument("--model", choices=config["models"].keys(),
                        help="Which model to use (as defined in config.json; defaults to config's default)")
    parser.add_argument("--temperature", type=float, help="Temperature for generation")
    parser.add_argument("--max-tokens", type=int, dest="max_tokens", help="Max tokens for the response")
    parser.add_argument("--no-wrap", action="store_true",
                        help="Return raw API response without HiveChain metadata (default wraps response)")
    args = parser.parse_args()

    try:
        # Determine wrap_response: if --no-wrap is provided, disable metadata wrapping.
        wrap_response = not args.no_wrap
        
        # Process the request through the complete pipeline.
        response = process_request(
            raw_input=args.prompt,
            model_name=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            wrap_response=wrap_response
        )
        
        # If the response is wrapped (a dict with a "result" key), print the result and any metadata.
        if isinstance(response, dict) and "result" in response:
            model_used = args.model if args.model else config.get("default_model", "openai")
            print(f"{model_used} response:\n{response.get('result', '')}\n")
            if response.get("fallback_used", False):
                print("Warning: Fallback formatting was applied to the input.")
        else:
            # Otherwise, assume it's the raw API response and print it directly.
            print(response)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


# File: src\hivechain\config_handler.py

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


# File: src\hivechain\config_validator.py

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


# File: src\hivechain\fallback_formatter.py

# fallback_formatter.py
"""
Module: fallback_formatter.py
Responsibility:
  - When raw input fails validation, this module uses a fallback formatting agent 
    (e.g., a cost-effective model like GPT-4o mini) to reformat and sanitize the input.
  - It inserts placeholder tags (e.g., {sanitized:object.type}) where necessary and 
    produces a structured prompt that the downstream API caller can handle.
  - In this stub, we simulate the fallback behavior. In a complete implementation, the
    function would call the formatting agent and process its output.
"""

def sanitize_input(raw_input: str) -> dict:
    """
    Processes raw input using a fallback mechanism to generate a structured prompt.
    
    Args:
        raw_input (str): The raw user input that failed validation.
        
    Returns:
        dict: A dictionary with the following keys:
            - "prompt": The sanitized and formatted prompt ready for the API caller.
            - "fallback": A boolean flag indicating that fallback formatting was applied.
            - "details": (Optional) Additional details on what was sanitized or any tags inserted.
    
    TODO:
        - Integrate an API call to a cost-effective model (e.g., GPT-4o mini) to perform the formatting.
        - Insert tags or annotations (e.g., {sanitized:object.type}) where parts of the input are unclear or redacted.
        - Handle potential errors from the formatting agent and provide informative messages.
    """
    # For now, we simulate fallback formatting by simply stripping the input and appending a note.
    sanitized_prompt = raw_input.strip()
    
    # Placeholder for API call to formatting agent:
    # response = call_formatting_agent(raw_input)  # #Placeholder: integrate actual agent call
    # sanitized_prompt = response.get("formatted_prompt", sanitized_prompt)
    # details = response.get("details", "Fallback formatting applied; details not available.")  # #Placeholder
    
    # For this stub, we simply append a note indicating fallback was used.
    sanitized_prompt += "\n\n[Note: Fallback formatting applied. Some content may have been sanitized.]"
    
    return {
        "prompt": sanitized_prompt,
        "fallback": True,
        "details": "Fallback formatting applied. Replace with agent response when implemented. #Placeholder"
    }

# For quick local testing, you can uncomment the block below:
# if __name__ == "__main__":
#     test_input = "raw, messy input that does not conform to schema..."
#     result = sanitize_input(test_input)
#     print(result)


# File: src\hivechain\hivechain_core.py

# hivechain_core.py
"""
Module: hivechain_core.py
Description:
  Manages the global configuration and shared state for HiveChain.
  By default, the configuration is made immutable to ensure consistency and avoid accidental modifications.
  However, an optional parameter allows disabling immutability if dynamic updates are required.
  
Keywords: singleton, global state, initialization, immutable.
"""

from types import MappingProxyType

_config = None

def init_config(config: dict, immutable: bool = True):
    """
    Initialize the library's configuration.
    Must be called once by the application before using other library functions.
    
    Args:
        config (dict): The configuration dictionary to be set as the global configuration.
        immutable (bool, optional): If True (default), the configuration will be made immutable.
                                    Set to False to allow modifications at runtime.
    """
    global _config
    if immutable:
        _config = MappingProxyType(config)
    else:
        _config = config

def get_config():
    """
    Retrieve the current configuration.
    
    Returns:
        dict: The global configuration.
    
    Raises:
        RuntimeError: If the configuration has not been initialized.
    """
    if _config is None:
        raise RuntimeError("Configuration not initialized. Please call init_config() first.")
    return _config


# File: src\hivechain\input_formatter.py

# input_formatter.py
"""
Module: input_formatter.py
Responsibility:
  - Process raw user input and return a structured prompt.
  - Validate input against expected criteria.
  - Mark the input as valid or not, so the pipeline can decide whether to trigger fallback formatting.
"""

def format_input(raw_input: str) -> dict:
    """
    Processes the raw input into a structured prompt.
    
    Args:
        raw_input (str): The raw user input.
        
    Returns:
        dict: A dictionary containing:
            - "prompt": the processed text.
            - "valid": a boolean flag indicating whether the input fits our expected schema.
    
    Current simple rule:
      - If the stripped input has fewer than 10 characters, it is considered not valid.
      
    #Placeholder: Add more complex validation logic (e.g., regex checks, JSON schema validation) as needed.
    """
    cleaned_input = raw_input.strip()
    # Simple rule: inputs shorter than 10 characters are flagged as not valid.
    if len(cleaned_input) < 10:
        return {"prompt": cleaned_input, "valid": False}
    
    # Otherwise, consider it valid.
    return {"prompt": cleaned_input, "valid": True}

# For testing purposes, you can uncomment the block below:
# if __name__ == "__main__":
#     test_input = "Hello"
#     print(format_input(test_input))


# File: src\hivechain\memory_manager.py

# memory_manager.py
"""
Module: memory_manager.py
Description:
  Manages conversation memory for multi-turn interactions using a simple rolling window.
  For now, this implementation is list-based and maintains a history of conversation messages.
  If the total token count exceeds a defined maximum, older messages are removed.
  
Key Tasks:
  - Append messages to memory.
  - Return the conversation history.
  - Enforce a maximum token count (using a placeholder token counting method).
  
#Placeholder: Replace the simple whitespace-based token count with a more accurate tokenizer.
#Placeholder: In the future, swap this implementation with a vector store or a persistent memory solution.
"""

class MemoryManager:
    def __init__(self, max_tokens: int = 2048):
        """
        Initializes the MemoryManager with a maximum token limit.
        
        Args:
            max_tokens (int): The maximum total token count for the conversation memory.
        """
        self.max_tokens = max_tokens
        self.memory = []  # List of messages, each a dict with keys 'role' and 'content'.
    
    def _count_tokens(self, text: str) -> int:
        """
        Counts tokens in a given text using a simple whitespace split.
        #Placeholder: Replace with a proper tokenization method.
        
        Args:
            text (str): The text to count tokens from.
            
        Returns:
            int: The number of tokens.
        """
        return len(text.split())
    
    def add_message(self, role: str, content: str):
        """
        Adds a message to the conversation memory. If the total token count exceeds max_tokens,
        older messages are removed until the total is within the limit.
        
        Args:
            role (str): The role of the message sender (e.g., 'user', 'assistant').
            content (str): The content of the message.
        """
        new_message = {"role": role, "content": content}
        self.memory.append(new_message)
        
        # Enforce the maximum token limit.
        total_tokens = sum(self._count_tokens(msg["content"]) for msg in self.memory)
        while total_tokens > self.max_tokens and self.memory:
            removed = self.memory.pop(0)
            total_tokens = sum(self._count_tokens(msg["content"]) for msg in self.memory)
    
    def get_memory(self) -> list:
        """
        Returns the current conversation history.
        
        Returns:
            list: A copy of the conversation memory.
        """
        return self.memory.copy()
    
    def reset_memory(self):
        """
        Clears the entire conversation memory.
        """
        self.memory.clear()

# Singleton instance for easy use across the application.
memory_manager = MemoryManager()

# For local testing, you can uncomment the block below:
# if __name__ == "__main__":
#     memory_manager.add_message("user", "Hello, how are you?")
#     memory_manager.add_message("assistant", "I'm good, thank you!")
#     print("Current Memory:", memory_manager.get_memory())
#     memory_manager.reset_memory()
#     print("Memory after reset:", memory_manager.get_memory())


# File: src\hivechain\output_formatter.py

# output_formatter.py
"""
Module: output_formatter.py
Responsibility:
  - Transform the raw API response (e.g., from openai.ChatCompletion.create) into a standardized output.
  - Extract key pieces of information such as the generated text.
  - Include metadata (e.g., whether fallback formatting was used) if applicable.
  
TODO:
  - Enhance error handling as needed for different API response formats.
  - Optionally add more detailed logging or extraction of additional metadata.
"""

def format_output(api_response: dict) -> dict:
    """
    Transforms the raw API response into a standardized format.
    
    Args:
        api_response (dict): The raw response from the API caller.
        
    Returns:
        dict: A dictionary containing:
            - "result": The generated text from the API.
            - "raw": The full, unmodified API response.
            - Optionally, you can add extra keys for metadata (e.g., fallback_used, processing_time, etc.)
    
    Raises:
        ValueError: If the expected keys are not found in the API response.
    """
    try:
        # Extract the generated text.
        # This assumes the response structure is similar to OpenAI's:
        # {'choices': [{'message': {'content': <generated_text>}}], ... }
        generated_text = api_response['choices'][0]['message']['content']
    except (KeyError, IndexError) as e:
        raise ValueError("Unexpected API response format. Ensure the API response conforms to expected structure.") from e
    
    # Construct and return the standardized output.
    return {
        "result": generated_text,
        "raw": api_response,
        # Additional metadata can be added here, for example:
        # "fallback_used": <True/False>, "details": "..." etc.
    }

# For local testing, you can uncomment the block below:
# if __name__ == "__main__":
#     # Simulate a raw API response (this structure should match the actual API's response)
#     simulated_response = {
#         "choices": [
#             {"message": {"content": "This is a sample generated text."}}
#         ],
#         "usage": {"total_tokens": 50}
#     }
#     output = format_output(simulated_response)
#     print(output)


# File: src\hivechain\pipeline.py

# pipeline.py
"""
Module: pipeline.py

Overview:
    This module orchestrates the complete processing of raw user input through the HiveChain pipeline.
    It validates and formats the input (using a standard or fallback formatter), calls the API via the
    provider adapter through the api_caller module, and formats the API response.
    Optionally, it wraps the response with additional HiveChain metadata.

Responsibilities:
    1. Input Processing:
        - Validate raw input using input_formatter.
        - Use fallback_formatter if the input does not match expected schema.
        - Otherwise, use standard_formatter.
    
    2. API Invocation:
        - Determine the model to use (defaulting to the configuration if unspecified).
        - Call the backend API via the api_caller module.
    
    3. Response Wrapping:
        - If wrap_response is True (or if the raw response is not dict-like), return a dictionary with:
              "raw": the full API response,
              "result": the extracted generated text,
              "fallback_used": a flag indicating if fallback formatting was applied.
        - Otherwise, return the raw API response.

Usage:
    Call process_request() with the raw input and any optional overrides.
    Set wrap_response=True to obtain HiveChain metadata along with the API response.
"""

from hivechain.input_formatter import format_input
from hivechain.fallback_formatter import sanitize_input
from hivechain.standard_formatter import standard_format_input
from hivechain.api_caller import call_api
# Note: output_formatter is available for further processing if needed.
from hivechain.hivechain_core import get_config

def process_request(raw_input: str, model_name: str = None, temperature: float = None,
                    max_tokens: int = None, wrap_response: bool = False) -> dict:
    """
    Processes raw user input through the complete HiveChain pipeline.

    Args:
        raw_input (str): The raw user input.
        model_name (str, optional): The model name to use. If None, defaults to the configuration's default.
        temperature (float, optional): Override for temperature.
        max_tokens (int, optional): Override for maximum tokens.
        wrap_response (bool, optional): If True, returns a dictionary containing:
                                        - "raw": the raw API response,
                                        - "result": the extracted generated text,
                                        - "fallback_used": a flag indicating if fallback formatting was applied.
                                        Defaults to False (returning the raw response).

    Returns:
        dict: Either the raw API response or a wrapped response with metadata.
    """
    # Step 1: Validate and format the input.
    initial_structured = format_input(raw_input)
    if not initial_structured.get("valid", False):
        print("Warning: Input did not conform to expected schema. Using fallback formatter.")
        structured_prompt = sanitize_input(raw_input)
    else:
        structured_prompt = standard_format_input(raw_input)
    
    # Step 2: Determine which model to use.
    if model_name is None:
        config = get_config()
        model_name = config.get("default_model", "openai")
    
    # Step 3: Call the API using the structured prompt.
    raw_response = call_api(structured_prompt, model_name, temperature, max_tokens)
    
    # Debug: Uncomment the lines below for debugging purposes.
    # print("DEBUG: wrap_response =", wrap_response)
    # print("DEBUG: type(raw_response) =", type(raw_response))
    
    # Step 4: Wrap the response if requested or if the raw response is not dict-like.
    if wrap_response or not hasattr(raw_response, "get"):
        try:
            generated_text = raw_response.choices[0].message.content
        except (AttributeError, IndexError):
            generated_text = ""
        return {
            "raw": raw_response,
            "result": generated_text,
            "fallback_used": structured_prompt.get("fallback", False)
        }
    else:
        return raw_response

# For local testing, you can uncomment the block below:
# if __name__ == "__main__":
#     test_input = "Hello, tell me a little about yourself."
#     result = process_request(test_input, model_name="openai", wrap_response=True)
#     print("Final Output:", result)


# File: src\hivechain\request_builder.py

# request_builder.py
"""
Module: request_builder.py
Description:
  Constructs the API request payload by converting a structured prompt into the format
  expected by the backend API. This module separates the request construction from the
  network call, enabling easier customization and extension.

Key Tasks:
  - Build a basic payload (e.g., a list of messages for chat completions).
  - Provide a clear placeholder for additional logic (e.g., inserting context or system messages).

Keywords: payload, construction, abstraction.
"""

def build_request_payload(structured_prompt: dict) -> dict:
    """
    Constructs the request payload for the API call.

    Args:
        structured_prompt (dict): A dictionary containing at least a "prompt" key with the text.

    Returns:
        dict: A dictionary representing the payload to be sent to the API.
    
    Example:
        Input: {"prompt": "Tell me a joke about programming.", ...}
        Output: {"messages": [{"role": "user", "content": "Tell me a joke about programming."}]}

    #Placeholder: Extend with additional logic to incorporate context, system messages,
    # or multi-turn conversation data as needed.
    """
    payload = {
        "messages": [
            {"role": "user", "content": structured_prompt.get("prompt", "")}
        ]
    }
    
    # #Placeholder: Insert additional messages, context, or formatting as required in the future.
    
    return payload

# For local testing, you can uncomment the block below:
# if __name__ == "__main__":
#     test_prompt = {"prompt": "Tell me a joke about programming.", "fallback": False, "details": "Standard formatting applied."}
#     print(build_request_payload(test_prompt))


# File: src\hivechain\response_processor.py

# response_processor.py
"""
Module: response_processor.py
Description:
  Parses and standardizes API responses.
  Extracts the generated text from the API response and optionally converts response objects
  to dictionaries if needed.
  
Key Tasks:
  - Extract generated text.
  - Optionally convert the response object to a dict (e.g., via .to_dict()) if the API supports it.
  
Keywords: extraction, standardization, formatting.
"""

def process_response(api_response) -> dict:
    """
    Parses the raw API response and standardizes it.
    
    Args:
        api_response: The raw response object returned by the API call.
        
    Returns:
        dict: A standardized dictionary containing:
            - "result": The generated text extracted from the response.
            - "raw": The full raw API response.
    
    #Placeholder: If needed, convert the api_response to a dictionary using .to_dict()
    """
    try:
        # Attempt to extract the generated text using attribute access.
        generated_text = api_response.choices[0].message.content
    except (AttributeError, IndexError) as e:
        raise ValueError("Unexpected API response format: could not extract generated text.") from e

    # Return a standardized dictionary.
    return {
        "result": generated_text,
        "raw": api_response
    }

# For local testing, you can uncomment the block below:
# if __name__ == "__main__":
#     # Simulate a raw API response object (dummy example)
#     class FakeMessage:
#         def __init__(self, content):
#             self.content = content
#     class FakeChoice:
#         def __init__(self, content):
#             self.message = FakeMessage(content)
#     class FakeResponse:
#         def __init__(self, content):
#             self.choices = [FakeChoice(content)]
#     fake_response = FakeResponse("This is a sample generated text.")
#     processed = process_response(fake_response)
#     print(processed)


# File: src\hivechain\retriever.py

# retriever.py
"""
Module: retriever.py
Description:
  Provides retrieval-augmented generation (RAG) capabilities.
  For now, this module returns an empty context or dummy data.
  In the future, integrate vector search or document retrieval to provide relevant external context.
  
Key Tasks:
  - Initially return an empty context or placeholder data.
  - Future: Replace with a real retrieval system (e.g., vector search, database query, etc.).
  
Keywords: retrieval, external context, RAG, pluggable.
"""

def retrieve_context(query: str) -> dict:
    """
    Retrieves external context based on the query.
    
    Args:
        query (str): The user query for which to retrieve relevant external context.
        
    Returns:
        dict: A dictionary containing the retrieved context.
              For now, returns an empty context.
    
    #Placeholder: Integrate with a vector search or document retrieval system in the future.
    """
    # Dummy implementation: return an empty context.
    return {
        "context": ""
    }

# For local testing, you can uncomment the block below:
# if __name__ == "__main__":
#     test_query = "What is the capital of France?"
#     result = retrieve_context(test_query)
#     print("Retrieved context:", result)


# File: src\hivechain\standard_formatter.py

# standard_formatter.py
"""
Module: standard_formatter.py
Responsibility:
  - Format input that has been validated as conforming to expected patterns.
  - Convert the valid raw input into a structured prompt.
  - This module is designed to be modular so that you can later extend its behavior
    (e.g., adding punctuation, converting to a specific JSON structure, etc.)
"""

def standard_format_input(raw_input: str) -> dict:
    """
    Processes the valid input into a structured prompt.
    
    Args:
        raw_input (str): The raw user input that has been validated.
        
    Returns:
        dict: A dictionary containing:
            - "prompt": the formatted text,
            - "fallback": False (indicating no fallback was applied),
            - "details": a note describing that standard formatting was used.
            
    #Placeholder: Extend with additional formatting logic if needed (e.g., punctuation, capitalization).
    """
    # Minimal formatting: trim whitespace.
    formatted = raw_input.strip()
    
    return {
        "prompt": formatted,
        "fallback": False,
        "details": "Standard formatting applied. #Placeholder for extended formatting logic."
    }

# For local testing, you can uncomment the block below:
# if __name__ == "__main__":
#     test_input = "Hello, how are you doing?"
#     result = standard_format_input(test_input)
#     print(result)


# File: src\hivechain\__init__.py



# File: src\hivechain\provider_adapters\deepseek_provider.py

# deepseek_provider.py
"""
Module: deepseek_provider.py
Responsibility:
  - Adapter for DeepSeek.
  - Implements generate_text(prompt, params) to call the DeepSeek API.
  - Uses environment variable DEEPSEEK_API_KEY and a provider-specific API base.
  
Keywords: adapter, vendor-specific.
  
TODO: Integrate with DeepSeek's actual API if different from OpenAI's interface.
"""

import os
import openai  # Assuming DeepSeek uses an OpenAI-compatible interface

def generate_text(prompt: str, params: dict) -> dict:
    """
    Calls the DeepSeek API to generate text based on the prompt.
    
    Args:
        prompt (str): The input prompt.
        params (dict): Parameters including:
                       - "engine": model identifier (default "deepseek-chat")
                       - "temperature": generation temperature (default 0.5)
                       - "max_tokens": maximum tokens (default 512)
                       - "api_base": DeepSeek endpoint (default "https://api.deepseek.com")
    
    Returns:
        dict: The API response.
    """
    openai.api_key = os.getenv("DEEPSEEK_API_KEY")
    openai.api_base = params.get("api_base", "https://api.deepseek.com")
    
    messages = [{"role": "user", "content": prompt}]
    
    response = openai.OpenAI().chat.completions.create(
        model=params.get("engine", "deepseek-chat"),
        messages=messages,
        temperature=params.get("temperature", 0.5),
        max_tokens=params.get("max_tokens", 512)
    )
    
    return response

# For local testing, you might add:
# if __name__ == "__main__":
#     test_params = {"engine": "deepseek-chat", "temperature": 0.5, "max_tokens": 512}
#     print(generate_text("Explain deep learning in simple terms.", test_params))


# File: src\hivechain\provider_adapters\huggingface_provider.py

# huggingface_provider.py
"""
Module: huggingface_provider.py
Responsibility:
  - Placeholder adapter for HuggingFace models.
  - Implements generate_text(prompt, params) as a stub for future integration.
  
Keywords: adapter, extendability.
  
TODO: Integrate HuggingFace's API or local inference mechanisms.
"""

def generate_text(prompt: str, params: dict) -> dict:
    """
    Simulates generating text using a HuggingFace model.
    
    Args:
        prompt (str): The input prompt.
        params (dict): Parameters for text generation.
    
    Returns:
        dict: A simulated API response.
    """
    # #Placeholder: Replace this stub with actual HuggingFace integration.
    return {
        "choices": [
            {"message": {"content": "This is a placeholder response from HuggingFace adapter."}}
        ]
    }

# For local testing, you might add:
# if __name__ == "__main__":
#     test_params = {"engine": "mistral-7b", "temperature": 0.5, "max_tokens": 8192}
#     print(generate_text("What is the capital of France?", test_params))


# File: src\hivechain\provider_adapters\openai_provider.py

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


# File: src\hivechain\provider_adapters\__init__.py

