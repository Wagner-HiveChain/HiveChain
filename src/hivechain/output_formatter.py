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
