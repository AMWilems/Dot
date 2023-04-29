import requests
import json

class Trivia:

    def __init__(self, message, type) :
        self.type = type
        self.num = self.__remove_prefix(message)
        print(self.num)

    def get_fact(self):
        url = 'http://numbersapi.com/' + self.num + '/' + self.type + '?json'
        response = requests.get(url) 
        json_data = response.text
        data_dict = json.loads(json_data)
        fact = data_dict["text"]
        return fact
    
    def get_random_fact(self):
        url = 'http://numbersapi.com/random?json'
        response = requests.get(url) 
        json_data = response.text
        data_dict = json.loads(json_data)
        fact = data_dict["text"]
        return fact
    
    def __remove_prefix(self, text):
        words = text.split()
        if len(words) >= 2:
            return words[1]
        else:
            return ""
    