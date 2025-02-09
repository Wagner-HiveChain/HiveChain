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
