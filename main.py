import requests

name = input("Github user: ")
endpoint = f'https://api.github.com/users/{name}/events'

response = requests.get(endpoint)
data = response.json()

tracker = {}

for element in data:
    action = element["type"]
    actor = element["actor"]["login"]
    repo = element["repo"]["name"]
    date = element["created_at"][0:10]

    key = (action,actor,repo,date)
    
    if tracker.get(key) is None:
        tracker[key] = 1
    else:
        tracker[key]+=1
    
for element in tracker:
    result = f"{element[1]} did {tracker.get(element)} {element[0]} on {element[2]} at {element[3]}"
    print(result)
        
     
    
     



     


