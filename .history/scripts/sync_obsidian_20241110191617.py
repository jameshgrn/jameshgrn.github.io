#!/usr/bin/env python3
import os
import frontmatter
import datetime
from pathlib import Path

# Paths
OBSIDIAN_PATH = "/Users/jakegearon/GearonWiki/PublicNotes"
SITE_PATH = "_random-musings"

def convert_obsidian_to_jekyll(obsidian_file, jekyll_path):
    """Convert Obsidian markdown to Jekyll format"""
    with open(obsidian_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title from filename
    title = Path(obsidian_file).stem.replace('-', ' ')
    
    # Create Jekyll front matter
    post = frontmatter.Post(
        content,
        title=title,
        collection='random-musings',
        permalink=f'/random-musings/{Path(obsidian_file).stem.lower()}',
        date=datetime.datetime.now().strftime('%Y-%m-%d'),
        layout='single',
        author_profile=True,
        toc=True,
        mathjax=True
    )
    
    # Write to Jekyll site
    output_path = os.path.join(jekyll_path, f"{Path(obsidian_file).stem.lower()}.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))

def main():
    os.makedirs(SITE_PATH, exist_ok=True)
    
    # Process all markdown files in the PublicNotes directory
    for file in Path(OBSIDIAN_PATH).glob('*.md'):
        print(f"Converting {file.name}...")
        convert_obsidian_to_jekyll(str(file), SITE_PATH)

if __name__ == "__main__":
    main() 