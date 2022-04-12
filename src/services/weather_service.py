import requests
from entities import Weather
from .config_service import ConfigService


class WeatherService:
    def __init__(self) -> None:
        self.__config = ConfigService()

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

    def __weather_data(self, latitude: str, longitude: str) -> dict:
        url = self.__config.open_weather_url + "lat=" + latitude + "&lon=" + longitude + \
            "&exclude=minutely,hourly,alerts" + "&appid=" + \
            self.__config.api_key + "&units=metric"
        return self.__request(url)

    def weather(self, city: str) -> dict:
        latitude, longitude = self.__location(city)
        weather_data = self.__weather_data(latitude, longitude)
        return Weather(city, weather_data)
