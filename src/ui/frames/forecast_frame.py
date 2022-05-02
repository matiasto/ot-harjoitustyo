from tkinter import font, ttk, constants
from .details_frame import DetailsFrame
from services import IconService


class ForecastFrame:
    def __init__(self, root, data):
        self.__root = root
        self.__frame = None
        self.__data = data
        self.__details_frame = None
        self.__icon_service = IconService()
        self.__options = {'padx': 5, 'pady': 5}
        self.__icons = []
        self.__initialize()

    def pack(self):
        self.__frame.pack(fill=constants.X)

    def destroy(self):
        self.__frame.destroy()

    def __handle_details(self, index):
        self.__details_frame.update(self.__data[index], self.__icons[index])

    def __set_header(self):
        forecast_header = ttk.Label(self.__frame, text="Forecast", font=("Arial", 25))
        forecast_header.grid(row=1, column=0)

    def __forecast(self):
        for i, day in enumerate(self.__data):
            self.__icons.append(self.__icon_service.geticon(day.icon))
            label_frame = ttk.Labelframe(self.__frame, text="Click for details")

            time = ttk.Label(label_frame, text=day.time)
            icon = ttk.Label(label_frame, image=self.__icons[i])
            temp = ttk.Label(label_frame, text=f"{day.temperature_max} | {day.temperature_min} C")
            report = ttk.Label(label_frame, text=day.report)

            def handler(event, self=self, i=i):
                self.__handle_details(i)

            time.bind("<Button-1>", handler)
            icon.bind("<Button-1>", handler)
            temp.bind("<Button-1>", handler)
            report.bind("<Button-1>", handler)

            time.grid(row=1, column=0)
            icon.grid(row=2, column=0)
            temp.grid(row=3, column=0)
            report.grid(row=4, column=0)
            label_frame.bind("<Button-1>", handler)
            label_frame.grid(row=2, column=i, rowspan=4, **self.__options)

    def __initialize(self):
        self.__frame = ttk.Frame(master=self.__root)
        self.__details_frame = DetailsWidget(self.__frame)
        self.__set_header()
        self.__forecast()
        self.__handle_details(0)
