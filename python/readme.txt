
def get_new_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    joke_data = response.json()
    rating = input("Please enter a rating between 0-5/n")

    joke_data = {
    "id": joke_data["id"],
    "joke": joke_data["value"],
    "rating": rating
}

with open('readme.txt', 'w') as f:
        f.write('readme') 

with open('joke.json', 'w') as f:
    f.write(json.dumps(joke_data))
get_new_joke()
s3.meta.client.upload-f('joke.json', 'wale-buck-for-boto3', 'joke.json')