#!/usr/bin/python3
"""
This module contains a function that fetches the number of subscribers
from a given subreddit using the Reddit API.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a specified subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: Number of subscribers if the subreddit is valid, 0 otherwise.
    """
    # Set up the URL and headers for the request
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    # Send a GET request
    response = requests.get(url, headers=headers)
    
    # Check if the subreddit is valid by checking the status code and response content
    if response.status_code == 200:
        # Parse JSON data from the response
        data = response.json()
        # Get the subscriber count
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # If the subreddit is not valid, return 0
        return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
