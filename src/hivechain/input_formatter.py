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
