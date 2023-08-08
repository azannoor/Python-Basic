import requests
import json

response= requests.get('https://api.github.com/repos/python/getpython3.com')
print(response.status_code)
data=response.text
parse_json=json.loads(data)
description=parse_json['description']
print("Description: "+description)

forkCount=parse_json['forks_count']
print("fork count: "+str(forkCount))