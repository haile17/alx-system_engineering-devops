#!/usr/bin/python3
"""
function that queries that Reddit API and
returns the number of subscriber count of a given subreddit
"""
from requests import get

def number_of_subscribers(subreddit):
    try:
        h = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers={'user-agent' : 'hAxr'}, allow_redirects=False).json()
        return h.get('data').get('subscribers') if not None else 0
    except:
        return 0
