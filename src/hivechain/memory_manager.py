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
