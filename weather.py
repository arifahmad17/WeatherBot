import requests
def Weather(city):
    API_key = "4db2e2579248614e39d9888e62721e00"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    Final_url = base_url + "appid=" + API_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(Final_url).json()
    
    return weather_data['main']


#print(Weather("Delhi"))