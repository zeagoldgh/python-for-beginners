import requests
import json

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
data = response.json


print("New Joke:")
print(data["value"])
rating = int(input("Please enter a rating between 0-5/n"))

joke_data = {
    "id": data["id"],
    "joke": data["value"],
    "rating": rating
}

print(joke_data)

if(rating > 3):
    
    with open(joke_data["id"] + '.json', 'w') as f:
        f.write(json.dumps(joke_data))

