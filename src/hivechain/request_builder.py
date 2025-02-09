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
