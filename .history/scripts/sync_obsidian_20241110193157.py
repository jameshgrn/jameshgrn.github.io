#!/usr/bin/env python3
import os
import shutil
import frontmatter
import datetime
from pathlib import Path
import re

OBSIDIAN_PATH = "/Users/jakegearon/GearonWiki/PublicNotes"
SITE_PATH = "_random-musings"

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text).strip('-')
    return text

def get_title_from_content(content):
    """Extract title from Obsidian markdown content"""
    # Try to find a # Title or ## Title at the start
    title_match = re.search(r'^#\s*(.+)$', content, re.MULTILINE)
    if title_match:
        return title_match.group(1).strip()
    
    # If no title found, use filename without extension
    return None

def convert_obsidian_to_jekyll(obsidian_file, jekyll_path):
    """Convert Obsidian markdown to Jekyll format"""
    with open(obsidian_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to get title from content, fallback to filename
    title = get_title_from_content(content) or Path(obsidian_file).stem.replace('-', ' ')
    
    # Create slug from title
    slug = slugify(title)
    
    # Create Jekyll front matter
    post = frontmatter.Post(
        content,
        title=title,
        collection='random-musings',
        permalink=f'/random-musings/{slug}',
        date=datetime.datetime.now().strftime('%Y-%m-%d'),
        layout='single',
        author_profile=True,
        toc=True,
        mathjax=True
    )
    
    # Write to Jekyll site with slugified filename
    output_path = os.path.join(jekyll_path, f"{slug}.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))
    
    print(f"Converted {title} -> {slug}.md")

def main():
    # Create directories
    os.makedirs(SITE_PATH, exist_ok=True)
    
    # Convert all markdown files in PublicNotes
    for file in Path(OBSIDIAN_PATH).glob('*.md'):
        print(f"Converting {file.name}...")
        convert_obsidian_to_jekyll(str(file), SITE_PATH)

if __name__ == "__main__":
    main() 