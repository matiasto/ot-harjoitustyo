from tkinter import constants
from services import WeatherService
from ..frames import NavbarFrame
from ..frames import WeatherFrame
from ..frames import GraphFrame


class WeatherView:
    def __init__(self, root):
        self.__root = root
        self.__weather = WeatherService()
        self.__frames = {}
        self.__data = None
        self.__initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def __handle_get_weather(self, city):
        self.__get_weather(city)

    def __show_navbar_frame(self):
        if "navbar" in self.__frames:
            frame = self.__frames["navbar"]
            frame.destroy()
        self.__frames["navbar"] = NavbarFrame(
            self.__root, self.__data.city, self.__handle_get_weather)
        self.__frames["navbar"].pack()

    def __show_weather_frame(self):
        if "weather" in self.__frames:
            frame = self.__frames["weather"]
            frame.destroy()
        self.__frames["weather"] = WeatherFrame(self.__root, self.__data)
        self.__frames["weather"].pack()

    def __show_graph_frame(self):
        if "graph" in self.__frames:
            frame = self.__frames["graph"]
            frame.destroy()
        self.__frames["graph"] = GraphFrame(self.__root, self.__data.graph)
        self.__frames["graph"].pack()

    def __get_weather(self, city):
        self.__data = self.__weather.weather(city)
        self.__update_frames()

    def __update_frames(self):
        self.__show_navbar_frame()
        self.__show_weather_frame()
        self.__show_graph_frame()

    def __initialize(self):
        city = "Helsinki"
        data = self.__weather.weather(city)
        self.__frames["navbar"] = NavbarFrame(
            self.__root, city, self.__handle_get_weather)
        self.__frames["weather"] = WeatherFrame(self.__root, data)
        self.__frames["graph"] = GraphFrame(self.__root, data.graph)

        self.__frames["navbar"].pack()
        self.__frames["weather"].pack()
        self.__frames["graph"].pack()
