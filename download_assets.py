import os
import re
import urllib.request
import urllib.error

BASE_URL = "https://www.247freepoker.com"

# 1. Site images
site_images = [
    "images/247/favicon.ico",
    "images/247/title.webp",
    "images/247/title.png",
    "images/close.webp",
    "images/close.png",
    "images/247/slice.webp",
    "images/247/slice.png",
    "images/247/thumbs_bg.webp",
    "images/247/thumbs_bg.png",
    "images/how-to-play/freepoker-preflop.png",
    "images/how-to-play/freepoker-flop.png",
    "images/how-to-play/freepoker-turn.png",
    "images/how-to-play/freepoker-river.png",
    "images/how-to-play/freepoker-example.png",
    "images/how-to-play/freepoker-deal.png",
    "images/how-to-play/freepoker-betting.png",
    "images/how-to-play/freepoker-flop-example.png",
    "images/how-to-play/freepoker-turn-example.png",
    "images/how-to-play/freepoker-river-example.png",
    "images/how-to-play/freepoker-showdown.png",
]

# 2. Game assets from game.js
with open("game/js/game.js") as f:
    game_js = f.read()

game_assets = re.findall(r'\{src:"([^"]+)"', game_js)

print(f"Total site images to fetch: {len(site_images)}")
print(f"Total game assets to fetch: {len(game_assets)}")

def fetch_file(url, local_path):
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        return True
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(local_path, "wb") as f:
                f.write(data)
        print(f"OK ({len(data)}b): {local_path}")
        return True
    except Exception as e:
        print(f"FAILED {url} -> {local_path}: {e}")
        return False

# Download site images
print("\n--- Downloading Site Images ---")
for img in site_images:
    url = f"{BASE_URL}/{img}"
    fetch_file(url, img)

# Download game assets (under game/)
print("\n--- Downloading Game Assets ---")
for asset in game_assets:
    url = f"{BASE_URL}/game/{asset}"
    local_path = os.path.join("game", asset)
    fetch_file(url, local_path)

# Download external link icons
print("\n--- Downloading External Link Icons ---")
with open("original_index.html") as f:
    orig_html = f.read()

ext_links = set(re.findall(r'https://www\.247games\.com/link-assets/[^\s"\'\<\>]+', orig_html))
print(f"Found {len(ext_links)} external link asset URLs")

for url in sorted(ext_links):
    rel_path = url.replace("https://www.247games.com/", "")
    fetch_file(url, rel_path)

print("\nDone downloading all assets!")
