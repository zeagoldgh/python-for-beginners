import requests
import json
import boto3
s3 = boto3.resource('s3')

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)

data = response.json()

joke_to_save = {
    "id": data["id"],
    "joke": data["value"],  
}
with open('pythonjoke.json', 'w') as f:
        f.write(json.dumps(joke_to_save))

s3.meta.client.upload-f('pythonjoke.json', 'wale-buck-for-boto3', 'pythonjoke.json')