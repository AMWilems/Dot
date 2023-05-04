# Import necessary libraries
import requests
from dotenv import load_dotenv
import os

class Twitch():

    # Class constructor - No parameter values
    def __init__(self):
        # Build correct url to direct user to Twitch oAuth path
        self.url = "https://id.twitch.tv/oauth2/token"

        # Get client details from .env
        load_dotenv()
        id = os.getenv("client_id")
        secret = os.getenv("client_secret")

        # Set required parameters
        self.client_id = str(id)
        self.client_secret = str(secret)
        self.grant_type = "client_credentials"

        # Load into a dictionary in order to more easily work with
        self.data = {
            'client_id' : self.client_id,
            'client_secret' : self.client_secret,
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
    
    # Class method to remove prefix from user input
    def remove_prefix(self, text):
        words = text.split()
        if len(words) >= 2:
            return words[1]
        else:
            return ""