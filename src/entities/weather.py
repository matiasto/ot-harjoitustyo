from .current import Current
from .forecast import Forecast
from .graph import Graph


class Weather:
    """Class for representing current weather"""

    def __init__(self, city: str, weather_data: dict, historical_data: list):
        self.__city = city
        self.__current = Current(weather_data["current"])
        self.__forecast = []
        self.__graph = None
        self.__parse_data(weather_data, historical_data)

    @property
    def city(self):
        return self.__city

    @property
    def current(self):
        return self.__current

    @property
    def forecast(self):
        return self.__forecast

    @property
    def graph(self):
        return self.__graph

    def __parse_data(self, weather_data: dict, historical_data):
        graph_data = weather_data["hourly"] + historical_data
        self.__graph = Graph(graph_data)
        for day in weather_data["daily"]:
            self.__forecast.append(Forecast(day))
