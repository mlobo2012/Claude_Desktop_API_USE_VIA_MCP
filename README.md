# Claude Desktop API Integration via MCP

This project provides an MCP server implementation that enables the use of Claude API within Claude Desktop, bypassing professional plan limitations and adding advanced features like conversation management.

## Features

- Direct Claude API integration via MCP
- Conversation history tracking
- System prompt support
- Easy configuration with Claude Desktop

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and add your Anthropic API key:
```bash
cp .env.example .env
```

3. Update the configuration in `config/claude_desktop_config.json` with your paths and tokens.

4. Copy the configuration to Claude Desktop's config location:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

## Usage

The server provides several MCP tools:

- `query_claude`: Send queries to Claude API
- `clear_conversation`: Reset conversation history
- `get_conversation_history`: Retrieve conversation records

## Development

The main server implementation is in `src/claude_api_server.py`. To extend functionality, you can add new tools using the `@mcp.tool()` decorator.

## License

MIT