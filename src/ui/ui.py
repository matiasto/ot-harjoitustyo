from .views import WeatherView
from .views import LoginView
from services import ConfigService


class UI:
    """The main UI.

    Manages all the views.

    Attributes:
        root: The root window.
        current_view: Active view.
        config: Instance of ConfigService.
    """

    def __init__(self, root: object) -> None:
        """Class constructor.

        Args:
            root (object): The root window, Tk() instance.
        """

        self.__root = root
        self.__current_view = None
        self.__config = ConfigService()
        self.__set_up_geometry()

    def __set_up_geometry(self) -> None:
        """Sets up window geometry."""

        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        center_x = int(screen_width/2)
        center_y = int(screen_height/2)
        self.__root.geometry("+%d+%d" % (center_x, center_y))

    def __hide_current_view(self) -> None:
        """Destroys the current view."""

        if self.__current_view:
            self.__current_view.destroy()
        self.__current_view = None

    def __handle_weather(self) -> None:
        """Handles redirect to WeatherView.

        Used in LoginView.
        """

        self.__show_weather_view()

    def __show_login_view(self) -> None:
        """Activates LoginView."""

        self.__hide_current_view()
        self.__current_view = LoginView(
            self.__root, self.__handle_weather, self.__config)
        self.__current_view.pack()

    def __show_weather_view(self) -> None:
        """Activates WeatherView."""

        self.__hide_current_view()
        self.__current_view = WeatherView(self.__root)

    def start(self) -> None:
        """Start the UI.

        Chooses view based on API key presence.
        """

        if self.__config.api_key_is_set():
            self.__handle_weather()
        else:
            self.__show_login_view()
