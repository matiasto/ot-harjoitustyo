from tkinter import ttk, constants, StringVar
from services import ConfigService


class LoginView:
    def __init__(self, root, handle_weather):
        self._root = root
        self._handle_weather = handle_weather
        self.__config = ConfigService()
        self._api_key = None
        self._frame = None
        self._options = {'padx': 5, 'pady': 5}

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_button_click(self):
        key = self._api_key.get()
        self.__config.api_key = key
        self._handle_weather()

    def _check_api(self):
        if self.__config.api_key_is_set():
            self._handle_weather()
        
    def _initialize(self):
        self._check_api()
        self._frame = ttk.Frame(master=self._root)
        self._api_key = StringVar()
        message = '''
No API key found!

Get a free API Key from https://openweathermap.org and
insert the key here'''

        label = ttk.Label(master=self._frame, text=message)
        key_entry = ttk.Entry(self._frame, textvariable=self._api_key)

        button = ttk.Button(
            master=self._frame,
            text="Set",
            command=self._handle_button_click
        )

        label.grid(row=0, column=0, sticky=(constants.E, constants.W), **self._options)
        key_entry.grid(row=1, column=0, sticky=(constants.E, constants.W), **self._options)
        button.grid(row=2, column=0, sticky=(constants.E, constants.W), **self._options)