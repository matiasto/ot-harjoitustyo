from tkinter import ttk, constants
from services import IconService


class CurrentFrame:
    def __init__(self, root, data):
        self.__root = root
        self.__frame = None
        self.__data = data
        self.__icon_service = IconService()
        self.__options = {'padx': 5, 'pady': 5}
        self.__icon = None
        self.__initialize()

    def pack(self):
        self.__frame.pack(fill=constants.X)

    def destroy(self):
        self.__frame.destroy()

    def __current(self):
        self.__icon = self.__icon_service.geticon(self.__data.icon)
        label_frame = ttk.Labelframe(self.__frame)
        time = ttk.Label(
            label_frame, text=f"Today at {self.__data.time}", font=("Arial", 25))
        icon = ttk.Label(label_frame, image=self.__icon)
        temp = ttk.Label(
            label_frame, text=f"{self.__data.temperature} C", font=("Arial", 16))
        wind = ttk.Label(
            label_frame, text=f"Wind: {self.__data.wind_speed} m/s {self.__data.wind_deg}")
        feels_like = ttk.Label(
            label_frame, text=f"Feels like: {self.__data.feels_like} C")
        day_length = ttk.Label(
            label_frame, text=f"Sunrise: {self.__data.sunrise}, Sunset: {self.__data.sunset}")
        uvi = ttk.Label(label_frame, text=f"UVI index: {self.__data.uvi}")
        report = ttk.Label(
            label_frame, text=f"{self.__data.report}", font=("Arial", 16))

        time.grid(row=0, column=0, columnspan=3)
        icon.grid(row=1, column=0, rowspan=3, columnspan=3)

        temp.grid(row=0, column=4, rowspan=2, columnspan=2, padx=30)
        report.grid(row=2, column=4, rowspan=2, columnspan=2, padx=30)

        wind.grid(row=0, column=10, columnspan=4, sticky=constants.E)
        feels_like.grid(row=1, column=10, columnspan=4, sticky=constants.E)
        day_length.grid(row=2, column=10, columnspan=4, sticky=constants.E)
        uvi.grid(row=3, column=10, columnspan=4, sticky=constants.E)

        label_frame.grid(row=1, column=0, rowspan=4,
                         columnspan=15, **self.__options)

    def __initialize(self):
        self.__frame = ttk.Frame(master=self.__root)
        self.__current()
