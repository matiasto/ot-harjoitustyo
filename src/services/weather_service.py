import requests
from entities import WeatherNow
from .config_service import ConfigService

class WeatherService:
    def __init__(self) -> None:
        self.__config = ConfigService()

    def __request(self, url: str) -> dict:
        data_request = requests.get(url)
        if data_request.status_code == 200:
            # getting data in the json format
            return data_request.json()
        else:
            print(f"Error in request:\nExited with code {data_request.status_code}")

    # Using Geocoding API, converts city name to longitude and latitude 
    def __location(self, city: str) -> tuple:
        URL = self.__config.geocoding_url + "q=" + city + "&appid=" + self.__config.api_key
        data = self.__request(URL)[0]
        return (str(data["lat"]), str(data["lon"]))

    def __current_weather_data(self, latitude: str, longitude: str) -> dict:
        URL = self.__config.open_weather_url + "lat=" + latitude + "&lon=" + longitude + \
            "&lang=fi" + "&appid=" + self.__config.api_key + "&units=metric"
        return self.__request(URL)

    def current_weather(self, city: str) -> dict:
        latitude, longitude = self.__location(city)
        weather_data = self.__current_weather_data(latitude, longitude)
        return WeatherNow(city, weather_data)

