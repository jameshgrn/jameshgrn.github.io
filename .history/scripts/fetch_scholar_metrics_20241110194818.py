#!/usr/bin/env python3
from scholarly import scholarly, ProxyGenerator
import json
import os
from datetime import datetime

def fetch_metrics():
    """Fetch citation metrics from Google Scholar"""
    try:
        # Set up proxy to avoid rate limiting
        pg = ProxyGenerator()
        success = pg.FreeProxies()
        scholarly.use_proxy(pg)
        
        # Search for your profile using ID
        author = scholarly.search_author_id('ppDq7_gAAAAJ')
        
        # Fill the author data
        author = scholarly.fill(author)
        
        metrics = {
            'total_citations': author.get('citedby', 0),
            'h_index': author.get('hindex', 0),
            'i10_index': author.get('i10index', 0),
            'papers': [],
            'updated': datetime.now().isoformat(),
        }
        
        # Get individual paper citations
        for pub in author.get('publications', []):
            filled_pub = scholarly.fill(pub)
            metrics['papers'].append({
                'title': filled_pub.get('bib', {}).get('title', ''),
                'year': filled_pub.get('bib', {}).get('pub_year', 'N/A'),
                'citations': filled_pub.get('num_citations', 0),
                'venue': filled_pub.get('bib', {}).get('venue', 'N/A')
            })
        
        # Save metrics to file
        os.makedirs('_data', exist_ok=True)
        with open('_data/scholar_metrics.json', 'w') as f:
            json.dump(metrics, f, indent=2)
            
        return metrics
        
    except Exception as e:
        print(f"Error fetching metrics: {str(e)}")
        return None

if __name__ == "__main__":
    print("Fetching Google Scholar metrics...")
    metrics = fetch_metrics()
    if metrics:
        print(f"Total citations: {metrics['total_citations']}")
        print(f"h-index: {metrics['h_index']}")
        print(f"i10-index: {metrics['i10_index']}")
    print("Done!")