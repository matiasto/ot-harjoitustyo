from .views import WeatherView
from .views import LoginView
from services import ConfigService


class UI:
    def __init__(self, root):
        self.__root = root
        self.__current_view = None
        self.__config = ConfigService()
        self.__set_up_geometry()

    def __set_up_geometry(self):
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        center_x = int(screen_width/2)
        center_y = int(screen_height/2)
        self.__root.geometry("+%d+%d" % (center_x, center_y))

    def __hide_current_view(self):
        if self.__current_view:
            self.__current_view.destroy()
        self.__current_view = None

    def __handle_weather(self):
        self.__show_weather_view()

    def __handle_login(self):
        self.__show_login_view()

    def __show_login_view(self):
        self.__hide_current_view()
        self.__current_view = LoginView(
            self.__root, self.__handle_weather, self.__config)
        self.__current_view.pack()

    def __show_weather_view(self):
        self.__hide_current_view()
        self.__current_view = WeatherView(self.__root)

    def start(self):
        if self.__config.api_key_is_set():
            self.__handle_weather()
        else:
            self.__handle_login()
