"""Memory system for agents."""

from typing import List, Dict, Any
from collections import deque

class Memory:
    """Simple memory system."""
    
    def __init__(self, max_size: int = 100):
        self.max_size = max_size
        self.short_term = deque(maxlen=max_size)
        self.long_term: List[Dict[str, Any]] = []
    
    def add(self, query: str, response: str):
        """Add interaction to memory."""
        self.short_term.append({
            "query": query,
            "response": response
        })
    
    def get_context(self, query: str) -> str:
        """Get relevant context for a query."""
        if not self.short_term:
            return ""
        
        context = "Previous interactions:\n"
        for item in list(self.short_term)[-5:]:
            context += f"Q: {item['query']}\nA: {item['response']}\n\n"
        return context
    
    def clear(self):
        """Clear short-term memory."""
        self.short_term.clear()
    
    def save_long_term(self):
        """Save important interactions to long-term memory."""
        # TODO: Implement importance scoring
        pass
