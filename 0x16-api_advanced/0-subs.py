#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys


import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent header to avoid being blocked by Reddit
    headers = {'User-Agent': 'MyBot/1.0'}
    
    # Make a GET request to the subreddit endpoint
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract and return the number of subscribers
        return data['data']['subscribers']
    else:
        # Invalid subreddit or other error, return 0
        return 0
