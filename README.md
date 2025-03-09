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
- [How ChromaDB Integration Works](#-how-chromadb-integration-works)
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

## 🔌 How ChromaDB Integration Works

This MCP server uses **ChromaDB in embedded mode**, which means:

- **No Separate Service Required**: ChromaDB runs directly within the MCP server process
- **File-Based Storage**: Data is stored as files in the configured data directory
- **Single Process Deployment**: You only need to run the MCP server, ChromaDB is embedded
- **Automatic Persistence**: Data is automatically persisted to disk between server restarts

The data directory (configurable as described below) contains:
- Vector embeddings of your documents
- Metadata and content storage
- Index structures for efficient similarity search
- Collection information

Behind the scenes, this implementation:
1. Creates text embeddings using the Sentence Transformers library
2. Stores these embeddings with metadata in ChromaDB collections
3. Provides search capabilities using vector similarity
4. Handles document versioning and collection management on top of ChromaDB's features

> **Note**: While ChromaDB can also be run as a separate service, this implementation uses the embedded mode for simplicity and ease of deployment.

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
| `bulk_create_documents` | Add multiple documents at once | `documents` (array of document objects) | Success confirmation with count |

### Search Tools

| Tool | Description | Parameters | Returns |
|------|-------------|------------|---------|
| `search_similar` | Find semantically similar documents | `query`, optional `num_results`, `metadata_filter`, `content_filter` | Ranked documents with similarity scores |
| `hybrid_search` | Search with combined semantic and keyword matching | `query`, optional `keyword_weight` (0-1), `num_results`, `metadata_filter` | Ranked documents with relevance scores |
| `multi_query_search` | Search with multiple queries | `queries` (array), optional `aggregation` ("union"/"intersection"), `num_results`, `metadata_filter` | Combined ranked results from all queries |

### Collection Management Tools

| Tool | Description | Parameters | Returns |
|------|-------------|------------|---------|
| `create_collection` | Create a new collection | `collection_name`, optional `description`, `metadata` | Success confirmation |
| `list_collections` | List all collections | None | List of collections with descriptions |
| `delete_collection` | Delete a collection | `collection_name` | Success confirmation |

### Document Versioning Tools

| Tool | Description | Parameters | Returns |
|------|-------------|------------|---------|
| `create_document_version` | Create a new version of a document | `document_id`, `content`, optional `version_note`, `metadata` | Success confirmation with version number |
| `list_document_versions` | List all versions of a document | `document_id` | Version history with timestamps and notes |
| `get_document_version` | Retrieve a specific version of a document | `document_id`, `version` (number or "latest") | Document content and version metadata |

### Error Messages

The server provides clear error messages for common scenarios:
- `Document already exists [id=X]`
- `Document not found [id=X]`
- `Invalid input: Missing document_id or content`
- `Invalid filter`
- `Operation failed: [details]`
- `Collection already exists [name=X]`
- `Collection not found [name=X]`
- `Version X not found for document 'Y'`

## 🛠️ Development

### Interactive Testing

The MCP Inspector provides a web interface for testing server functionality:

```bash
npx @modelcontextprotocol/inspector chroma-mcp
```

For uv installations:

```bash
npx @modelcontextprotocol/inspector uv --directory C:/PATH/TO/YOUR/PROJECT run chroma-mcp
```

### Building the Package

```bash
# Update dependencies
uv compile pyproject.toml

# Build package
uv build
```

## ❓ Troubleshooting

### Common Issues

**Issue**: Server fails to start  
**Solution**: Check Python version (`python --version`), ensure 3.12+ is installed

**Issue**: Document search returns unexpected results  
**Solution**: Verify embedding model is loaded correctly; check query formatting

**Issue**: Cannot connect from AI assistant  
**Solution**: Verify MCP configuration in assistant settings, check server logs for connection attempts

**Issue**: Document versions not appearing  
**Solution**: Ensure you're using the correct document_id and check that versions were created successfully

### Getting Help

If you encounter issues not covered here:
1. Check server logs for detailed error messages
2. Open an issue on the GitHub repository
3. Contact HumainLabs.ai support

## 👥 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on:
- Code style and conventions
- Testing requirements
- Pull request process
- Bug reporting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <p>Maintained with ❤️ by <a href="https://humainlabs.ai">HumainLabs.ai</a></p>
  <p>Built on <a href="https://github.com/chroma-core/chroma">ChromaDB</a> and <a href="https://modelcontextprotocol.ai">Model Context Protocol</a></p>
</div> 