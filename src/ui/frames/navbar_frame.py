from tkinter import ttk, constants, StringVar


class NavbarFrame:
    def __init__(self, root, city, handle_get_weather):
        self._root = root
        self._frame = None
        self._city = city
        self._handle_get_weather = handle_get_weather
        self._options = {'padx': 5, 'pady': 5}
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_event(self):
        self._handle_get_weather(self._city.get())

    def _header(self):
        header = ttk.Label(
            self._frame, text=f"Weather in {self._city}", font=("Arial", 30))
        header.grid(row=0, column=7, columnspan=5,
                    sticky=(constants.S), padx=50)

    def _navbar(self):
        self._city = StringVar(value=self._city)
        label_frame = ttk.Labelframe(self._frame)

        city_entry = ttk.Entry(
            label_frame, textvariable=self._city, takefocus=True)
        get_weather_button = ttk.Button(
            label_frame,
            text='Search',
            command=self._handle_event
        )

        city_entry.grid(column=0, row=0, sticky=constants.W, **self._options)
        get_weather_button.grid(column=1, row=0, sticky=constants.W)
        label_frame.grid(row=0, column=0, columnspan=5, sticky=(constants.W))

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._header()
        self._navbar()
