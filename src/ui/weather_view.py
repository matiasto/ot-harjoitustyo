from tkinter import ttk, constants, StringVar
from services import Weather


class WeatherView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._city = None
        self._options = {'padx': 5, 'pady': 5}
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def get_weather(self):
        weather = Weather()
        data = weather.current_weather(self._city.get())

        self.result_label_city.config(text=data.city_name)
        temp_result = f"Lämpötila: {data.temperature} C"
        self.result_label_temp.config(text=temp_result)
        humidity_result = f"Ilmankosteus: {data.humidity} %"
        self.result_label_humidity.config(text=humidity_result)
        pressure_result = f"Ilmanpaine: {data.pressure} hPa"
        self.result_label_pressure.config(text=pressure_result)
        report_result = f"Tiedote: {data.report}"
        self.result_label_report.config(text=report_result)

        
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._city = StringVar()
        self.city_label = ttk.Label(master=self._frame, text="City")
        self.city_label.grid(column=0, row=0, sticky=constants.W, **self._options)
        
        self.city_entry = ttk.Entry(self._frame, textvariable=self._city)

        self.result_label_city = ttk.Label(self._frame)
        self.result_label_temp = ttk.Label(self._frame)
        self.result_label_humidity = ttk.Label(self._frame)
        self.result_label_pressure = ttk.Label(self._frame)
        self.result_label_report = ttk.Label(self._frame)

        self.get_weather_button = ttk.Button(
            self._frame, 
            text='Current Weather',
            command=self.get_weather
        )
        self.city_entry.grid(column=1, row=0, sticky=constants.W, **self._options)
        self.get_weather_button.grid(column=2, row=0, sticky=constants.W)
        self.result_label_city.grid(row=1, columnspan=3, **self._options)
        self.result_label_temp.grid(row=2, columnspan=3, **self._options)
        self.result_label_humidity.grid(row=3, columnspan=3, **self._options)
        self.result_label_pressure.grid(row=4, columnspan=3, **self._options)
        self.result_label_report.grid(row=5, columnspan=3, **self._options)
    