import requests

url = "https://jokes.p.rapidapi.com/joke/random"

headers = {
	"X-RapidAPI-Key": "3e8789e929msh7d6211db050d85cp146690jsneccd5efcbf28",
	"X-RapidAPI-Host": "jokes.p.rapidapi.com"
}
def get_joke():
    response = requests.request("GET", url, headers=headers)
    return(response.text)
