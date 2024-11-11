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
        search_query = scholarly.search_author_id('ppDq7_gAAAAJ')
        author = next(search_query)
        
        # Fill in author data
        author = scholarly.fill(author)
        
        metrics = {
            'total_citations': author['citedby'],
            'h_index': author['hindex'],
            'i10_index': author['i10index'],
            'papers': [],
            'updated': datetime.now().isoformat(),
        }
        
        # Get individual paper citations
        for pub in author['publications']:
            pub = scholarly.fill(pub)
            metrics['papers'].append({
                'title': pub['bib']['title'],
                'year': pub['bib'].get('year', 'N/A'),
                'citations': pub['num_citations'],
                'venue': pub['bib'].get('venue', 'N/A')
            })
        
        # Save metrics to file
        os.makedirs('_data', exist_ok=True)
        with open('_data/metrics.json', 'w') as f:
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