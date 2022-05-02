from tkinter import ttk, constants


class DetailsWidget:
    def __init__(self, frame):
        self.__frame = frame
        self.__current = None
        self.__data = None
        self.__icon = None
        self.__options = {'padx': 5, 'pady': 5}

    def __clear(self):
        if self.__current:
            self.__current.grid_remove()

    def __set_general(self):
        time = ttk.Label(
            self.__current, text=f"{self.__data.time}", font=("Arial", 20))
        icon = ttk.Label(self.__current, image=self.__icon)
        temperature = ttk.Label(
            self.__current, text=f"High: {self.__data.temperature_max} C | Low: {self.__data.temperature_min} C", font=("Arial", 16))
        wind = ttk.Label(self.__current, text=f"Wind: {self.__data.wind_speed} m/s {self.__data.wind_deg}")
        day_length = ttk.Label(self.__current, text=f"Sunrise: {self.__data.sunrise}, Sunset: {self.__data.sunset}")
        uvi = ttk.Label(self.__current, text=f"UVI index: {self.__data.uvi}")
        report = ttk.Label(self.__current, text=f"{self.__data.report}", font=("Arial", 16))

        time.grid(row=0, column=0, columnspan=2)
        icon.grid(row=1, column=0, rowspan=2,columnspan=2)

        temperature.grid(row=0, column=3, columnspan=2, sticky=constants.W, padx=30)
        wind.grid(row=1, column=3, columnspan=2, sticky=constants.W, padx=30)
        report.grid(row=2, column=3, columnspan=2, sticky=constants.W, padx=30)
        uvi.grid(row=3, column=3, columnspan=2, sticky=constants.W, padx=30)
        day_length.grid(row=4, column=3, columnspan=2, sticky=constants.W, padx=30)

    def __set_table(self):
        temp_header = ttk.Label(self.__current, text="Temperature")
        feels_header = ttk.Label(self.__current, text="Feels like")

        temp_header.grid(row=2, column=9, sticky=constants.E)
        feels_header.grid(row=3, column=9, sticky=constants.E)

        for index, (key, value) in enumerate(self.__data.temperature.items(), start=12):
            header = ttk.Label(self.__current, text=key)
            temp = ttk.Label(self.__current, text=f"{value} C")
            feels = ttk.Label(self.__current, text=f"{self.__data.feels_like[key]} C")

            header.grid(row=1, column=index)
            temp.grid(row=2, column=index)
            feels.grid(row=3, column=index)
        

    def update(self, day, icon):
        self.__clear()
        self.__data = day
        self.__icon = icon
        self.__current = ttk.Labelframe(self.__frame, text="Details")
        self.__set_general()
        self.__set_table()
        self.__current.grid(row=7, column=0, rowspan=4, columnspan=15, sticky=constants.W, **self.__options)
