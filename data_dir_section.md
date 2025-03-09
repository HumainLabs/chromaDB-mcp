# Customizing Data Storage Location

You can customize where ChromaDB stores its data using any of these methods (in order of precedence):

## 1. Command-Line Argument

When starting the server directly:
```bash
chroma-mcp --data-dir /path/to/your/data
```

When using uv:
```bash
uv run chroma-mcp --data-dir /path/to/your/data
```

## 2. Environment Variable

Set the `CHROMA_MCP_DATA_DIR` environment variable:

```bash
# Linux/macOS
export CHROMA_MCP_DATA_DIR=/path/to/your/data
chroma-mcp

# Windows
set CHROMA_MCP_DATA_DIR=C:\path\to\your\data
chroma-mcp
```

## 3. Claude Desktop Configuration

When configuring for Claude Desktop, you can pass the data directory as an argument:

```json
{
  "mcpServers": {
    "chroma": {
      "command": "chroma-mcp",
      "args": ["--data-dir", "/path/to/your/data"]
    }
  }
}
```

## 4. Cursor IDE Configuration

Similarly for Cursor IDE in your `.cursor/mcp.json` file:

```json
{
  "mcpServers": {
    "chroma": {
      "command": "chroma-mcp",
      "args": ["--data-dir", "/path/to/your/data"]
    }
  }
}
```

> **Tip**: For persistent data storage, choose a location outside your project directory, such as a dedicated data directory in your user home folder or another permanent location. 