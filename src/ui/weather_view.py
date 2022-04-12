from cgitb import text
from io import BytesIO
from time import time
from tkinter import ttk, constants, StringVar
from PIL import Image, ImageTk
import requests
from services import WeatherService


class WeatherView:
    def __init__(self, root):
        self._root = root
        self._weather = WeatherService()
        self._frame = None
        self._city = None
        self._options = {'padx': 5, 'pady': 5}
        self._icons = []
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _geticon(self, iconcode):
        url = "http://openweathermap.org/img/wn/" + iconcode + "@2x.png"
        response_img = requests.get(url)
        raw_data = response_img.content
        img_data = Image.open(BytesIO(raw_data))
        img = ImageTk.PhotoImage(img_data)
        return img

    def _set_header(self, city_name):
        header = ttk.Label(
            self._frame, text=f"Weather in {city_name}", font=("Arial", 25))
        header.grid(row=0, column=3, columnspan=5, sticky=(constants.W))

    def _current(self, current):
        self._icons.append(self._geticon(current.icon))
        label_frame = ttk.Labelframe(self._frame)
        time = ttk.Label(label_frame, text=f"Today at {current.time}")
        icon = ttk.Label(label_frame, image=self._icons[0])
        temp = ttk.Label(label_frame, text=f"{current.temperature} C")
        report = ttk.Label(label_frame, text=f"{current.report}")

        time.grid(row=1, column=0)
        icon.grid(row=2, column=0)
        temp.grid(row=3, column=0)
        report.grid(row=4, column=0)
        label_frame.grid(row=1, column=0, rowspan=4, **self._options)

    def _forecast(self, forecast):
        for i, day in enumerate(forecast, start=1):
            self._icons.append(self._geticon(day.icon))
            label_frame = ttk.Labelframe(self._frame)
            time = ttk.Label(label_frame, text=day.time)
            image = ttk.Label(label_frame, image=self._icons[i])
            temp = ttk.Label(label_frame, text=f"{day.temperature} C")
            report = ttk.Label(label_frame, text=day.report)

            time.grid(row=1, column=0)
            image.grid(row=2, column=0)
            temp.grid(row=3, column=0)
            report.grid(row=4, column=0)

            label_frame.grid(row=1, column=i, rowspan=4, **self._options)

    def _get_weather(self):
        city = self._city.get()
        data = self._weather.weather(city)
        for item in self._frame.winfo_children():
            item.destroy()
        self._navbar(city)
        self._frame.grid_forget()
        self._set_header(city)
        self._current(data.current)
        self._forecast(data.forecast)

    def _navbar(self, city):
        self._city = StringVar(value=city)
        label_frame = ttk.Labelframe(self._frame)

        city_entry = ttk.Entry(
            label_frame, textvariable=self._city, takefocus=True)
        get_weather_button = ttk.Button(
            label_frame,
            text='Search',
            command=self._get_weather
        )

        city_entry.grid(column=0, row=0, sticky=constants.W, **self._options)
        get_weather_button.grid(column=1, row=0, sticky=constants.W)
        label_frame.grid(row=0, column=0, columnspan=5, sticky=(constants.W))

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._navbar("Helsinki")
        self._get_weather()
