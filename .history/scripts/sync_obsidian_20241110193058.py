#!/usr/bin/env python3
import os
import shutil
import frontmatter
from pathlib import Path

OBSIDIAN_PATH = "/Users/jakegearon/GearonWiki/Zettelkasten"
PUBLIC_PATH = "/Users/jakegearon/GearonWiki/PublicNotes"
SITE_PATH = "_random-musings"

# List of files to sync
FILES_TO_SYNC = [
    "Universal Scaling of Topographic Memory.md",
    "Derivation of Exponential Decay in Moran's I for River Planforms and its Diffusive Interpretation.md",
    "A dimensionless analysis of the shear stress ratio on an alluvial ridge.md",
    "Derivation of Softmax Random Walk Algorithm.md",
    "The Semantic Mirror Effect.md",
    "science writing prompt.md"
]

def copy_to_public(filename):
    """Copy file from Zettelkasten to PublicNotes"""
    src = os.path.join(OBSIDIAN_PATH, filename)
    dst = os.path.join(PUBLIC_PATH, filename)
    if os.path.exists(src):
        os.makedirs(PUBLIC_PATH, exist_ok=True)
        shutil.copy2(src, dst)
        return True
    return False

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
    # Create directories
    os.makedirs(PUBLIC_PATH, exist_ok=True)
    os.makedirs(SITE_PATH, exist_ok=True)
    
    # Copy files to public directory
    for filename in FILES_TO_SYNC:
        if copy_to_public(filename):
            print(f"Copied {filename} to PublicNotes")
    
    # Convert files to Jekyll format
    for file in Path(PUBLIC_PATH).glob('*.md'):
        print(f"Converting {file.name} to Jekyll format...")
        convert_obsidian_to_jekyll(str(file), SITE_PATH)

if __name__ == "__main__":
    main() 