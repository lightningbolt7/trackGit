import requests

#name = input("Github user: ")
endpoint = f'https://api.github.com/users/lightningbolt7/events'

response = requests.get(endpoint)
data = response.json()

for element in data:
     action = element["type"]
     actor = element["actor"]["login"]
     repo = element["repo"]["name"]
     date = element["created_at"]
     
     result = f"{actor} did {action} on {repo} at {date}"
     print(result)
     


