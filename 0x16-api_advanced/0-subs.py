#!/usr/bin/python3
"""
0-subs.py
"""
import requests


def number_of_subscribers(subreddit):
    """_summary_

    Args:
        subreddit (str): Subreddit name

    Returns:
        int: the number of subs in the passed subreddit
    """
    try:
        headers = {
            'User-Agent': 'My User Agent 1.0',
        }
        res = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers=headers)

        resJson = res.json()
        subCount = resJson['data']['subscribers']

        return subCount
    except KeyError:
        return 0
