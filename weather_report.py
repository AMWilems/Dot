import requests
class Weather:
    def get_weather():
        city = 'Austin'
        
        url = 'https://wttr.in/{}'.format(city)
        res = requests.get(url)

        return(url)