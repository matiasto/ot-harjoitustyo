from tkinter import ttk, constants


class DetailsFrame:
    """Displays forecast details.

    This Frame presents the detailed information devolved from the ForecastFrame.

    Unlike the other frames, this class works as an
    extension to ForecastFrame. In practise, this means
    that instead of using the main TK() instance as the root window,
    this class uses the Frame instance of ForecastFrame object.

    Managed by the ForecastFrame.
    
    Attributes:
        frame: The Frame instance from ForecastFrame.
        current: current details frame.
        data: data for the frame. Recieves the day as a Forecast object.
        icon: Current icon as an ImageTk.PhotoImage object.
    """

    def __init__(self, frame: object) -> None:
        """Class constructor.

        Args:
            frame (object): Frame instance from ForecastFrame.
        """

        self.__frame = frame
        self.__current = None
        self.__data = None
        self.__icon = None
        self.__options = {'padx': 5, 'pady': 5}

    def __clear(self) -> None:
        """Clears the current details frame."""

        if self.__current:
            self.__current.grid_remove()

    def __set_general(self) -> None:
        """Generates the general widgets.
        
        These widgets display general information about the day.
        """

        time = ttk.Label(
            self.__current, text=f"{self.__data.time}", font=("Arial", 20))
        icon = ttk.Label(self.__current, image=self.__icon)
        temperature = ttk.Label(
            self.__current, text=f"High: {self.__data.temperature_max} C | Low: {self.__data.temperature_min} C", font=("Arial", 16))
        wind = ttk.Label(
            self.__current, text=f"Wind: {self.__data.wind_speed} m/s {self.__data.wind_deg}")
        day_length = ttk.Label(
            self.__current, text=f"Sunrise: {self.__data.sunrise}, Sunset: {self.__data.sunset}")
        uvi = ttk.Label(self.__current, text=f"UVI index: {self.__data.uvi}")
        report = ttk.Label(
            self.__current, text=f"{self.__data.report}", font=("Arial", 16))

        time.grid(row=0, column=0, columnspan=2)
        icon.grid(row=1, column=0, rowspan=2, columnspan=2)

        temperature.grid(row=0, column=3, columnspan=2,
                         sticky=constants.W, padx=30)
        wind.grid(row=1, column=3, columnspan=2, sticky=constants.W, padx=30)
        report.grid(row=2, column=3, columnspan=2, sticky=constants.W, padx=30)
        uvi.grid(row=3, column=3, columnspan=2, sticky=constants.W, padx=30)
        day_length.grid(row=4, column=3, columnspan=2,
                        sticky=constants.W, padx=30)

    def __set_table(self) -> None:
        """Generates the table.
        
        The table displays the temperature and 
        feels like values trough out the day.
        """

        temp_header = ttk.Label(self.__current, text="Temperature")
        feels_header = ttk.Label(self.__current, text="Feels like")

        temp_header.grid(row=2, column=9, sticky=constants.E)
        feels_header.grid(row=3, column=9, sticky=constants.E)

        for index, (key, value) in enumerate(self.__data.temperature.items(), start=12):
            header = ttk.Label(self.__current, text=key)
            temp = ttk.Label(self.__current, text=f"{value} C")
            feels = ttk.Label(
                self.__current, text=f"{self.__data.feels_like[key]} C")

            header.grid(row=1, column=index)
            temp.grid(row=2, column=index)
            feels.grid(row=3, column=index)

    def update(self, day: object, icon: object) -> None:
        """The method visible for ForecastFrame.
        
        This method updates the shown details.

        Args:
            day (dict): The data to be shown.
            icon (object): The weather icon as ImageTk.PhotoImage.
        """

        self.__clear()
        self.__data = day
        self.__icon = icon
        self.__current = ttk.Labelframe(self.__frame, text="Details")
        self.__set_general()
        self.__set_table()
        self.__current.grid(row=7, column=0, rowspan=4,
                            columnspan=15, sticky=constants.W, **self.__options)
