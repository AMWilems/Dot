# Import necessary libraries
import requests
import json

class Trivia:

    # Class constructor - Parameter types: (self, string, string)
    def __init__(self, message, type) :
        self.type = type

        # Extract user inputted integer value from message
        self.num = self.__remove_prefix(message)

    # Class method to return fact given math or trivia type
    def get_fact(self):
        # Build the correct URI for the API call
        url = 'http://numbersapi.com/' + self.num + '/' + self.type + '?json'

        # Perform GET request on 'url'
        response = requests.get(url) 

        # Store response as JSON data
        json_data = response.text
        data_dict = json.loads(json_data)

        # Extract only the resource we need
        fact = data_dict["text"]

        # Return output from API call
        return fact
    
    # Class method to return random fact given no input type
    def get_random_fact(self):
        # Build the correct URI for the API call
        url = 'http://numbersapi.com/random?json'

        # Perform GET request on 'url'
        response = requests.get(url) 

        # Store response as JSON data
        json_data = response.text
        data_dict = json.loads(json_data)

        # Extract only the resource we need
        fact = data_dict["text"]

        # Return output from API call
        return fact
    
    # Private class method to remove prefix from user input
    def __remove_prefix(self, text):
        words = text.split()
        if len(words) >= 2:
            return words[1]
        else:
            return ""
    