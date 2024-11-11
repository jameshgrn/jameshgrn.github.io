#!/usr/bin/env python3
from scholarly import scholarly, ProxyGenerator
import json
import os
from datetime import datetime
import time

def fetch_metrics():
    """Fetch citation metrics from Google Scholar"""
    try:
        print("Setting up proxy...")
        pg = ProxyGenerator()
        success = pg.FreeProxies()
        if not success:
            print("Failed to set up proxy, trying Tor...")
            success = pg.Tor_External(tor_sock_port=9050, tor_control_port=9051)
        
        scholarly.use_proxy(pg)
        
        print("Fetching author profile...")
        # Your Google Scholar ID
        author = scholarly.search_author_id('ppDq7_gAAAAJ')
        if not author:
            print("Could not find author profile")
            return None
            
        print("Fetching detailed metrics...")
        metrics = {
            'total_citations': author.get('citedby', 0),
            'h_index': author.get('hindex', 0),
            'i10_index': author.get('i10index', 0),
            'papers': [],
            'updated': datetime.now().isoformat(),
        }
        
        # Get publications without filling
        for pub in author.get('publications', []):
            metrics['papers'].append({
                'title': pub.get('bib', {}).get('title', 'Unknown'),
                'year': pub.get('bib', {}).get('pub_year', 'N/A'),
                'citations': pub.get('num_citations', 0),
                'venue': pub.get('bib', {}).get('venue', 'N/A')
            })
            time.sleep(2)  # Rate limiting
        
        print("Saving metrics...")
        os.makedirs('_data', exist_ok=True)
        with open('_data/scholar_metrics.json', 'w') as f:
            json.dump(metrics, f, indent=2)
            
        return metrics
        
    except Exception as e:
        print(f"Error fetching metrics: {e}")
        return None

if __name__ == "__main__":
    print("Starting Google Scholar metrics fetch...")
    metrics = fetch_metrics()
    if metrics:
        print(f"Success! Found {len(metrics['papers'])} papers")
        print(f"Total citations: {metrics['total_citations']}")
        print(f"h-index: {metrics['h_index']}")
        print(f"i10-index: {metrics['i10_index']}")
    else:
        print("Failed to fetch metrics")