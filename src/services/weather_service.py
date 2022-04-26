from datetime import datetime, timedelta
import requests
from entities import Weather
from .config_service import ConfigService


class WeatherService:
    def __init__(self) -> None:
        self.__config = ConfigService()

    # Handles all the requests
    def __request(self, url: str) -> dict:
        data_request = requests.get(url)
        data = data_request.json()
        if data_request.status_code == 200 and data != []:
            # getting data in the json format
            return data
        raise Exception

    # Using Geocoding API, converts city name to longitude and latitude
    def __location(self, city: str) -> tuple:
        url = self.__config.geocoding_url + "q=" + \
            city + "&appid=" + self.__config.api_key
        data = self.__request(url)[0]
        return (str(data["lat"]), str(data["lon"]))

    # Onecall API retrieves current and 7 day forecast weather
    def __weather_data(self, latitude: str, longitude: str) -> dict:
        url = self.__config.open_weather_url + "?" + "lat=" + latitude + "&lon=" + longitude + \
            "&exclude=minutely,alerts" + "&appid=" + \
            self.__config.api_key + "&units=metric"
        return self.__request(url)

    # Regarding historical data, the api call has to be called separately on past 5 days
    def __historical_weather_data(self, latitude: str, longitude: str) -> dict:
        historical_data = []
        today = datetime.now()
        for i in range(1, 6):
            day = str(int(datetime.timestamp(today - timedelta(days=i))))
            url = self.__config.open_weather_url + "/timemachine?" + "lat=" + latitude + \
                "&lon=" + longitude + "&dt=" + day + "&appid=" + \
                self.__config.api_key + "&units=metric"
            historical_data = historical_data + self.__request(url)["hourly"]
        return historical_data

    def weather(self, city: str) -> object:
        latitude, longitude = self.__location(city)
        weather_data = self.__weather_data(latitude, longitude)
        historical_data = self.__historical_weather_data(latitude, longitude)
        return Weather(city, weather_data, historical_data)
