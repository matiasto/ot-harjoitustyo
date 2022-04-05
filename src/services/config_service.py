from configparser import ConfigParser
import os


class ConfigService:

    def __init__(self) -> None:
        self.__parser = ConfigParser()
        self.__CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "config.ini")
        self.__open_weather_url = None
        self.__geocoding_url = None
        self.__api_key = None

        self.__initialize()

    @property
    def open_weather_url(self):
        return self.__open_weather_url

    @property
    def geocoding_url(self):
        return self.__geocoding_url

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self, new_key: str):
        self.__parser.set("USER", "api_key", new_key)
        with open(self.__CONFIG_FILE_PATH, 'w') as configfile:
            self.__parser.write(configfile)

    def api_key_is_set(self) -> bool:
        if self.api_key != "":
            return True
        return False

    def __initialize(self):
        self.__parser.read(self.__CONFIG_FILE_PATH)
        self.__open_weather_url = self.__parser["DEFAULT"]["open_weather_url"]
        self.__geocoding_url = self.__parser["DEFAULT"]["geocoding_url"]
        self.__api_key = self.__parser["USER"]["api_key"]


if __name__=="__main__":
    test = ConfigService()
    print(test.open_weather_url)