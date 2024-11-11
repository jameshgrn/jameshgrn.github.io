#!/usr/bin/env python3
import os
import frontmatter
import datetime
from pathlib import Path
import re

OBSIDIAN_PATH = "/Users/jakegearon/GearonWiki/PublicNotes"
SITE_PATH = "_random-musings"
MUSINGS_INDEX = "_pages/random-musings.md"

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text).strip('-')
    return text

def get_title_from_content(content, filename):
    """Extract title from Obsidian markdown content or use filename"""
    # Try to find a top-level heading (# Title)
    title_match = re.search(r'^#\s+([^#\n]+)', content, re.MULTILINE)
    if title_match:
        return title_match.group(1).strip()
    
    # If no title found, use filename without extension
    return Path(filename).stem.replace('-', ' ')

def convert_obsidian_to_jekyll(obsidian_file, jekyll_path):
    """Convert Obsidian markdown to Jekyll format"""
    with open(obsidian_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get title from content or filename
    title = get_title_from_content(content, obsidian_file)
    
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
    
    print(f"Converted '{title}' -> {slug}.md")
    return title, slug

def update_index_page(converted_files):
    """Update the random-musings index page with current files"""
    # Read the template parts
    with open(MUSINGS_INDEX, 'r') as f:
        content = f.read()
    
    # Split content at the "Current Notes" section
    parts = content.split("## Current Notes")
    if len(parts) != 2:
        print("Warning: Could not find '## Current Notes' section in index page")
        return
    
    header = parts[0] + "## Current Notes\n\n"
    
    # Group files by category
    math_physics = []
    meta_writing = []
    
    for title, slug in converted_files:
        if any(kw in title.lower() for kw in ['derivation', 'analysis', 'algorithm', 'equation']):
            math_physics.append((title, slug))
        else:
            meta_writing.append((title, slug))
    
    # Build the new content
    new_content = header
    new_content += "### Mathematical & Physical Models\n"
    for title, slug in math_physics:
        new_content += f"- [{title}](/random-musings/{slug})\n"
    
    new_content += "\n### Meta & Writing\n"
    for title, slug in meta_writing:
        new_content += f"- [{title}](/random-musings/{slug})\n"
    
    new_content += "\n---\n\n"
    new_content += "I believe in working in public and sharing ideas early, even if they're not fully formed. Feel free to explore, but approach with appropriate skepticism!\n\n"
    new_content += "*Want to learn more about digital gardens? Check out [this article](https://maggieappleton.com/garden-history) by Maggie Appleton.*"
    
    # Write the updated index
    with open(MUSINGS_INDEX, 'w') as f:
        f.write(new_content)
    
    print("Updated random-musings index page")

def main():
    # Create directories
    os.makedirs(SITE_PATH, exist_ok=True)
    
    # Convert all markdown files and keep track of them
    converted_files = []
    for file in Path(OBSIDIAN_PATH).glob('*.md'):
        print(f"Converting {file.name}...")
        title, slug = convert_obsidian_to_jekyll(str(file), SITE_PATH)
        converted_files.append((title, slug))
    
    # Update the index page
    update_index_page(converted_files)

if __name__ == "__main__":
    main() 