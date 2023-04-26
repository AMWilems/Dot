import requests

class Twitch():

    def __init__(self):
        self.url = "https://id.twitch.tv/oauth2/token"
        self.client_id = "l9lwpc7k4zsmu2mphiuku5thumguht"
        self.client_secret = "5nc2a3uhs3orwxp5dsbjxztjhqbomb"
        self.grant_type = "client_credentials"
        self.data = {
            'client_id' : 'l9lwpc7k4zsmu2mphiuku5thumguht',
            'client_secret' : '5nc2a3uhs3orwxp5dsbjxztjhqbomb',
            'grant_type' : 'client_credentials'
        }
        self.has_valid_token = False
        self.access_token = ""

    def authorize_user_token(self):
        # Send the token request
        response = requests.post(self.url, data=self.data)
        self.access_token = response.json()['access_token']
        self.has_valid_token = True
