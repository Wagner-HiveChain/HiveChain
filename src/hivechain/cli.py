# cli.py
"""
Module: cli.py
Responsibility:
  - Provide a command-line interface (CLI) for interacting with the HiveChain pipeline.
  - Load configuration, initialize the library, parse user input, call the pipeline,
    and display the final output.
"""

import argparse
from .config_handler import load_config
from .hivechain_core import init_config
from .pipeline import process_request

def main():
    # Load configuration (from config.json, .env, etc.)
    config = load_config()
    # Initialize the library's configuration
    init_config(config)
    
    parser = argparse.ArgumentParser(description="AI Model Conversation CLI")
    parser.add_argument("prompt", type=str, help="User prompt for the AI model")
    # Use the keys from config["models"] to provide choices
    parser.add_argument("--model", choices=config["models"].keys(), 
                        help="Which model to use (as defined in config.json)")
    parser.add_argument("--temperature", type=float, help="Temperature for generation")
    parser.add_argument("--max-tokens", type=int, dest="max_tokens", help="Max tokens for the response")
    args = parser.parse_args()

    try:
        # Set wrap_response=True so we get HiveChain metadata along with the raw API response.
        response = process_request(
            raw_input=args.prompt,
            model_name=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            wrap_response=True
        )
        print("GPT-4o Mini:", response.get("result", ""), "\n")
        if "fallback_used" in response and response["fallback_used"]:
            print("Warning: Fallback formatting was applied to the input.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
