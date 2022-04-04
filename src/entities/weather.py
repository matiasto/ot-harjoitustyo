
class WeatherNow:
    """Class for representing current weather"""

    def __init__(self, city_name: str, data: dict):
        self.__city_name = city_name
        self.__temperature = None
        self.__humidity = None
        self.__pressure = None
        self.__report = None
        self.__parse_data(data)

    @property
    def city_name(self):
        return self.__city_name

    @property
    def temperature(self):
        return self.__temperature

    @property
    def humidity(self):
        return self.__humidity

    @property
    def pressure(self):
        return self.__pressure

    @property
    def report(self):
        return self.__report

    def __parse_data(self, data: dict):
        main = data['main']
        self.__temperature = main['temp']
        self.__humidity = main['humidity']
        self.__pressure = main['pressure']
        self.__report = data['weather'][0]
