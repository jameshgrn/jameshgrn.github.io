#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

OBSIDIAN_PATH = "/Users/jakegearon/GearonWiki/PublicNotes"
SITE_PATH = "_random-musings"

def sync_files():
    """Simply copy markdown files from Obsidian to site directory"""
    os.makedirs(SITE_PATH, exist_ok=True)
    
    # First clean the destination directory
    for file in Path(SITE_PATH).glob('*.md'):
        file.unlink()
    
    # Copy all markdown files
    for file in Path(OBSIDIAN_PATH).glob('*.md'):
        dest_file = Path(SITE_PATH) / file.name
        print(f"Copying {file.name} to {dest_file}")
        shutil.copy2(file, dest_file)

def main():
    print("Syncing Obsidian notes...")
    sync_files()
    print("Done!")

if __name__ == "__main__":
    main()