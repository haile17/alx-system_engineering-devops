#!/usr/bin/python3
"""
prints the top ten titiles of a given subreddit
"""

from requests import get

def top_ten(subreddit):
    try:
        h = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={'user-agent':'' }, params={'limits': 10},
        allow_redirects=False).json()
        for item in h['data']['children']:
            print(item['data']['title'])
    except:
        print('None')
