import os
import asyncio
from mcp.server.fastmcp import FastMCP
from youtube_utils import fetch_transcript_text, optimize_transcript, get_playlist_video_urls
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create an MCP server
mcp = FastMCP("Video Indexer")

@mcp.tool()
def get_video_topics(url: str) -> str:
    """
    Fetches the transcript of a YouTube video, optimizes it locally 
    (token-efficient, lossless), and returns the factual content.
    
    Args:
        url: The full URL of the YouTube video.
    """
    print(f"Fetching transcript for: {url}")
    raw_transcript = fetch_transcript_text(url)
    
    if raw_transcript.startswith("Error"):
        return raw_transcript
        
    print("Optimizing transcript locally (Lossless)...")
    optimized_text = optimize_transcript(raw_transcript)
    
    return f"--- LOCAL OPTIMIZED TRANSCRIPT ---\n\n{optimized_text}"

@mcp.tool()
def get_playlist_details(url: str) -> str:
    """
    Retrieves the list of video titles and URLs from a YouTube playlist.
    
    Args:
        url: The full URL of the YouTube playlist.
    """
    print(f"Fetching details for playlist: {url}")
    videos = get_playlist_video_urls(url)
    
    if not videos:
        return "Error: Could not retrieve any videos from the playlist. Please check the URL."
        
    result = "### Playlist Videos:\n\n"
    for v in videos:
        result += f"- **{v['title']}**: {v['url']}\n"
    
    return result

if __name__ == "__main__":
    # Standard MCP server runner
    mcp.run()
