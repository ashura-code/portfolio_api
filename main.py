import requests
import json

a = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")

for data in a.json()['items']:
    if ('javascript' or 'nodejs' or 'linux' or 'safari' or 'regex') in data['tags']:
        print(data['tags'])
        print("\n")
        print(data['owner']['display_name'])
        print(data['title'])
        print(data['link'])
        print("\n")
