import sys
from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse as urlparse

def get_video_id(url):
    url_data = urlparse.urlparse(url)
    query = urlparse.parse_qs(url_data.query)
    v = query.get("v")
    if v: return v[0]
    if "youtu.be" in url_data.netloc: return url_data.path.lstrip("/")
    return None

def fetch_transcript(video_id):
    # Try common library methods
    methods = ["get_transcript", "list_transcripts"]
    for method_name in methods:
        if hasattr(YouTubeTranscriptApi, method_name):
            method = getattr(YouTubeTranscriptApi, method_name)
            try:
                if method_name == "get_transcript":
                    transcript_list = method(video_id)
                    return " ".join([t['text'] for t in transcript_list])
                elif method_name == "list_transcripts":
                    transcript_list = method(video_id).find_transcript(['en']).fetch()
                    return " ".join([t['text'] for t in transcript_list])
            except Exception as e:
                print(f"Method {method_name} failed: {e}")
    return "Could not find a working method to fetch transcript."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_transcript.py <youtube_url>")
        sys.exit(1)
    
    url = sys.argv[1]
    video_id = get_video_id(url)
    if not video_id:
        print("Could not extract video ID from URL.")
        sys.exit(1)
        
    transcript = fetch_transcript(video_id)
    print(transcript)
