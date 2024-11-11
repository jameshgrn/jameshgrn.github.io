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
        pg.FreeProxies()
        scholarly.use_proxy(pg)
        
        # Search for your profile
        author = scholarly.search_author_id('ppDq7_gAAAAJ')  # Your Google Scholar ID
        
        # Get complete author info
        author_info = scholarly.fill(author)
        
        metrics = {
            'total_citations': author_info['citedby'],
            'h_index': author_info['hindex'],
            'i10_index': author_info['i10index'],
            'papers': [],
            'updated': datetime.now().isoformat(),
        }
        
        # Get individual paper citations
        for pub in author_info['publications']:
            pub_complete = scholarly.fill(pub)
            metrics['papers'].append({
                'title': pub_complete['bib']['title'],
                'year': pub_complete['bib'].get('pub_year', 'N/A'),
                'citations': pub_complete['num_citations'],
                'venue': pub_complete['bib'].get('venue', 'N/A')
            })
        
        # Save metrics to file
        os.makedirs('_data', exist_ok=True)
        with open('_data/scholar_metrics.json', 'w') as f:
            json.dump(metrics, f, indent=2)
            
        return metrics
        
    except Exception as e:
        print(f"Error fetching metrics: {e}")
        return None

if __name__ == "__main__":
    metrics = fetch_metrics()
    if metrics:
        print(f"Total citations: {metrics['total_citations']}")
        print(f"h-index: {metrics['h_index']}")
        print(f"i10-index: {metrics['i10_index']}") 