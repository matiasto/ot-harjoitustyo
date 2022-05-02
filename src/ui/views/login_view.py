from tkinter import ttk, constants, StringVar


class LoginView:
    def __init__(self, root, handle_weather, config):
        self.__root = root
        self.__handle_weather = handle_weather
        self.__config = config
        self.__frame = None
        self.__api_key = StringVar()
        self.__options = {'padx': 5, 'pady': 5}
        self.__initialize()

    def pack(self):
        self.__frame.pack(fill=constants.X)

    def destroy(self):
        self.__frame.destroy()

    def __handle_button_click(self):
        key = self.__api_key.get()
        self.__config.api_key = key
        self.__handle_weather()

    def __login(self):
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

    def __initialize(self):
        self.__frame = ttk.Frame(master=self.__root)
        self.__login()
