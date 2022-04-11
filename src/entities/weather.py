from .current import Current
from .day import Day


class Weather:
    """Class for representing current weather"""

    def __init__(self, city_name: str, data: dict):
        self.__city_name = city_name
        self.__current = None
        self.__forecast = list()
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

    def __set_current(self, data: dict):
        self.__current = Current(data)

    def __parse_data(self, data: dict):
        self.__set_current(data["current"])
        for day in data["daily"]:
            self.__forecast.append(Day(day))
