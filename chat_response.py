import discord
import os
from Console_Text import Console
import asyncio
from weather_report import Weather
import requests
from Jokes import Jokes
from Trivia import Trivia

SIGNAL = ('$')  # may need to change, unusable in other countries with different keyboard layout,


class Chat:



    # may be taken at incorrect time

    def Check_Intent(message):
        if message.content.startswith(SIGNAL):
            return True
        else:
            return False  # prevents error 400 bad request in terminal


    def check_contents(message):
        reply = Chat.check_verbage(message)
        return reply


    def check_verbage(message):
        # default response
        text = 'no message recognized'

        if message.content.__contains__('hey'):
            text = "Hi everybody! ＼(^o^)／"
            print(Console.Get_Time(), "Said hi")  # makes note in terminal

        elif message.content.__contains__('weather'):
            text = Weather.get_weather()
            res = requests.get(Weather.get_weather())
            print(Console.Get_Time(), "Weather Report")  # makes note in terminal

        elif message.content.__contains__('brew coffee'):
            text = "This server is a teapot, and it cannot brew coffee. error 418"
            print(Console.Get_Time(), "error 418")

        elif message.content.__contains__('your stupid'):
            text = "*you're\n\nand no you."
            print(Console.Get_Time(), 'get wrecked')

        elif message.content.__contains__('joke'):
            text = Jokes.get_joke()
            print(Console.Get_Time(), "made a funny")
        
        elif message.content.__contains__('random'):
            # Create Trivia() object in order to call API
            trivia = Trivia(message.content, "random")

            # Call the API with method in Trivia class and store to user output
            text = trivia.get_random_fact()

            # Log user interatction and time to console
            print(Console.Get_Time(), 'Random Trivia')
        
        elif message.content.__contains__('trivia'):
            # Create Trivia() object in order to call API
            trivia = Trivia(message.content, "trivia")

            # Call the API with method in Trivia class and store to user output
            text = trivia.get_fact()

            # Log user interatction and time to console
            print(Console.Get_Time(), 'Trivia')
        
        elif message.content.__contains__('math'):
            trivia = Trivia(message.content, "math")
            text = trivia.get_fact()
            print(Console.Get_Time(), 'Math Trivia')

        # elif message.content.__contains__('date'):
        #     print(Console.Get_Time(), 'Date Trivia')

        # elif message.content.__contains__('year'):
        #     print(Console.Get_Time(), 'Year Trivia')

        elif message.content.__contains__('numbers-help'):
            # Set output to intended command use
            text = "$math 'integer_value' ---> Displays cool math fact about specified integer value!\n" \
                   "$trivia 'integer_value' ---> Displays cool trivia fact about specified integer value!\n" \
                   "$random ---> Displays cool random fact!" 
            
            # Log user interatction and time to console
            print(Console.Get_Time(), 'Numbers Trivia Help')

        else:
            text = "hmm I don't know that one"

            # Log user interatction and time to console
            print(Console.Get_Time(), "unknown command: ", message.content)

        return text
"""
    elif message.content.__contains__('meme'):
        url = "https://reddit-meme.p.rapidapi.com/memes/trending"

        headers = {
            "X-RapidAPI-Key": "3e8789e929msh7d6211db050d85cp146690jsneccd5efcbf28",
            "X-RapidAPI-Host": "reddit-meme.p.rapidapi.com"
        }

        info = requests.request("GET", url, headers=headers)
        temp = json.loads(info.text)
        response = temp[0]
        text = response["url"]
        print(Console_Text.Get_Time(), "heheheh meme")
"""

