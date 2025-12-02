import re
import sys
import json

files = ["branding_iron.html", "golf_stamp.html", "cowboy_hat.html", "pet_tag.html"]

for f in files:
    print(f"--- {f} ---")
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            # Find image URLs that look like product images (often in a list or gallery)
            # Look for larger versions if possible, usually ending in .jpg without _100x etc if possible, or just the base ID
            
            # Regex for fantaskycdn images
            matches = re.findall(r'img\.fantaskycdn\.com/([a-f0-9]{32})', content)
            
            unique_ids = []
            seen = set()
            for m in matches:
                if m not in seen:
                    seen.add(m)
                    unique_ids.append(m)
            
            for i, img_id in enumerate(unique_ids[:15]):
                 print(f"https://img.fantaskycdn.com/{img_id}.jpg")

    except Exception as e:
        print(f"Error reading {f}: {e}")

