# Import necessary libraries
import requests

class Twitch():

    # Class constructor - No parameter values
    def __init__(self):
        # Build correct url to direct user to Twitch oAuth path
        self.url = "https://id.twitch.tv/oauth2/token"

        # Set required parameters
        self.client_id = "l9lwpc7k4zsmu2mphiuku5thumguht"
        self.client_secret = "5nc2a3uhs3orwxp5dsbjxztjhqbomb"
        self.grant_type = "client_credentials"

        # Load into a dictionary in order to more easily work with
        self.data = {
            'client_id' : 'l9lwpc7k4zsmu2mphiuku5thumguht',
            'client_secret' : '5nc2a3uhs3orwxp5dsbjxztjhqbomb',
            'grant_type' : 'client_credentials'
        }

        self.has_valid_token = False
        self.access_token = ""

    # Class method to grant user access token to Twitch API
    def authorize_user_token(self):
        # Send the token request
        response = requests.post(self.url, data=self.data)

        # Store the user access token
        self.access_token = response.json()['access_token']

        # Set class member variable 'has_valid_token' to True
        self.has_valid_token = True
    
    # Private class method to remove prefix from user inpu
    def remove_prefix(self, text):
        words = text.split()
        if len(words) >= 2:
            return words[1]
        else:
            return ""