# YouTube Transcript & Topic Extractor MCP Server

A high-performance, token-efficient MCP server designed to extract technical topics and full transcripts from YouTube videos. Optimized for large-scale indexing (e.g., Selenium playlists) with local pre-processing to minimize LLM token usage.

## Features
- **FastMCP Integration**: Connects seamlessly with Claude Desktop or any MCP client.
- **Lossless Optimization**: Local heuristic cleaning removes verbal fillers and fluff without losing technical facts.
- **Playlist Scanning**: Analyzes entire playlists to gather session details.
- **Selenium Study Guide**: Included `index.md` with 300+ questions covering a complete Selenium 4 course.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd Selenium
   ```

2. **Set up Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure API Key**:
   Create a `.env` file:
   ```env
   GEMINI_API_KEY=your_key_here
   ```

## Usage

### Registering with Claude Desktop
Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "youtube-transcript": {
      "command": "C:\\path\\to\\python.exe",
      "args": ["C:\\path\\to\\youtube_mcp_server.py"],
      "env": {
        "PYTHONPATH": "C:\\path\\to\\project"
      }
    }
  }
}
```

### Key Files
- `youtube_mcp_server.py`: Main MCP server entry point.
- `youtube_utils.py`: Core logic for fetching and optimizing transcripts.
- `index.md`: The generated Selenium study guide.

## License
MIT
