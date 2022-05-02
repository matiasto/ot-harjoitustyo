from tkinter import ttk, constants, StringVar


class NavbarFrame:
    def __init__(self, root, city, handle_get_weather):
        self.__root = root
        self.__frame = None
        self.__city = city
        self.__handle_get_weather = handle_get_weather
        self.__options = {'padx': 5, 'pady': 5}
        self.__initialize()

    def pack(self):
        self.__frame.pack(fill=constants.X)

    def destroy(self):
        self.__frame.destroy()

    def __handle_event(self):
        self.__handle_get_weather(self.__city.get())

    def __header(self):
        header = ttk.Label(
            self.__frame, text=f"Weather in {self.__city}", font=("Arial", 30))
        header.grid(row=0, column=7, columnspan=5,
                    sticky=(constants.S), padx=50)

    def __navbar(self):
        self.__city = StringVar(value=self.__city)
        label_frame = ttk.Labelframe(self.__frame)

        city_entry = ttk.Entry(
            label_frame, textvariable=self.__city, takefocus=True)
        get_weather_button = ttk.Button(
            label_frame,
            text='Search',
            command=self.__handle_event
        )

        city_entry.grid(column=0, row=0, sticky=constants.W, **self.__options)
        get_weather_button.grid(
            column=1, row=0, sticky=constants.W, **self.__options)
        label_frame.grid(row=0, column=0, columnspan=5, sticky=(constants.W))

    def __initialize(self):
        self.__frame = ttk.Frame(master=self.__root)
        self.__header()
        self.__navbar()
