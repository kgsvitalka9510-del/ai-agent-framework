"""Core Agent class."""

from typing import List, Optional, Dict, Any
from .memory import Memory
from .tool import Tool

class Agent:
    """AI Agent with memory and tools."""
    
    def __init__(
        self,
        model: str = "gpt-4",
        memory: bool = True,
        tools: Optional[List[Tool]] = None,
        system_prompt: Optional[str] = None
    ):
        self.model = model
        self.memory = Memory() if memory else None
        self.tools = tools or []
        self.system_prompt = system_prompt or "You are a helpful assistant."
        self.conversation = []
    
    def run(self, query: str) -> str:
        """Run the agent with a query."""
        # Add to conversation
        self.conversation.append({"role": "user", "content": query})
        
        # Get memory context
        context = ""
        if self.memory:
            context = self.memory.get_context(query)
        
        # Get tool descriptions
        tool_desc = self._get_tool_descriptions()
        
        # Build prompt
        prompt = f"{self.system_prompt}\n\n{context}\n\n{tool_desc}\n\nUser: {query}"
        
        # TODO: Call LLM API
        response = f"Agent response to: {query}"
        
        # Add to conversation
        self.conversation.append({"role": "assistant", "content": response})
        
        # Update memory
        if self.memory:
            self.memory.add(query, response)
        
        return response
    
    def _get_tool_descriptions(self) -> str:
        """Get descriptions of available tools."""
        if not self.tools:
            return ""
        
        desc = "Available tools:\n"
        for tool in self.tools:
            desc += f"- {tool.name}: {tool.description}\n"
        return desc
    
    def add_tool(self, tool: Tool):
        """Add a tool to the agent."""
        self.tools.append(tool)
    
    def clear_memory(self):
        """Clear agent memory."""
        if self.memory:
            self.memory.clear()
