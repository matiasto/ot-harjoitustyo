from io import BytesIO
from tkinter import ttk, constants
from PIL import Image, ImageTk
import requests


class WeatherFrame:
    def __init__(self, root, data):
        self._root = root
        self._frame = None
        self._current_data = data.current
        self._forecast_data = data.forecast
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

    def _current(self):
        self._icons.append(self._geticon(self._current_data.icon))
        label_frame = ttk.Labelframe(self._frame)
        time = ttk.Label(
            label_frame, text=f"Today at {self._current_data.time}")
        icon = ttk.Label(label_frame, image=self._icons[0])
        temp = ttk.Label(
            label_frame, text=f"{self._current_data.temperature} C")
        report = ttk.Label(label_frame, text=f"{self._current_data.report}")

        time.grid(row=1, column=0)
        icon.grid(row=2, column=0)
        temp.grid(row=3, column=0)
        report.grid(row=4, column=0)
        label_frame.grid(row=1, column=0, rowspan=4, **self._options)

    def _forecast(self):
        for i, day in enumerate(self._forecast_data, start=1):
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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._current()
        self._forecast()
