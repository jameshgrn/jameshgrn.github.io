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
        author_info = scholarly.fill(author)
        
        metrics = {
            'total_citations': getattr(author_info, 'citedby', 0),
            'h_index': getattr(author_info, 'hindex', 0),
            'i10_index': getattr(author_info, 'i10index', 0),
            'papers': [],
            'updated': datetime.now().isoformat(),
        }
        
        # Get individual paper citations
        for pub in getattr(author_info, 'publications', []):
            pub_complete = scholarly.fill(pub)
            metrics['papers'].append({
                'title': pub_complete.bib.get('title', ''),
                'year': pub_complete.bib.get('year', 'N/A'),
                'citations': getattr(pub_complete, 'citedby', 0),
                'venue': pub_complete.bib.get('venue', 'N/A')
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