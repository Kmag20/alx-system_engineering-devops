#!/usr/bin/python3

"""Function to query a list of all hot posts on a given Reddit subreddit."""

import requests
from urllib.parse import urljoin

BASE_URL = "https://www.reddit.com"
USER_AGENT = "Mozilla/5.0(by /u/CapillaryMercenary12)"


def get_hot_posts(subreddit):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = urljoin(BASE_URL, f"/r/{subreddit}/hot.json")
    headers = {"User-Agent": USER_AGENT}
    params = {"limit": 100}
    hot_posts = []

    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            if response.status_code == 404:
                return None
            else:
                raise err

        data = response.json().get("data")
        if not data:
            break

        hot_posts.extend(post["data"]["title"] for post in data["children"])

        after = data.get("after")
        if not after:
            break

        params["after"] = after

    return hot_posts
