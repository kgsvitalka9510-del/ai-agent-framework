"""Tool abstraction."""

from typing import Callable, Any

class Tool:
    """Base tool class."""
    
    def __init__(self, name: str, description: str, function: Callable = None):
        self.name = name
        self.description = description
        self.function = function
    
    def execute(self, **kwargs) -> Any:
        """Execute the tool."""
        if self.function:
            return self.function(**kwargs)
        raise NotImplementedError("Tool function not implemented")
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "description": self.description
        }
