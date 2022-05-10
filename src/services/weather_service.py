from datetime import datetime, timedelta
import requests
from entities import Weather
from .config_service import ConfigService


class WeatherService:
    """Fetches weather data from the API.

    The weather() method works as the class endpoint
    and is therefore the only public method.

    Given the city name as the input, the name is first converted to
    longitude and latitude by location() method. Then, that location
    data is used to retrieve historical, current and forecast weather data.
    The data is then remodeled to Weather object and returned.

    Attributes:
        config: object instance that includes API base urls and api key.
    """

    def __init__(self) -> None:
        """Class constructor.

        Creates an instance of config service.
        """

        self.__config = ConfigService()

    def __request(self, url: str) -> dict:
        """Handles all requests.

        Makes the request to appointed url, parses data
        from json respond, and returns the data as dictionary.

        Args:
            url (str): The request url.

        Raises:
            Exception: The request failed.

        Returns:
            dict: The data from succesful request.
        """

        data_request = requests.get(url)
        data = data_request.json()
        if data_request.status_code == 200 and data != []:
            return data
        return False

    def __location(self, city: str) -> tuple:
        """Using Geocoding API, converts city name to longitude and latitude.

        Converts user input city name to longitude and latitude.

        Args:
            city (str): Cities name from user input.

        Returns:
            tuple: Longitude and latitude are float values in string format.
        """

        url = f"{self.__config.geocoding_url}q={city}&appid={self.__config.api_key}"
        data = self.__request(url)
        if not data:
            return False
        return (data[0]["name"], str(data[0]["lat"]), str(data[0]["lon"]))

    def __weather_data(self, latitude: str, longitude: str) -> dict:
        """Using Onecall API retrieves the current and 7 day forecast weather.

        Args:
            latitude (str): Input city latitude.
            longitude (str): Input city longitude.

        Returns:
            dict: The weather data in dict format.
            keys of interest include "current", "hourly", and "daily".
            Keys "hourly" and "daily" include a list of dictionaries
            describing their respective weather conditions.
        """

        url = (f"{self.__config.open_weather_url}?lat={latitude}&lon={longitude}"
               f"&exclude=minutely,alerts&appid={self.__config.api_key}&units=metric")
        return self.__request(url)

    def __historical_weather_data(self, latitude: str, longitude: str) -> list:
        """Using Onecall API retrieves the 5 day historical weather.

        The API requires separate requests for each day.

        Args:
            latitude (str): Input city latitude.
            longitude (str): Input city longitude.

        Returns:
            list: List of hourly historical data.
            Each hours weather is represented as dictionary.
        """

        historical_data = []
        today = datetime.now()
        for i in range(1, 6):
            day = str(int(datetime.timestamp(today - timedelta(days=i))))
            url = (f"{self.__config.open_weather_url}/timemachine?lat={latitude}&lon={longitude}"
                   f"&dt={day}&appid={self.__config.api_key}&units=metric")
            new_day = self.__request(url)
            if not new_day:
                return False
            historical_data += new_day["hourly"]
        return historical_data

    def weather(self, city: str) -> object:
        """The class endpoint.

        Given the city input, the method calls for location() on the input.
        The returned latitude and longitude are then fed to
        weather_data() and historical_data().
        The retrieved data is remodeled to Weather object
        and returned.

        Args:
            city (str): User input city name.

        Returns:
            object: Weather object.
        """
        
        location_data = self.__location(city)
        if not location_data:
            return False
        city_name, latitude, longitude = location_data
        weather_data = self.__weather_data(latitude, longitude)
        if not weather_data:
            return False
        historical_data = self.__historical_weather_data(latitude, longitude)
        if not historical_data:
            return False
        return Weather(city_name, weather_data, historical_data)
