from .current import Current
from .forecast import Forecast


class Weather:
    """Class for representing current weather"""

    def __init__(self, city_name: str, data: dict):
        self.__city_name = city_name
        self.__current = Current(data["current"])
        self.__forecast = []
        self.__parse_data(data)

    @property
    def city_name(self):
        return self.__city_name

    @property
    def current(self):
        return self.__current

    @property
    def forecast(self):
        return self.__forecast

    def __parse_data(self, data: dict):
        for day in data["daily"]:
            self.__forecast.append(Forecast(day))
