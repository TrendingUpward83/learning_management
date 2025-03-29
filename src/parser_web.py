import json
from pathlib import Path

def load_web_highlights(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def example_usage():
    sample_file = Path("../data/web_highlights.json")
    highlights = load_web_highlights(sample_file)
    print(highlights[:2])  # Just preview a few items

if __name__ == "__main__":
    example_usage()
