
# Dot The Discord Bot

Dot is a Discord Bot developed for small Discord communities, small content creators, and small streaming communities to aid in user engagement and entertainment. 

## Authors

- [@AMWilems](https://github.com/AMWilems)
- [@KatelinVincent](https://github.com/KatelinVincent)
- [@Nwilliamsonwork](https://github.com/Nwilliamsonwork)
- [@TerryTosh](https://github.com/terrytosh)

## Features

- Chat repsonses
- Jokes
- Weather on command
- Weather on a schedule
- Music in Voice Chat utilizing Youtube Music
- some other magic shit
- Math facts about user inputted integers
- Trivia facts about user inputted integers
- Random facts about trivia/math/years/dates
- Account connection to Twitch (No other functionality)
- TwitchAPI/NumbersAPI user help command

## Installation

```bash
    git clone https://github.com/AMWilems/Dot.git
    cd Dot
    pip install discord.py python-dotenv
    python3 -m pip install -U yt-dlp
```
once depenancies are set up, you must next set up a bot through discord to create a connection to the application. using the [Discord Developer Portal](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications). in the portal, create a new application, fill out the information for the application, and then copy the token that is created in the Bot tab.
The program will need the token to run in any capacity, which is stored in a .env file in the root directory of the bot. 

```bash
    cd Dot
    nano .env
```

in the .env, the Discord token should be placed within for secure connection to the Discord.py API with the following syntax:

```bash
DISCORD_TOKEN=<your discord token>
```

in the .env, the Twitch API client_id and client_secret should be place for secure connection to the API with the following syntax:

'''bash
client_id=<your client id>
client_secret=<your client secret>
'''

You will also need an API key for the Jokes API. to generate the key, you need to create an account on [Rapid API](https://rapidapi.com/apininjas/api/jokes-by-api-ninjas/). once an account is created, head to the same link, and copy the X-RapidAPI-Key key that is autogenerated. after which, add a line in to the .env using the following format:
```bash
X-RapidAPI-Key=<your key here>
```
your .env should look like this after these steps:
```bash
DISCORD_TOKEN=<your discord token>
client_id=<your client id>
client_secret=<your client secret>
X-RapidAPI-Key=<your key here>
```

After doing so, save your changes, and exit the file. 

once all dependancies are in place, and .env file has been properly set up, the bot should run as intended on your local system!

## Running Tests

For testing, 2 different approaches are needed. for API connection testing of weather, and for output validation of chat responses, the following code can be ran to test these functions with built in functions from the source code:
```bash
  npm run test
```
    
For other functions, manual testing is needed. the list below shows how to run the tests for each function.
    
    
**Music**: to test music, a user must first connect to a voice channel by clicking on a voice channel within the discord application. once done, use the below command for Dot to join the channel:
    
```bash
    >join
```
    
once this is typed in, we give her something to play using the following command:
    
```bash
    >play https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
    
then using the following commands, we can test pause, resume, and stop
    
```bash
    >pause
    >resume
    >stop
```
    
and finally to have her leave, we test this function using the below command:
    
```bash
    >leave
```

    
    
**Weather**: to test weather functionality, we choose the text channel we wish for this to happen by typing the following command into that channel
    
```bash
    $weather
```
    
note that the above command does not have to be exact, as long as weather is spelt correctly without capitalization, we can use any statement with the word weather in it, and the expected behavior is her providing a link to the current weather report in a link. 
    
    
    
**Jokes**: to test jokes, we perform a similar action to weather, typing the command into the text channel we want the response in. for jokes we include some form of request for jokes with the word joke in it lowercase such as below:
    
```bash
    $joke
```
    
expected output is a random joke generated by an API.
   
    
    
**Random**: for the random function, we again make the request in the text channel we wish for reply in, using a variant of the below command:
    
```bash
    $random
```
    
expected output is a random fact about a random number
  
    
    
**Math**: as with the previous commands, we provide a request in the channel we want an output in, and use the following command: 
    
```bash
    $math <random number>
```
    
expected output is some random math fact about the number provided in the request.

    
    
**Trivia**: as with the other commands, type the following command into the channel we want output in to:
    
```bash
    $trivia <random number>
```
    
the output will be some random trivia regarding the number given

    
    
**Twitch**: as of right now, the only function that the twitch function has is connection to twitch API. to validate this connection, we use a command as follows: 
    
```bash
    $twitch-connect <user>
```
expected output is either a successful connection response, or unsuccessful response. 
