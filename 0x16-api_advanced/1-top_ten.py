#!/usr/bin/python3
"""
1-top_ten.py
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given subreddit

    Args:
        subreddit (str): Subreddit name
    """
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers = {
            'User-Agent': 'My User Agent 1.0',
        }
        res = requests.get(url, headers=headers)
        resJson = res.json()
        posts = resJson['data']['children']

        if len(posts) == 0:
            raise KeyError()

        for post in posts:
            print(post['data']['title'])

    except KeyError:
        print(None)
