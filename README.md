# ChromaDB MCP Server 🧩

[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintained by HumainLabs.ai](https://img.shields.io/badge/Maintained%20by-HumainLabs.ai-orange)](https://humainlabs.ai)
[![MCP Protocol](https://img.shields.io/badge/MCP-Protocol-green)](https://modelcontextprotocol.ai)

A powerful Model Context Protocol (MCP) server implementation that provides seamless vector database capabilities through ChromaDB. Enhance your AI applications with semantic document search, metadata filtering, and persistent document storage.

<div align="center">
  <table border="0" cellspacing="0" cellpadding="0">
    <tr align="center">
      <td width="45%"><img src="humainlabs.ai.png" width="200px" alt="HumainLabs.ai logo"/></td>
      <td width="10%"><h2>×</h2></td>
      <td width="45%"><img src="chromadb.jpg" width="150px" alt="ChromaDB logo"/></td>
    </tr>
  </table>
  <p><i>HumainLabs.ai fork of privetin/chroma</i></p>
  <a href="https://humainlabs.ai">HumainLabs.ai -- Cognitive Framework Engineering & Research</a>
</div>

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage Examples](#-usage-examples)
- [API Reference](#-api-reference)
  - [Document Management](#document-management-tools)
  - [Search Operations](#search-tools)
  - [Collection Management](#collection-management-tools)
  - [Document Versioning](#document-versioning-tools)
- [Development](#-development)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## 🔍 Overview

The ChromaDB MCP Server bridges the gap between Language Models and vector databases. By implementing the Model Context Protocol (MCP), this server allows AI assistants to:

- **Store and retrieve documents** with semantic understanding
- **Search for related content** based on meaning rather than keywords
- **Filter results** using metadata and content specifications
- **Maintain persistent storage** across sessions
- **Manage document versions** to track changes over time
- **Organize content in collections** for better document management

MCP (Model Context Protocol) is an open protocol that standardizes how AI models interact with external tools and resources. This implementation focuses on document storage and retrieval powered by ChromaDB's vector database capabilities.

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Semantic Search** | Find documents based on meaning rather than exact matches using ChromaDB's embedding models |
| **Hybrid Search** | Combine semantic and keyword search with adjustable weights for optimal results |
| **Multi-Query Search** | Search with multiple queries at once and aggregate results with union or intersection |
| **Metadata Filtering** | Narrow search results by specific metadata fields (e.g., date, author, category) |
| **Content Filtering** | Apply additional text-based filters to search results |
| **Document Versioning** | Track document changes over time with version history and retrieval |
| **Collection Management** | Organize documents into separate collections for better content organization |
| **Bulk Operations** | Create multiple documents in a single operation for improved performance |
| **Persistent Storage** | Documents persist in local storage between server restarts |
| **Comprehensive Error Handling** | Clear error messages and automatic retry mechanisms for reliability |
| **Cross-Platform Support** | Works on Windows, macOS, and Linux |
| **MCP Integration** | Seamlessly works with Claude and other MCP-compatible AI assistants |

## 📦 Requirements

- Python 3.12 or higher
- ChromaDB 0.4.22 or higher
- MCP SDK 1.1.2 or higher
- Sentence Transformers 2.2.2 or higher

## 🚀 Quick Start

1. **Install the package**:
   ```bash
   pip install .
   ```

2. **Start the server**:
   ```bash
   chroma-mcp
   ```

3. **Configure your AI assistant** to use the server (see [Configuration](#-configuration))

4. **Start storing and retrieving documents!**

## 📥 Installation

### Using pip

```bash
# Clone the repository
git clone https://github.com/humainlabs/chromadb-mcp.git
cd chromadb-mcp

# Install directly
pip install .

# Or install in development mode
pip install -e .
```

### Using uv (recommended for development)

```bash
# Create and activate virtual environment
uv venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies
uv sync --dev --all-extras
```

### Directory Structure Change

> **Note**: The module has been renamed from `chroma` to `chroma_mcp` to avoid conflicts with the official ChromaDB package.

If you're upgrading from a previous version, the data directory has moved from `src/chroma/data` to `src/chroma_mcp/data`. To migrate your existing data, run the included migration script:

```bash
python migrate_data.py
```

## 🔄 Usage Examples

### Creating and Storing Documents

```python
# Create a new document with metadata
create_document({
    "document_id": "research_paper_123",
    "content": "Recent advancements in transformer models have revolutionized NLP tasks.",
    "metadata": {
        "year": 2023,
        "author": "Smith et al.",
        "field": "natural language processing",
        "tags": ["transformers", "deep learning"]
    }
})
```

### Creating Multiple Documents at Once

```python
# Bulk create multiple documents
bulk_create_documents({
    "documents": [
        {
            "document_id": "research_paper_123",
            "content": "Transformer models have revolutionized NLP.",
            "metadata": {"year": 2023, "field": "NLP"}
        },
        {
            "document_id": "research_paper_124",
            "content": "Reinforcement learning from human feedback improves model alignment.",
            "metadata": {"year": 2023, "field": "AI alignment"}
        },
        {
            "document_id": "research_paper_125",
            "content": "Multimodal models can process both text and images.",
            "metadata": {"year": 2023, "field": "multimodal AI"}
        }
    ]
})
```

### Searching with Hybrid Mode

```python
# Find documents using a combination of semantic and keyword matching
hybrid_search({
    "query": "transformer architecture improvements",
    "keyword_weight": 0.3,  # 0.0 for pure semantic, 1.0 for pure keyword
    "num_results": 3,
    "metadata_filter": {
        "year": 2023,
        "field": "natural language processing"
    }
})
```

### Searching with Multiple Queries

```python
# Search with multiple related queries and combine the results
multi_query_search({
    "queries": [
        "transformer architecture",
        "attention mechanisms",
        "language model training"
    ],
    "aggregation": "union",  # or "intersection" for documents matching all queries
    "num_results": 5,
    "metadata_filter": {"field": "NLP"}
})
```

### Managing Document Versions

```python
# Create a new version of a document
create_document_version({
    "document_id": "research_paper_123",
    "content": "Updated research on transformer architectures and their applications.",
    "version_note": "Added new section on emerging applications",
    "metadata": {"last_updated": "2023-12-01"}
})

# List all versions of a document
list_document_versions({
    "document_id": "research_paper_123"
})

# Retrieve a specific version
get_document_version({
    "document_id": "research_paper_123",
    "version": 2  # or "latest"
})
```

### Working with Collections

```python
# Create a new collection
create_collection({
    "collection_name": "research_papers",
    "description": "Academic research papers on AI topics",
    "metadata": {"category": "academic", "field": "AI"}
})

# List all collections
list_collections()

# Delete a collection
delete_collection({
    "collection_name": "research_papers"
})
```

## 🧰 API Reference

### Document Management Tools

| Tool | Description | Parameters | Returns |
|------|-------------|------------|---------|
| `create_document` | Add a new document | `document_id`, `content`, optional `metadata` | Success confirmation |
| `read_document` | Retrieve a document | `document_id` | Document with content and metadata |
| `update_document` | Modify existing document | `document_id`, `content`, optional `metadata` | Success confirmation |
| `delete_document` | Remove a document | `document_id` | Success confirmation |
| `list_documents` | Get all documents | optional `limit`, `offset` | List of documents |
| `bulk_create_documents` | Add multiple documents at once | `

## ⚙️ Configuration

### Method 1: Claude Desktop Integration

Add the server configuration to your Claude Desktop config file:

**Windows**: `C:\Users\<username>\AppData\Roaming\Claude\claude_desktop_config.json`  
**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "chroma": {
      "command": "uv",
      "args": [
        "--directory",
        "C:/MCP/server/community/chroma-mcp",
        "run",
        "chroma-mcp"
      ]
    }
  }
}
```

### Method 2: Cursor IDE Project Configuration

For project-specific configuration in Cursor IDE, create a `.cursor/mcp.json` file in your project root:

```json
{
  "mcpServers": {
    "chroma": {
      "command": "chroma-mcp",
      "args": []
    }
  }
}
```

If running with uv instead of installing:

```json
{
  "mcpServers": {
    "chroma": {
      "command": "uv",
      "args": [
        "--directory",
        "C:/MCP/server/community/chroma-mcp",
        "run",
        "chroma-mcp"
      ]
    }
  }
}
```

### Storage Configuration

By default, documents are stored in:
- `src/chroma_mcp/data` directory
- This location persists between server restarts

### Customizing Data Storage Location

You can customize where ChromaDB stores its data using any of these methods (in order of precedence):

#### 1. Command-Line Argument

When starting the server directly:
```bash
chroma-mcp --data-dir /path/to/your/data
```

When using uv:
```bash
uv run chroma-mcp --data-dir /path/to/your/data
```

#### 2. Environment Variable

Set the `CHROMA_MCP_DATA_DIR` environment variable:

```bash
# Linux/macOS
export CHROMA_MCP_DATA_DIR=/path/to/your/data
chroma-mcp

# Windows
set CHROMA_MCP_DATA_DIR=C:\path\to\your\data
chroma-mcp
```

#### 3. Claude Desktop Configuration

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

#### 4. Cursor IDE Configuration

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

> **Tip**: For persistent data storage, choose a location outside your project directory, such as a dedicated data directory in your user home folder or another permanent location.# Customizing Data Storage Location

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