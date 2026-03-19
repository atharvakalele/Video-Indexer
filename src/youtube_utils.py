import os
import re
import subprocess
import google.generativeai as genai
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

load_dotenv()

def get_video_id(url):
    """Extracts the video ID from a YouTube URL."""
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query)['v'][0]
        if parsed_url.path.startswith(('/embed/', '/v/')):
            return parsed_url.path.split('/')[2]
    return None

def fetch_transcript_text(url):
    """Downloads and cleans the transcript using yt-dlp."""
    # Store temporary transcripts in the 'temp/' directory
    output_dir = os.path.join(os.getcwd(), "temp")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_base = os.path.join(output_dir, "temp_transcript")
    
    # Clean up old files
    for ext in ['srt', 'txt']:
        if os.path.exists(f"{output_base}.en.{ext}"):
            os.remove(f"{output_base}.en.{ext}")
        if os.path.exists(f"{output_base}.{ext}"):
            os.remove(f"{output_base}.{ext}")
            
    try:
        # Get absolute path to yt-dlp in the venv (root/venv/Scripts/yt-dlp.exe)
        # Standard: Root is CWD
        yt_dlp_path = os.path.join(os.getcwd(), "venv", "Scripts", "yt-dlp.exe")
        if not os.path.exists(yt_dlp_path):
             yt_dlp_path = "yt-dlp" # Fallback
             
        # Download auto-generated English subs in srt format
        cmd = [
            yt_dlp_path, "--write-auto-subs", "--sub-format", "srt", 
            "--skip-download", "-o", output_base, url
        ]
        print(f"Running command: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"yt-dlp output length: {len(result.stdout)}")
        
        srt_path = f"{output_base}.en.srt"
        if not os.path.exists(srt_path):
            # Try without .en or other variations
            found = False
            for f in os.listdir(output_dir):
                if f.startswith("temp_transcript") and f.endswith(".srt"):
                    srt_path = os.path.join(output_dir, f)
                    found = True
                    break
            if not found:
                srt_path = ""
            
        print(f"Checking for srt at: {srt_path}")
        if not srt_path or not os.path.exists(srt_path):
            files = ", ".join(os.listdir(output_dir)[:5])
            return f"Error: Could not find downloaded transcript file in temp/. Files in dir: {files}"
            
        with open(srt_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Basic cleanup: Remove timestamps and sequence numbers
        content = re.sub(r'^\d+\s*$', '', content, flags=re.MULTILINE)
        content = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', content)
        content = re.sub(r'<[^>]*>', '', content)
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Deduplicate sequential lines
        clean_lines = []
        for line in lines:
            if not clean_lines or line != clean_lines[-1]:
                clean_lines.append(line)
        
        return " ".join(clean_lines)
    except Exception as e:
        return f"Error fetching transcript: {e}"

def optimize_transcript(text, api_key=None):
    """
    Optimizes the transcript LOCALLY using rules to remove fillers and redundancy.
    Fact-loss is prioritized to be essentially zero.
    """
    # 1. Remove verbal fillers (regex-based)
    fillers = r'\b(um|uh|so|basically|like|you know|right|okay|actually|literally|sort of|kind of|i mean|think|guess|maybe|pretty much)\b'
    text = re.sub(fillers, '', text, flags=re.IGNORECASE)
    
    # 2. Remove stuttering/repeated words (e.g. "we we", "it it")
    text = re.sub(r'\b(\w+)\s+\1\b', r'\1', text, flags=re.IGNORECASE)
    
    # 3. Normalize common wordy phrases
    phrases = {
        r"what we're going to do is": "we will",
        r"what we are going to do is": "we will",
        r"i am going to": "i will",
        r"we are going to": "we will",
        r"let's go ahead and": "let's",
        r"if you look at the": "look at",
        r"as you can see": "",
        r"is that right": "",
        r"does that make sense": "",
    }
    for pattern, replacement in phrases.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    # 4. Remove excessive punctuation/whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    # 5. Clean up any resulting double spaces
    text = re.sub(r'\s{2,}', ' ', text)
    
    return text

def get_playlist_video_urls(playlist_url):
    """Extracts video titles and URLs from a playlist."""
    try:
        cmd = ["yt-dlp", "--get-title", "--get-id", "--flat-playlist", playlist_url]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        lines = result.stdout.strip().split('\n')
        
        videos = []
        for i in range(0, len(lines), 2):
            if i + 1 < len(lines):
                videos.append({
                    "title": lines[i],
                    "video_id": lines[i+1],
                    "url": f"https://www.youtube.com/watch?v={lines[i+1]}"
                })
        return videos
    except Exception as e:
        print(f"Error fetching playlist: {e}")
        return []
