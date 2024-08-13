#!/usr/bin/python3
"""Script that returns the number of subscribers of a subreddit"""
import requests

def number_of_subscribers(subreddit):
    """Function that returns the number of subscribers of a subreddit"""
    if not isinstance(subreddit, str):
        return 0

    headers = {'User-Agent': 'selBot/1.0'}
    URL = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(URL, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)  # Safely access 'subscribers'

    except requests.exceptions.RequestException:
        return 0
