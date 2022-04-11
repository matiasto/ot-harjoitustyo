from datetime import datetime

class Day:
    def __init__(self, data: dict):
        self.__time = datetime.fromtimestamp(data["dt"]).strftime("%A")
        self.__temperature = data["temp"]["day"]
        self.__report = data["weather"]["description"]
        self.__icon = data["weather"]["icon"]

    @property
    def time(self):
        return self.__time

    @property
    def temperature(self):
        return self.__temperature

    @property
    def report(self):
        return self.__report

    @property
    def icon(self):
        return self.__icon