Good chuck noris joke tool

We want to filter good jokes from chuck noris and save them to s3. We will use the follwing api

Get a joke from the api

We will need to call the api. Therefore we need aditional code. Therefore we could use requests

To Install it you can use the python package manager called pip.

pip install requests
(if you have python2 and python3 and it does not work with pip try pip3 install requests)

now we can import the code to call the api.

At the following line at the top for that:

import requests
And than your code to get a new joke

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
To get the data(joke) you can use

data = response.json()
You can also print the data it.

print(data)
it schould look like this

{
  'categories': [],
  'created_at': '2020-01-05 13:42:26.991637',
  'icon_url': 'https://assets.chucknorris.host/img/avatar/chuck-norris.png', 
  'id': 'GrI9Mv07Tj2gL0Wu2Ijcqw', 
  'updated_at': '2020-01-05 13:42:26.991637',
  'url': 'https://api.chucknorris.io/jokes/GrI9Mv07Tj2gL0Wu2Ijcqw',
  'value': 'Chuck Norris once stabbed a man with a bowling ball.'
}
Get a joke from the dictinary

The data you get looks like the json you already know. We just want to have the value of the joke and the id to have a unique name. We will save this with a rating to a file

A dicitinary allways contains of key value pairs like in json.

you can access the value of the response with

joke = data["value"]
You can also create a new dictionary with curly brackets like this

joke_data_to_save = {
  "id": data["id"],
  "joke": data["value"],
  "rating": 4
}
(Optional ) You can add a user input for rating

Save to file

With python you can write to a file with the following command

with open('readme.txt', 'w') as f:
    f.write('readme')
Save the joke_data_to_save to a file with the name [id].json

you can use

import json 
joke_data_as_string = json.dumps(joke_data_to_save)
to create a json string.

And than save it with

with open(joke_data_to_save["id"]+'.json', 'w') as f:
    f.write(joke_data_as_string)
(optional) Use boto 3 to upload file to a s3 bucket when rating is higher than 5