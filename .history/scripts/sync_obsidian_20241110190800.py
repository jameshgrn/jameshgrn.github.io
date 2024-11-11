#!/usr/bin/env python3
import os
import shutil
import frontmatter
import datetime
from pathlib import Path

# Paths
OBSIDIAN_PATH = "/Users/jakegearon/GearonWiki/Zettelkasten"
SITE_PATH = "_random-musings"

def convert_obsidian_to_jekyll(obsidian_file, jekyll_path):
    """Convert Obsidian markdown to Jekyll format"""
    
    # Read the original file
    with open(obsidian_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create Jekyll front matter
    title = Path(obsidian_file).stem.replace('-', ' ')
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # Create Jekyll file
    post = frontmatter.Post(
        content,
        title=title,
        collection='random-musings',
        permalink=f'/random-musings/{Path(obsidian_file).stem.lower()}',
        date=date,
        layout='single',
        author_profile=True,
        toc=True,
        mathjax=True  # Enable math rendering
    )
    
    # Write the Jekyll file
    output_path = os.path.join(jekyll_path, f"{Path(obsidian_file).name}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))

def main():
    # Create _random-musings directory if it doesn't exist
    os.makedirs(SITE_PATH, exist_ok=True)
    
    # List of files to sync
    files_to_sync = [
        "The Semantic Mirror Effect.md",
        "Derivation of Exponential Decay in Moran's I for River Planforms and its Diffusive Interpretation.md",
        "A dimensionless analysis of the shear stress ratio on an alluvial ridge.md",
        "Derivation of Softmax Random Walk Algorithm.md"
    ]
    
    # Convert each file
    for filename in files_to_sync:
        obsidian_file = os.path.join(OBSIDIAN_PATH, filename)
        if os.path.exists(obsidian_file):
            print(f"Converting {filename}...")
            convert_obsidian_to_jekyll(obsidian_file, SITE_PATH)
        else:
            print(f"Warning: {filename} not found in Obsidian vault")

if __name__ == "__main__":
    main() 