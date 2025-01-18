import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";
import { Claude } from "@anthropic-ai/sdk";

const log = (message: string) => {
  console.error(`[DEBUG] ${message}`);
};

const claude = new Claude({
  apiKey: process.env.ANTHROPIC_API_KEY
});

const server = new Server(
  {
    name: "claude-api",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {}
    }
  }
);

server.setRequestHandler(ListToolsRequestSchema, async () => {
  log("Listing tools...");
  return {
    tools: [
      {
        name: "send-message",
        description: "Send a message to Claude",
        inputSchema: {
          type: "object",
          properties: {
            message: {
              type: "string",
              description: "Message to send to Claude"
            }
          },
          required: ["message"]
        }
      }
    ]
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  log(`Executing tool: ${request.params.name}`);
  
  if (request.params.name === "send-message") {
    try {
      const msg = await claude.messages.create({
        model: "claude-3-opus-20240229",
        max_tokens: 1024,
        messages: [
          { role: "user", content: request.params.arguments.message }
        ]
      });

      return {
        content: [
          {
            type: "text",
            text: msg.content[0].text
          }
        ]
      };
    } catch (error) {
      log(`Error calling Claude API: ${error}`);
      throw error;
    }
  }
  throw new Error(`Unknown tool: ${request.params.name}`);
});

async function main() {
  try {
    log("Starting server...");
    const transport = new StdioServerTransport();
    await server.connect(transport);
    log("Server running");
  } catch (error) {
    log(`Server error: ${error}`);
    process.exit(1);
  }
}

main();