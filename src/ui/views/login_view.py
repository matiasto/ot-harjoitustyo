from tkinter import ttk, constants, StringVar


class LoginView:
    """View for setting API key.

    This view is shown if UI can't find an API key.
    Once user has set their own API key, they are
    redirected to WeatherView.

    Managed by the UI.

    Attributes:
        root: The root window.
        frame: The Frame instance.
        handle_weather: Method for redirect after API key is set.
        config: Instance of ConfigService.
        api_key: API key input variable.
        options: General style options.
    """

    def __init__(self, root: object, handle_weather, config: object) -> None:
        """Class constructor.

        Args:
            root (object): The root window, Tk() instance.
            handle_weather (method): Handles redirect.
            config (object): Instance of ConfigService.
        """

        self.__root = root
        self.__frame = None
        self.__handle_weather = handle_weather
        self.__config = config
        self.__api_key = StringVar()
        self.__options = {'padx': 5, 'pady': 5}
        self.__initialize()

    def pack(self) -> None:
        """Pack widgets."""

        self.__frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self.__frame.destroy()

    def __handle_button_click(self) -> None:
        """Sets API key and handles redirect"""

        key = self.__api_key.get()
        self.__config.api_key = key
        self.__handle_weather()

    def __login(self) -> None:
        """Generates the login frame."""

        message = '''
No API key found!

Get a free API Key from https://openweathermap.org and
insert the key here'''

        label = ttk.Label(self.__frame, text=message)
        key_entry = ttk.Entry(self.__frame, textvariable=self.__api_key)

        button = ttk.Button(
            master=self.__frame,
            text="Set",
            command=self.__handle_button_click
        )

        label.grid(row=0, column=0, sticky=(
            constants.E, constants.W), **self.__options)
        key_entry.grid(row=1, column=0, sticky=(
            constants.E, constants.W), **self.__options)
        button.grid(row=2, column=0, sticky=(
            constants.E, constants.W), **self.__options)

    def __initialize(self) -> None:
        """Initializes the view."""

        self.__frame = ttk.Frame(master=self.__root)
        self.__login()
