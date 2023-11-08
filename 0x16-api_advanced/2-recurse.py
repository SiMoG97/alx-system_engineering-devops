#!/usr/bin/python3
"""
2-recurse.py.py
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.

    Args:
        subreddit (str): Subreddit name
        hot_list (list): an empty list to be filled with the titles
    Returns:
        list: a list of hot titles
    """
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
        headers = {
            'User-Agent': 'My User Agent 1.0',
        }
        res = requests.get(url, headers=headers)

        resJson = res.json()
        posts = resJson['data']['children']
        after = resJson['data']['after']

        if 'subreddit_id' not in posts[0]['data']:
            return None

        for post in posts:
            hot_list.append(post['data']['title'])

        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)

    except Exception:
        return None
