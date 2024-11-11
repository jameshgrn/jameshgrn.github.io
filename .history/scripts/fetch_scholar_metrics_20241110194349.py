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
        
        # Get complete author info
        metrics = {
            'total_citations': search_query['citedby'],
            'h_index': search_query['hindex'],
            'i10_index': search_query.get('i10index', 0),
            'papers': [],
            'updated': datetime.now().isoformat(),
        }
        
        # Get individual paper citations
        for pub in search_query.get('publications', []):
            pub_data = scholarly.fill(pub)
            metrics['papers'].append({
                'title': pub_data['bib'].get('title'),
                'year': pub_data['bib'].get('year', 'N/A'),
                'citations': pub_data.get('num_citations', 0),
                'venue': pub_data['bib'].get('venue', 'N/A')
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
    print("Fetching Google Scholar metrics...")
    metrics = fetch_metrics()
    if metrics:
        print(f"Total citations: {metrics['total_citations']}")
        print(f"h-index: {metrics['h_index']}")
        print(f"i10-index: {metrics['i10_index']}")
    print("Done!")