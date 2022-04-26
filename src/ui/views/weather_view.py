from tkinter import constants
from services import WeatherService
from frames import NavbarFrame
from frames import WeatherFrame
from frames import GraphFrame


class WeatherView:
    def __init__(self, root):
        self._root = root
        self._weather = WeatherService()
        self._frames = {}
        self._data = None
        self._options = {'padx': 5, 'pady': 5}
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_get_weather(self, city):
        self._get_weather(city)

    def _show_navbar_frame(self):
        if "navbar" in self._frames:
            frame = self._frames["navbar"]
            frame.destroy()
        self._frames["navbar"] = NavbarFrame(
            self._root, self._data.city, self._handle_get_weather)
        self._frames["navbar"].pack()

    def _show_weather_frame(self):
        if "weather" in self._frames:
            frame = self._frames["weather"]
            frame.destroy()
        self._frames["weather"] = WeatherFrame(self._root, self._data)
        self._frames["weather"].pack()

    def _show_graph_frame(self):
        if "graph" in self._frames:
            frame = self._frames["graph"]
            frame.destroy()
        self._frames["graph"] = GraphFrame(self._root, self._data.graph)
        self._frames["graph"].pack()

    def _get_weather(self, city):
        self._data = self._weather.weather(city)
        self._update_frames()

    def _update_frames(self):
        self._show_navbar_frame()
        self._show_weather_frame()
        self._show_graph_frame()

    def _initialize(self):
        city = "Helsinki"
        data = self._weather.weather(city)
        self._frames["navbar"] = NavbarFrame(
            self._root, city, self._handle_get_weather)
        self._frames["weather"] = WeatherFrame(self._root, data)
        self._frames["graph"] = GraphFrame(self._root, data.graph)

        self._frames["navbar"].pack()
        self._frames["weather"].pack()
        self._frames["graph"].pack()
