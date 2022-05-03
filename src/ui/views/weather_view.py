from tkinter import constants
from services import WeatherService
from ..frames import NavbarFrame
from ..frames import CurrentFrame
from ..frames import ForecastFrame
from ..frames import GraphFrame


class WeatherView:
    """The applications main view.
    
    Combines multiple frames into one view.
    Handles new requests to WeatherService.
    Updates frames with new data.

    Managed by the UI.

    Attributes:
        root: The root window.
        frame: The Frame instance.
        weather: Instance of WeatherService.
        frames: Collection of all frames in key: Frame format.
        data: The Weather entity that holds the weather data.
    """

    def __init__(self, root: object) -> None:
        """Class constructor.

        Args:
            root (object): The root window, Tk() instance.
        """

        self.__root = root
        self.__weather = WeatherService()
        self.__frames = {}
        self.__data = None
        self.__initialize()

    def pack(self) -> None:
        """Pack widgets."""

        self._frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self._frame.destroy()

    def __handle_get_weather(self, city: str) -> None:
        """The get handler.

        This method is passed on to NavbarFrame
        Where it is also called. Once called,
        the method activates the request sequence
        better desribed in Documentation.

        Args:
            city (str): City name user input.
        """

        self.__get_weather(city)

    def __show_navbar_frame(self) -> None:
        """Activates NavbarFrame.
        
        Passes the city name as an argument.
        (used in header element).
        """

        if "navbar" in self.__frames:
            frame = self.__frames["navbar"]
            frame.destroy()
        self.__frames["navbar"] = NavbarFrame(
            self.__root, self.__data.city, self.__handle_get_weather)
        self.__frames["navbar"].pack()

    def __show_current_frame(self) -> None:
        """Activates CurrentFrame.

        Passes the "Current" entity as an argument.
        """

        if "current" in self.__frames:
            frame = self.__frames["current"]
            frame.destroy()
        self.__frames["current"] = CurrentFrame(
            self.__root, self.__data.current)
        self.__frames["current"].pack()

    def __show_forecast_frame(self) -> None:
        """Activates ForecastFrame.

        Passes the list of Forecast entitis as an argument.
        """

        if "forecast" in self.__frames:
            frame = self.__frames["forecast"]
            frame.destroy()
        self.__frames["forecast"] = ForecastFrame(
            self.__root, self.__data.forecast)
        self.__frames["forecast"].pack()

    def __show_graph_frame(self) -> None:
        """Activates GraphFrame.

        Passes the Graph DataFrame as an argument.
        """
        if "graph" in self.__frames:
            frame = self.__frames["graph"]
            frame.destroy()
        self.__frames["graph"] = GraphFrame(self.__root, self.__data.graph)
        self.__frames["graph"].pack()

    def __get_weather(self, city: str) -> None:
        """Interacts with WeatherService.

        Requests data from WeatherService, stores the result to
        data attribute, and updates the frames.

        Args:
            city (str): User city name input.
        """

        self.__data = self.__weather.weather(city)
        self.__update_frames()

    def __update_frames(self) -> None:
        """Sets of frame updates."""

        self.__show_navbar_frame()
        self.__show_current_frame()
        self.__show_forecast_frame()
        self.__show_graph_frame()

    def __initialize(self) -> None:
        """Initializes the view.
        
        Default parameter: Helsinki.
        """

        city = "Helsinki"
        data = self.__weather.weather(city)
        self.__frames["navbar"] = NavbarFrame(
            self.__root, city, self.__handle_get_weather)
        self.__frames["current"] = CurrentFrame(self.__root, data.current)
        self.__frames["forecast"] = ForecastFrame(self.__root, data.forecast)
        self.__frames["graph"] = GraphFrame(self.__root, data.graph)

        self.__frames["navbar"].pack()
        self.__frames["current"].pack()
        self.__frames["forecast"].pack()
        self.__frames["graph"].pack()
