import urllib
from urllib.request import*
import json
import requests
foundUsers = set()
foundTreads = set()
startTread = "https://www.reddit.com/.json"
newFeed = requests.get(startTread, headers = {'User-agent': 'Chrome'})
jsonData = json.loads(newFeed.text)
threads = jsonData["data"]["children"]
for thread in threads:
    subReddit = thread["data"]["subreddit"]
    print(subReddit)
    toCrawl = thread["data"]["subreddit_name_prefixed"]
