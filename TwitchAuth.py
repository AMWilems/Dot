import requests

class TwitchAuth():
    # Set up the parameters for the token request
    def __init__(self, url, client_id, client_secret, grant_type):
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type

    def get_token(self):
        # Send the token request
        response = requests.post(self.url, params={
        'client_id': self.client_id,
        'client_secret': self.client_secret,
        'grant_type': self.grant_type
        })
        access_token = response.json()['access_token']
        return access_token
