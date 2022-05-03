from configparser import ConfigParser
import os


class ConfigService:
    """Administers API configurations.

    Attributes:
        arser: Instanse of ConfigParser that reads and writes config.ini file.
        config_file_path: File path for configuration file.
        open_weather_url: base url for Onecall API used to retrieve weather data.
        geocoding_url: base url for Geocoding API used to convert city name to
                       latitude and longitude.
        icon_url: base url for weather icons.
        api_key: The key required to access the OpenWeather- and Geocoding API.
    """

    def __init__(self) -> None:
        """The class constuctor.

        Initializes the class by reading the existing config.ini file
        and setting the attributes.
        """
        self.__parser = ConfigParser()
        self.__config_file_path = os.path.join(
            os.path.dirname(__file__), "..", "config.ini")
        self.__open_weather_url = None
        self.__geocoding_url = None
        self.__icon_url = None
        self.__api_key = None

        self.__initialize()

    @property
    def open_weather_url(self):
        """The Open Weather - One Call API base url."""

        return self.__open_weather_url

    @property
    def geocoding_url(self):
        """The Open Weather - Geocoding API base url."""

        return self.__geocoding_url

    @property
    def icon_url(self):
        """The Open Weather - weather icon base url"""
        return self.__icon_url

    @property
    def api_key(self):
        """The Open Weather - API Key."""
        return self.__api_key

    @api_key.setter
    def api_key(self, new_key: str):
        """Sets API key.

        Saves the key to config.ini.

        Args:
            new_key (str): New key from the user.
        """

        self.__parser.set("USER", "api_key", new_key)
        with open(self.__config_file_path, 'w', encoding="utf8") as configfile:
            self.__parser.write(configfile)
        self.__api_key = new_key

    def api_key_is_set(self) -> bool:
        """Check if API key is set.

        Returns:
            bool: Is set?
        """
        if self.__api_key:
            return True
        return False

    def __initialize(self):
        """Initialize atributes.

        Reads config.ini file and sets corresponding atribute values.
        """
        self.__parser.read(self.__config_file_path)
        self.__open_weather_url = self.__parser["DEFAULT"]["open_weather_url"]
        self.__geocoding_url = self.__parser["DEFAULT"]["geocoding_url"]
        self.__icon_url = self.__parser["DEFAULT"]["icon_url"]
        self.__api_key = self.__parser["USER"]["api_key"]
