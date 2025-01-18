from mcp.server.fastmcp import FastMCP
import anthropic
import os
from dotenv import load_dotenv
from typing import Dict, List, Optional
import json

# Load environment variables
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("ClaudeAPI")

# Initialize Anthropic client
client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

class KnowledgeBase:
    def __init__(self):
        self.conversations: Dict[str, List[Dict]] = {}
        
    def add_message(self, conversation_id: str, message: Dict):
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = []
        self.conversations[conversation_id].append(message)
        
    def get_conversation(self, conversation_id: str) -> List[Dict]:
        return self.conversations.get(conversation_id, [])

# Initialize knowledge base
kb = KnowledgeBase()

@mcp.tool()
async def query_claude(prompt: str, conversation_id: str = "default", system_prompt: Optional[str] = None) -> str:
    """
    Query Claude API with a prompt and optional system prompt
    
    Args:
        prompt: The user's query
        conversation_id: Unique identifier for the conversation
        system_prompt: Optional system prompt to guide Claude's behavior
    """
    try:
        # Get conversation history
        messages = kb.get_conversation(conversation_id)
        
        # Construct the new message
        message = {
            "role": "user",
            "content": prompt
        }
        
        # Add message to history
        kb.add_message(conversation_id, message)
        
        # Make API call to Claude
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4096,
            temperature=0.7,
            system=system_prompt if system_prompt else None,
            messages=messages + [message]
        )
        
        # Store Claude's response
        assistant_message = {
            "role": "assistant",
            "content": response.content[0].text
        }
        kb.add_message(conversation_id, assistant_message)
        
        return response.content[0].text
        
    except Exception as e:
        return f"Error querying Claude API: {str(e)}"

@mcp.tool()
async def clear_conversation(conversation_id: str = "default") -> str:
    """Clear a specific conversation history"""
    try:
        if conversation_id in kb.conversations:
            kb.conversations[conversation_id] = []
            return f"Conversation {conversation_id} cleared successfully"
        return f"Conversation {conversation_id} not found"
    except Exception as e:
        return f"Error clearing conversation: {str(e)}"

@mcp.tool()
async def get_conversation_history(conversation_id: str = "default") -> str:
    """Get the conversation history for a specific ID"""
    try:
        history = kb.get_conversation(conversation_id)
        return json.dumps(history, indent=2)
    except Exception as e:
        return f"Error retrieving conversation history: {str(e)}"

if __name__ == "__main__":
    mcp.run()