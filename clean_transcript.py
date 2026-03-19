import re
import os

def clean_srt(filepath):
    if not os.path.exists(filepath):
        print(f"File {filepath} not found.")
        return None
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove SRT sequence numbers
    content = re.sub(r'^\d+\s*$', '', content, flags=re.MULTILINE)
    # Remove SRT timestamps (00:00:00,000 --> 00:00:00,000)
    content = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', content)
    # Remove HTML tags if any (sometimes present in auto-subs)
    content = re.sub(r'<[^>]*>', '', content)
    # Remove empty lines and normalize spaces
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    
    # Optional: deduplicate concurrent lines (common in auto-generated subs)
    clean_lines = []
    for line in lines:
        if not clean_lines or line != clean_lines[-1]:
            clean_lines.append(line)
            
    return " ".join(clean_lines)

if __name__ == "__main__":
    srt_file = "transcript.en.srt"
    text = clean_srt(srt_file)
    if text:
        with open("transcript_clean.txt", "w", encoding='utf-8') as f:
            f.write(text)
        print("Transcript cleaned and saved to transcript_clean.txt")
