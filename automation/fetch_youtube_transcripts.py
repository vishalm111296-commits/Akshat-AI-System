#!/usr/bin/env python3
"""
fetch_youtube_transcripts.py
Detects new Akshat Shrivastava YouTube videos via RSS and downloads transcripts.
No paid API required. Uses youtube-transcript-api + feedparser.
"""

import os
import json
from datetime import datetime

try:
    from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
    import feedparser
except ImportError:
    print("Run: pip install -r automation/requirements.txt")
    exit(1)

# Akshat Shrivastava YouTube channel RSS
CHANNEL_RSS = "https://www.youtube.com/feeds/videos.xml?channel_id=UCfU6El0eOFtDMwq24BoMpxQ"
TRANSCRIPTS_DIR = "raw_sources/youtube_transcripts"
SEEN_FILE = ".automation_state/seen_videos.json"

os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)
os.makedirs(".automation_state", exist_ok=True)


def load_seen():
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE) as f:
            return json.load(f)
    return {}


def save_seen(seen):
    with open(SEEN_FILE, "w") as f:
        json.dump(seen, f, indent=2)


def get_new_videos(seen):
    feed = feedparser.parse(CHANNEL_RSS)
    return [
        entry for entry in feed.entries
        if entry.get("yt_videoid") and entry["yt_videoid"] not in seen
    ]


def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join(t["text"] for t in transcript)
    except (TranscriptsDisabled, NoTranscriptFound):
        return None
    except Exception as e:
        print(f"  Error fetching {video_id}: {e}")
        return None


def save_transcript(video, text):
    pub_date = video.get("published", "")[:10].replace("-", "-")
    vid_id = video["yt_videoid"]
    title_slug = "".join(
        c if c.isalnum() else "-"
        for c in video.get("title", "untitled").lower()
    )[:40].strip("-")
    filename = f"YT-{pub_date}-{title_slug}-{vid_id}.txt"
    filepath = os.path.join(TRANSCRIPTS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {video.get('title', 'Unknown Title')}\n")
        f.write(f"# Published: {video.get('published', 'Unknown')}\n")
        f.write(f"# VideoID: {vid_id}\n")
        f.write(f"# URL: https://www.youtube.com/watch?v={vid_id}\n")
        f.write(f"# Ingested: {datetime.now().isoformat()}\n\n")
        f.write(text)
    print(f"  Saved: {filename}")
    return filename


def main():
    print("[fetch_youtube_transcripts] Starting...")
    seen = load_seen()
    new_videos = get_new_videos(seen)
    print(f"  Found {len(new_videos)} new video(s).")

    fetched = []
    for video in new_videos:
        vid_id = video["yt_videoid"]
        title = video.get("title", "Unknown")
        print(f"  Processing: {title} ({vid_id})")
        text = fetch_transcript(vid_id)
        if text:
            filename = save_transcript(video, text)
            fetched.append(filename)
            seen[vid_id] = {
                "title": title,
                "published": video.get("published", ""),
                "ingested": datetime.now().isoformat(),
                "file": filename
            }
        else:
            print(f"  No transcript available for: {title}")
            seen[vid_id] = {"title": title, "status": "no_transcript"}

    save_seen(seen)
    print(f"[fetch_youtube_transcripts] Done. Fetched {len(fetched)} transcript(s).")
    return fetched


if __name__ == "__main__":
    main()
