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
