from io import BytesIO
from tkinter import ttk, constants
from PIL import Image, ImageTk
import requests


class WeatherFrame:
    def __init__(self, root, data):
        self.__root = root
        self.__frame = None
        self.__current_data = data.current
        self.__forecast_data = data.forecast
        self.__options = {'padx': 5, 'pady': 5}
        self.__icons = []
        self.__initialize()

    def pack(self):
        self.__frame.pack(fill=constants.X)

    def destroy(self):
        self.__frame.destroy()

    def __geticon(self, iconcode):
        url = "http://openweathermap.org/img/wn/" + iconcode + "@2x.png"
        response_img = requests.get(url)
        raw_data = response_img.content
        img_data = Image.open(BytesIO(raw_data))
        img = ImageTk.PhotoImage(img_data)
        return img

    def __current(self):
        self.__icons.append(self.__geticon(self.__current_data.icon))
        label_frame = ttk.Labelframe(self.__frame)
        time = ttk.Label(
            label_frame, text=f"Today at {self.__current_data.time}")
        icon = ttk.Label(label_frame, image=self.__icons[0])
        temp = ttk.Label(
            label_frame, text=f"{self.__current_data.temperature} C")
        report = ttk.Label(label_frame, text=f"{self.__current_data.report}")

        time.grid(row=1, column=0)
        icon.grid(row=2, column=0)
        temp.grid(row=3, column=0)
        report.grid(row=4, column=0)
        label_frame.grid(row=1, column=0, rowspan=4, **self.__options)

    def __forecast(self):
        for i, day in enumerate(self.__forecast_data, start=1):
            self.__icons.append(self.__geticon(day.icon))
            label_frame = ttk.Labelframe(self.__frame)
            time = ttk.Label(label_frame, text=day.time)
            image = ttk.Label(label_frame, image=self.__icons[i])
            temp = ttk.Label(label_frame, text=f"{day.temperature} C")
            report = ttk.Label(label_frame, text=day.report)

            time.grid(row=1, column=0)
            image.grid(row=2, column=0)
            temp.grid(row=3, column=0)
            report.grid(row=4, column=0)

            label_frame.grid(row=1, column=i, rowspan=4, **self.__options)

    def __initialize(self):
        self.__frame = ttk.Frame(master=self.__root)
        self.__current()
        self.__forecast()
