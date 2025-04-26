import json
from pathlib import Path
#Template for importing json format data

raw_folder = Path("../data/raw")
json_files = sorted(raw_folder.glob("*.json"))

def load_web_highlights(json_path):
    #Use the with open() function to open a file and then use 
    # read() or readlines() to read the data into a variable value.
    # You should use the mode of r so that the file will be opened as 
    # read only and you do not accidentally overwrite it.
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def example_usage():
    sample_file = Path("../data/web_highlights.json")
    highlights = load_web_highlights(sample_file)
    print(highlights[:2])  # Just preview a few items
    
    
#export json file of processed ID's    

if __name__ == "__main__":
    example_usage()
