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
    baseUrl = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'My User Agent 1.0',
    }
    params = {'after': after} if after else {}
    res = requests.get(
        baseUrl,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if res.status_code != 200:
        return None

    resJson = res.json()
    posts = resJson.get('data').get('children')
    afterId = resJson.get('data').get('after')

    for post in posts:
        hot_list.append(post['data']['title'])

    if afterId:
        return recurse(subreddit, hot_list, afterId)

    return hot_list if len(hot_list) > 0 else None
