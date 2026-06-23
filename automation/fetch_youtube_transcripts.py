#!/usr/bin/env python3
"""
fetch_youtube_transcripts.py
Detects new Akshat Shrivastava YouTube videos via RSS and downloads transcripts.
No paid API required. Uses youtube-transcript-api + feedparser.

NOTE: If transcript fetching fails (YouTube bot protection, no transcript available),
the script exits with code 0 (non-fatal) so the CI pipeline continues.
"""

import os
import json
import sys
from datetime import datetime

try:
    from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
    import feedparser
except ImportError:
    print("[fetch] ERROR: Missing dependencies. Run: pip install -r automation/requirements.txt")
    sys.exit(0)  # Non-fatal: pipeline continues without transcript fetch


def get_channel_id():
    try:
        import yaml
        cfg_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                "operating_system", "config.yaml")
        with open(cfg_path) as f:
            cfg = yaml.safe_load(f)
        return cfg["automation"]["youtube_channel_id"]
    except Exception as e:
        print(f"[fetch] WARNING: Could not read config.yaml ({e}). Using fallback channel ID.")
        return "UCfU6El0eOFtDMwq24BoMpxQ"  # Akshat Shrivastava -- fallback only


CHANNEL_ID = get_channel_id()
CHANNEL_RSS = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
TRANSCRIPTS_DIR = "raw_sources/youtube_transcripts"
SEEN_FILE = ".automation_state/seen_videos.json"

os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)
os.makedirs(".automation_state", exist_ok=True)


def load_seen():
    if os.path.exists(SEEN_FILE):
        try:
            with open(SEEN_FILE) as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("[fetch] WARNING: seen_videos.json is corrupt. Resetting.")
            return {}
    return {}


def save_seen(seen):
    tmp = SEEN_FILE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(seen, f, indent=2)
    os.replace(tmp, SEEN_FILE)


def get_new_videos(seen):
    print(f"[fetch] Fetching RSS: {CHANNEL_RSS}")
    try:
        feed = feedparser.parse(CHANNEL_RSS)
    except Exception as e:
        print(f"[fetch] WARNING: Could not fetch RSS feed: {e}. Skipping.")
        return []
    if not feed.entries:
        print("[fetch] WARNING: RSS feed returned 0 entries. Channel may be private or RSS unavailable.")
        return []
    new = [
        entry for entry in feed.entries
        if entry.get("yt_videoid") and entry["yt_videoid"] not in seen
    ]
    print(f"[fetch] RSS returned {len(feed.entries)} total entries, {len(new)} unseen.")
    return new


def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'en-IN', 'hi'])
        return " ".join(t["text"] for t in transcript)
    except (TranscriptsDisabled, NoTranscriptFound):
        return None
    except Exception as e:
        print(f"[fetch] WARNING: Could not fetch transcript for {video_id}: {e}")
        return None


def save_transcript(video, text):
    pub_raw = video.get("published", "")[:10]
    pub_date = pub_raw if pub_raw else datetime.now().strftime("%Y-%m-%d")
    vid_id = video["yt_videoid"]
    title_slug = "".join(
        c if c.isalnum() else "-"
        for c in video.get("title", "untitled").lower()
    )[:40].strip("-")
    filename = f"YT-{pub_date}-{title_slug}-{vid_id}.txt"
    filepath = os.path.join(TRANSCRIPTS_DIR, filename)
    tmp = filepath + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(f"# {video.get('title', 'Unknown Title')}\n")
        f.write(f"# Published: {video.get('published', 'Unknown')}\n")
        f.write(f"# VideoID: {vid_id}\n")
        f.write(f"# URL: https://www.youtube.com/watch?v={vid_id}\n")
        f.write(f"# Ingested: {datetime.now().isoformat()}\n")
        f.write(f"# SourceType: YOUTUBE_TRANSCRIPT\n")
        f.write(f"# ChannelID: {CHANNEL_ID}\n\n")
        f.write(text)
    os.replace(tmp, filepath)
    print(f"[fetch] Saved: {filename} ({len(text)} chars)")
    return filename


def main():
    print(f"[fetch_youtube_transcripts] Started: {datetime.now().isoformat()}")
    print(f"[fetch] Channel ID: {CHANNEL_ID}")
    seen = load_seen()
    print(f"[fetch] Previously seen videos: {len(seen)}")
    new_videos = get_new_videos(seen)

    if not new_videos:
        print("[fetch_youtube_transcripts] No new videos found. Exiting cleanly.")
        save_seen(seen)
        return []

    fetched = []
    no_transcript = []
    for video in new_videos:
        vid_id = video["yt_videoid"]
        title = video.get("title", "Unknown")
        print(f"[fetch] Processing: {title} ({vid_id})")
        text = fetch_transcript(vid_id)
        if text:
            filename = save_transcript(video, text)
            fetched.append(filename)
            seen[vid_id] = {
                "title": title,
                "published": video.get("published", ""),
                "ingested": datetime.now().isoformat(),
                "file": filename,
                "status": "fetched"
            }
        else:
            print(f"[fetch] No transcript available: {title}")
            no_transcript.append(vid_id)
            seen[vid_id] = {
                "title": title,
                "published": video.get("published", ""),
                "status": "no_transcript",
                "checked": datetime.now().isoformat()
            }

    save_seen(seen)
    print(f"[fetch_youtube_transcripts] Done.")
    print(f"  Fetched transcripts: {len(fetched)}")
    print(f"  No transcript available: {len(no_transcript)}")
    print(f"  Total seen (cumulative): {len(seen)}")
    return fetched


if __name__ == "__main__":
    main()
