#!/usr/bin/python3

"""Function to count words in all hot posts of a given Reddit subreddit."""

import requests
from urllib.parse import urljoin
from collections import defaultdict

BASE_URL = "https://www.reddit.com"
USER_AGENT = "Mozilla/5.0(by /u/CapillaryMercenary12)"


def count_words(subreddit, word_list):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
    """
    url = urljoin(BASE_URL, f"/r/{subreddit}/hot.json")
    headers = {"User-Agent": USER_AGENT}
    params = {"limit": 100}
    instances = defaultdict(int)

    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            if response.status_code == 404:
                print("")
                return
            else:
                raise err

        data = response.json().get("data")
        if not data:
            break

        for post in data["children"]:
            title = post["data"]["title"].lower().split()
            for word in word_list:
                instances[word] += title.count(word.lower())

        after = data.get("after")
        if not after:
            break

        params["after"] = after

    if not instances:
        print("")
        return

    for word, count in sorted(instances.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"{word}: {count}")