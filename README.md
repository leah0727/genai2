# spring2026-genai2
# 📚 Course-Assistant-RAG & MCP Integration
## Workflow Overview

- The user submits a query through Claude Desktop.  
- Claude calls the MCP tool exposed by the local Python server.  
- The MCP server queries ChromaDB for relevant document embeddings.  
- Retrieved context is returned to the AI client.  
- The LLM (Gemini 2.0 Flash) synthesizes a final answer using the retrieved knowledge.

---

## 🛠️ Technical Comparison

This project improves upon traditional RAG architectures by introducing agent-based interoperability through MCP.

| Feature | Traditional RAG | This Project (RAG + MCP) |
|---|---|---|
| Data Access | Requires manual file uploads | Persistent connection to a local database |
| Agent Integration | Works only inside dedicated apps | Integrates with external AI agents (e.g., Claude Desktop) |
| Technology Standard | Isolated API calls | Standardized MCP protocol |
| Data Security | Data often sent to cloud services | Local storage ensures privacy |

---

## 🧠 Reasoning & Pipeline Logic

The system processes user queries through a four-stage pipeline.

| Stage | Name | Description |
|---|---|---|
| 1 | Ingestion | Documents (PDFs, lecture notes) are split into semantic chunks and converted into vector embeddings |
| 2 | Retrieval | Semantic similarity search retrieves the most relevant text using cosine similarity |
| 3 | Augmentation | Retrieved passages are injected into the prompt as contextual knowledge |
| 4 | MCP Orchestration | The MCP server exposes the retrieval pipeline as a tool accessible by AI agents |

---

## 🚀 Setup & Installation

### 1. Requirements

- Python 3.12+ (Conda environment recommended)
- Claude Desktop installed

### 2. Dependencies

```bash
pip install mcp langchain-chroma langchain-google-genai streamlit
```

## ⚙️ MCP Configuration

Add the following configuration to:

`~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "course-assistant": {
      "command": "/Users/nayeong-eun/anaconda3/envs/mendel/bin/python",
      "args": ["/Users/nayeong-eun/Desktop/genai2/mcp_server.py"],
      "env": {
        "GOOGLE_API_KEY": "YOUR_API_KEY_HERE",
        "PYTHONPATH": "/Users/nayeong-eun/anaconda3/envs/mendel/lib/python3.12/site-packages"
      }
    }
  }
}
```
## ▶️ Running the System
### Web Interface
```
streamlit run app.py
```

### Agent Integration

- Restart Claude Desktop
- Check the plugin icon in the top-right corner
- The MCP tool should appear as course-assistant

## 📑 Project Notes
### ⚡ Performance

The system uses Gemini 2.0 Flash, allowing fast responses while staying within the free-tier API limits.

### 📈 Scalability

ChromaDB indexing enables efficient retrieval even as the document collection grows.

### 🔒 Security

API keys are managed via environment variables, preventing accidental exposure.

## 💡 Key Idea

By combining RAG with MCP, this project transforms a traditional knowledge retrieval system into a tool accessible by AI agents, enabling seamless interaction between personal data and modern AI assistants.
