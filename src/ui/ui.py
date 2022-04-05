from ui.weather_view import WeatherView
from ui.login_view import LoginView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
          # set window size
        window_width = 400
        window_height = 200
        # get the screen dimension
        screen_width = self._root.winfo_screenwidth()
        screen_height = self._root.winfo_screenheight()
        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # set the position of the window to the center of the screen
        self._root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _handle_weather(self):
        self._show_weather_view()

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(self._root, self._handle_weather)
        self._current_view.pack()

    def _show_weather_view(self):
        self._hide_current_view()
        self._current_view = WeatherView(self._root)
        self._current_view.pack()