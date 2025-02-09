#!/usr/bin/env python3
# run.py
"""
Module: run.py
Responsibility:
  - Provide an interactive CLI that uses the complete HiveChain pipeline.
  - Force the use of the GPT-4o mini model.
  - Handle user conversation, exit gracefully, and print the standardized output.
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
            
            # Process the request through the full pipeline.
            response = process_request(raw_input=prompt, model_name=model)
            # Print the standardized output (assuming "result" holds the generated text).
            print("GPT-4o Mini:", response.get("result", ""), "\n")
        except KeyboardInterrupt:
            print("\nConversation interrupted. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print("Error:", e, file=sys.stderr)

if __name__ == "__main__":
    main()
