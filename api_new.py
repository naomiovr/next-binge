# https://rapidapi.com/movie-of-the-night-movie-of-the-night-default/api/streaming-availability/ 

from requests import get  # This function is how we will make requests to a server.
from requests.models import Response  # This is the type of a Response object.
import requests

url = "https://streaming-availability.p.rapidapi.com/search/basic"

querystring = {"country":"us","service":"netflix","type":"movie","genre":"18","page":"1","output_language":"en","language":"en"}

headers = {
    'x-rapidapi-host': "streaming-availability.p.rapidapi.com",
    'x-rapidapi-key': "a0c9353549msh1b9896d6211d69ep18e7ddjsn07febce82bc1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)