#!/usr/bin/env python3
from scholarly import scholarly, ProxyGenerator
import json
import os
from datetime import datetime, timedelta
import time

CACHE_FILE = "_data/metrics.json"
CACHE_DURATION = timedelta(hours=12)

def create_default_metrics():
    """Create default metrics structure"""
    return {
        'total_citations': 0,
        'h_index': 0,
        'i10_index': 0,
        'papers': [],  # Always include empty papers list
        'updated': datetime.now().isoformat()
    }

def fetch_metrics():
    """Fetch citation metrics from Google Scholar"""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            try:
                cached = json.load(f)
                if 'papers' not in cached:
                    cached['papers'] = []
                return cached
            except json.JSONDecodeError:
                pass
    
    print("Fetching fresh metrics from Google Scholar...")
    try:
        pg = ProxyGenerator()
        pg.FreeProxies()
        scholarly.use_proxy(pg)
        
        # Get author data
        author = next(scholarly.search_author_id('ppDq7_gAAAAJ'))
        author = scholarly.fill(author)
        
        metrics = create_default_metrics()
        metrics.update({
            'total_citations': author.citedby,
            'h_index': author.hindex,
            'i10_index': getattr(author, 'i10index', 0),
        })
        
        # Get paper details
        for pub in author.publications:
            pub_filled = scholarly.fill(pub)
            metrics['papers'].append({
                'title': pub_filled.bib.get('title', ''),
                'year': pub_filled.bib.get('year', 'N/A'),
                'citations': getattr(pub_filled, 'citedby', 0),
                'venue': pub_filled.bib.get('venue', 'N/A')
            })
        
        # Save metrics
        os.makedirs('_data', exist_ok=True)
        with open(CACHE_FILE, 'w') as f:
            json.dump(metrics, f, indent=2)
            
        return metrics
        
    except Exception as e:
        print(f"Error fetching metrics: {str(e)}")
        return create_default_metrics()

if __name__ == "__main__":
    print("Fetching Google Scholar metrics...")
    metrics = fetch_metrics()
    print(f"Total citations: {metrics['total_citations']}")
    print(f"h-index: {metrics['h_index']}")
    print(f"i10-index: {metrics['i10_index']}")
    print(f"Number of papers: {len(metrics['papers'])}")