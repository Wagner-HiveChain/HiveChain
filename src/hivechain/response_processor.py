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
