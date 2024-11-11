#!/usr/bin/env python3
import os
import frontmatter
from pathlib import Path
import re
import shutil

OBSIDIAN_PATH = "/Users/jakegearon/GearonWiki/PublicNotes"
SITE_PATH = "_random-musings"

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text).strip('-')
    return text

def fix_math_rendering(content):
    """Fix math rendering by ensuring proper delimiters"""
    # First, protect any escaped dollar signs
    content = content.replace(r'\$', 'ESCAPED_DOLLAR_SIGN')
    
    # Handle specific math patterns first
    special_patterns = [
        (r'\\beta = \\frac{H_r}{H_c}', r'$\beta = \frac{H_r}{H_c}$'),
        (r'\\gamma = \\frac{S_r}{S_c}', r'$\gamma = \frac{S_r}{S_c}$'),
        (r'\\tau_c = \\rho g H_c S_c', r'$\tau_c = \rho g H_c S_c$'),
        (r'\\tau_r = \\rho g H_r S_r', r'$\tau_r = \rho g H_r S_r$'),
        (r'H_r = \\beta H_c', r'$H_r = \beta H_c$'),
        (r'S_r = \\gamma S_c', r'$S_r = \gamma S_c$'),
    ]
    
    for pattern, replacement in special_patterns:
        content = content.replace(pattern, replacement)
    
    # Keep single $ for inline math - don't modify them
    # Just ensure they're properly spaced
    content = re.sub(r'(?<=[^\s])\$', r' $', content)  # Add space before $
    content = re.sub(r'\$(?=[^\s])', r'$ ', content)   # Add space after $
    
    # Handle display math with double $$
    content = re.sub(r'\$\$\s*(.*?)\s*\$\$', r'$$\n\1\n$$', content, flags=re.DOTALL)
    
    # Fix specific LaTeX commands - don't add extra $
    latex_commands = [
        r'\beta', r'\gamma', r'\tau', r'\frac', r'\cdot', 
        r'\Delta', r'\Omega', r'\rho', r'\equiv', r'\tag',
        r'\vho', r'\cdot', r'\equiv', r'\tag', r'\rho',
    ]
    
    # Keep LaTeX commands intact
    for cmd in latex_commands:
        content = content.replace(cmd, cmd)
    
    # Restore escaped dollar signs
    content = content.replace('ESCAPED_DOLLAR_SIGN', r'\$')
    
    return content

def get_title_from_content(content, filename):
    """Extract first heading from Obsidian markdown content or use filename"""
    for match in re.finditer(r'^#\s+(.+)$', content, re.MULTILINE):
        title = match.group(1).strip()
        if title.lower() != 'references' and not title.startswith('{{'):
            return title
    
    filename_title = Path(filename).stem
    return filename_title.replace('-', ' ').title()

def is_public_note(content):
    """Check if note should be public based on frontmatter"""
    try:
        post = frontmatter.loads(content)
        # Check for explicit privacy setting in frontmatter
        if 'private' in post.metadata:
            return not post.metadata['private']
        # Check for private tag
        if 'tags' in post.metadata:
            if 'private' in post.metadata['tags']:
                return False
        return True
    except:
        # If no frontmatter, assume public
        return True

def convert_obsidian_to_jekyll(obsidian_file, jekyll_path):
    """Convert Obsidian markdown to Jekyll format"""
    with open(obsidian_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if note should be public
    if not is_public_note(content):
        print(f"Skipping private note: {obsidian_file}")
        return None, None
    
    # Fix math rendering
    content = fix_math_rendering(content)
    
    # Get title
    title = get_title_from_content(content, obsidian_file)
    slug = slugify(title)
    
    # Create Jekyll front matter
    post = frontmatter.Post(
        content,
        title=title,
        layout='single',
        permalink=f'/random-musings/{slug}',
        author_profile=True,
        toc=True,
        toc_sticky=True,
        mathjax=True,
        classes=['wide']
    )
    
    # Write to Jekyll site
    output_path = os.path.join(jekyll_path, f"{slug}.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))
    
    print(f"Converted '{title}' -> {slug}.md")
    return title, slug

def update_index_page(converted_files):
    """Update the random musings index page with the latest files"""
    index_content = """---
layout: single
title: "Random Musings"
permalink: /random-musings/
author_profile: true
---

# Open Notes & Ideas

This is a collection of notes, ideas, and work-in-progress thoughts from my [Obsidian](https://obsidian.md) vault. These documents are often drafted and refined with the help of Large Language Models (LLMs).

⚠️ **Note**: These are living documents that I work on publicly. They may contain:
- Incomplete thoughts
- Work-in-progress ideas
- Potential inaccuracies

## Current Notes

"""
    # Group files by category based on content/title
    math_physics = []
    meta_writing = []
    other = []
    
    for title, slug in converted_files:
        link = f"- [{title}](/random-musings/{slug})"
        if any(kw in title.lower() for kw in ['analysis', 'derivation', 'equation', 'model']):
            math_physics.append(link)
        elif any(kw in title.lower() for kw in ['writing', 'semantic', 'testing', 'resistance']):
            meta_writing.append(link)
        else:
            other.append(link)
    
    if math_physics:
        index_content += "\n### Mathematical & Physical Models\n" + "\n".join(math_physics)
    if meta_writing:
        index_content += "\n\n### Meta & Writing\n" + "\n".join(meta_writing)
    if other:
        index_content += "\n\n### Other Notes\n" + "\n".join(other)
    
    index_content += "\n\n---\n\nI believe in working in public and sharing ideas early. Feel free to explore!"
    
    # Write the index page
    with open("_pages/random-musings.md", 'w', encoding='utf-8') as f:
        f.write(index_content)

def main():
    # Clean up existing files
    if os.path.exists(SITE_PATH):
        shutil.rmtree(SITE_PATH)
    os.makedirs(SITE_PATH, exist_ok=True)
    
    converted_files = []
    for file in Path(OBSIDIAN_PATH).glob('*.md'):
        print(f"\nProcessing {file.name}...")
        title, slug = convert_obsidian_to_jekyll(str(file), SITE_PATH)
        if title and slug:
            converted_files.append((title, slug))
    
    if converted_files:
        print(f"\nSuccessfully converted {len(converted_files)} files:")
        for title, slug in converted_files:
            print(f"- {title} -> {slug}.md")
        
        # Update the index page
        update_index_page(converted_files)
        print("\nUpdated random-musings index page")
    else:
        print("\nNo files were converted.")

if __name__ == "__main__":
    main()