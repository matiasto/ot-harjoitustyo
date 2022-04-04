import requests
from os import getenv
from entities import WeatherNow

class Weather:
    def __init__(self) -> None:
        # API key for OpenWeatherMap
        self.__API_KEY = getenv("OPENWEATHER_API_KEY")
        # URL for weather data request
        self.__WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?"
        # URL for location request city -> latitude, longitude
        self.__GEO_URL = "http://api.openweathermap.org/geo/1.0/direct?"

    # getters for class atributes
    @property
    def api_key(self):
        return self.__API_KEY

    @property
    def weather_url(self):
        return self.__WEATHER_URL

    @property
    def geo_url(self):
        return self.__GEO_URL

    # Using Geocoding API, converts city name to longitude and latitude 
    def __location(self, city: str) -> tuple:

        URL = self.geo_url + "q=" + city + "&appid=" + self.api_key

        location_request = requests.get(URL)
        if location_request.status_code == 200:
            # getting data in the json format
            data = location_request.json()[0]
            return (str(data["lat"]), str(data["lon"]))
        else:
            print('Error in location request')

    def __current_weather_data(self, latitude: str, longitude: str) -> dict:
        
        URL = self.weather_url + "lat=" + latitude + "&lon=" + longitude + \
            "&lang=fi" + "&appid=" + self.api_key + "&units=metric"

        weather_request = requests.get(URL)
        if weather_request.status_code == 200:
            # getting data in the json format
            return weather_request.json()
        else:
            print("Error in the weather request")

    def current_weather(self, city: str) -> dict:
        latitude, longitude = self.__location(city)
        weather_data = self.__current_weather_data(latitude, longitude)
        weather_data = WeatherNow(city, weather_data)
        return weather_data

