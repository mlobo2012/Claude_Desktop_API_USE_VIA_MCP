# Claude Desktop API Integration via MCP

This project provides an MCP server implementation that enables seamless integration between Claude Desktop and the Claude API. It allows you to bypass Professional Plan limitations and access advanced features like custom system prompts and conversation management.

## Features

- Direct Claude API integration via MCP
- Conversation history tracking and management
- System prompt support
- Seamless switching between Professional Plan and API usage
- Easy configuration with Claude Desktop

## When to Use

- **Professional Plan** (default):
  - Regular conversations in Claude Desktop
  - Basic usage within plan limits
  - No special configuration needed

- **API Token** (via this MCP server):
  - When you need longer context windows
  - To use custom system prompts
  - To bypass rate limits
  - For advanced conversation management

## Setup Instructions

1. **Clone the Repository**
   ```bash
   # Using VS Code:
   # 1. Press Cmd + Shift + P
   # 2. Type "Git: Clone"
   # 3. Paste: https://github.com/mlobo2012/Claude_Desktop_API_USE_VIA_MCP.git

   # Or using terminal:
   git clone https://github.com/mlobo2012/Claude_Desktop_API_USE_VIA_MCP.git
   cd Claude_Desktop_API_USE_VIA_MCP
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   ```bash
   # Copy environment template
   cp .env.example .env

   # Edit .env and add your API key
   ANTHROPIC_API_KEY=your_api_key_here
   ```

4. **Configure Claude Desktop**
   - macOS: Navigate to `~/Library/Application Support/Claude/`
     ```bash
     # Using Finder:
     # 1. Press Cmd + Shift + G
     # 2. Enter: ~/Library/Application Support/Claude/
     ```
   - Windows: Navigate to `%APPDATA%\Claude\`
   - Create or edit `claude_desktop_config.json`
   - Copy contents from `config/claude_desktop_config.json`
   - Update paths and API keys

## Usage Guide

### Basic Usage

1. **Regular Claude Desktop Usage**
   - Just chat normally with Claude
   - Uses your Professional Plan
   - No special commands needed

2. **API Usage**
   ```
   @claude-api Please answer using the API: What is the capital of France?
   ```

### Advanced Features

1. **Using System Prompts**
   ```
   @claude-api {"system_prompt": "You are an expert fitness coach"} Create a workout plan
   ```

2. **Managing Conversations**
   ```
   # Start a new conversation
   @claude-api {"conversation_id": "project1"} Let's discuss Python

   # Continue same conversation
   @claude-api {"conversation_id": "project1"} Tell me more

   # View conversation history
   @claude-api get_conversation_history project1

   # Clear conversation
   @claude-api clear_conversation project1
   ```

### Cost Management

- API calls use your Anthropic API credits and may incur charges
- Use the Professional Plan for regular queries
- Only use @claude-api when you specifically need:
  - Longer context windows
  - Custom system prompts
  - To bypass rate limits

## MCP Tools Available

1. `query_claude`
   - Make direct API calls to Claude
   - Support for system prompts
   - Conversation tracking

2. `clear_conversation`
   - Reset conversation history
   - Manage multiple conversation threads

3. `get_conversation_history`
   - Retrieve conversation records
   - Debug conversation flow

## Development

The main server implementation is in `src/claude_api_server.py`. To extend functionality, you can add new tools using the `@mcp.tool()` decorator.

Example of adding a new tool:

```python
@mcp.tool()
async def custom_tool(param: str) -> str:
    """
    Custom tool description
    
    Args:
        param: Parameter description
    """
    try:
        # Tool implementation
        return result
    except Exception as e:
        return f"Error: {str(e)}"
```

## Troubleshooting

1. **API Key Issues**
   - Verify your API key in .env
   - Check Claude Desktop config paths
   - Ensure API key has correct permissions

2. **Connection Issues**
   - Check if MCP server is running
   - Verify Python environment
   - Check Claude Desktop logs

3. **Usage Issues**
   - Ensure correct @claude-api syntax
   - Check conversation IDs
   - Verify system prompt format

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT

## Support

For issues and questions:
1. Open an issue in the repository
2. Check existing discussions
3. Review the troubleshooting guide