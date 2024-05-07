#!/usr/bin/python3

"""Function to query subscribers on a given Reddit subreddit."""

import requests
from urllib.parse import urljoin

BASE_URL = "https://www.reddit.com"
USER_AGENT = "Mozilla/5.0(by /u/CapillaryMercenary12)"


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = urljoin(BASE_URL, f"/r/{subreddit}/about.json")
    headers = {"User-Agent": USER_AGENT}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            return 0
        else:
            raise err

    data = response.json().get("data")
    return data.get("subscribers", 0)


if __name__ == "__main__":
    subreddit = input("Enter a subreddit name: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"The subreddit /r/{subreddit} has {subscribers} subscribers.")