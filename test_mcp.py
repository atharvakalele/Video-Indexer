import os
from youtube_mcp_server import get_video_topics
from dotenv import load_dotenv

load_dotenv()

def test():
    video_url = "https://youtu.be/2DD-ynCIZ4w?si=--cykyu34s053eWE"
    print(f"Testing get_video_topics for: {video_url}")
    
    try:
        result = get_video_topics(video_url)
        print("\n--- RESULTS ---\n")
        print(result)
        print(f"\nTotal length: {len(result)}")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    test()
