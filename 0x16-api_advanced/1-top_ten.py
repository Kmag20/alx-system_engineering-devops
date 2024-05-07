#!/usr/bin/python3

"""Function to print hot posts on a given Reddit subreddit."""

import requests
from urllib.parse import urljoin

BASE_URL = "https://www.reddit.com"
USER_AGENT = "Mozilla/5.0(by /u/CapillaryMercenary12)"


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = urljoin(BASE_URL, f"/r/{subreddit}/hot.json")
    headers = {"User-Agent": USER_AGENT}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print("None")
            return
        else:
            raise err

    data = response.json().get("data")
    if not data:
        print("None")
        return

    for child in data.get("children", []):
        print(child.get("data", {}).get("title", "No title"))