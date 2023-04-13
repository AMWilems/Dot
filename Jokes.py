import requests
import json

url = "https://jokes-by-api-ninjas.p.rapidapi.com/v1/jokes"

headers = {
	"X-RapidAPI-Key": "3e8789e929msh7d6211db050d85cp146690jsneccd5efcbf28",
	"X-RapidAPI-Host": "jokes-by-api-ninjas.p.rapidapi.com"
}

def get_joke():
    response = requests.request("GET", url, headers=headers)
    return(response.text["joke"])
