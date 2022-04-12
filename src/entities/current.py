from datetime import datetime


class Current:
    def __init__(self, data: dict):
        self.__time = datetime.fromtimestamp(data["dt"]).strftime("%H:%M")
        self.__temperature = data["temp"]
        self.__report = data["weather"][0]["description"]
        self.__icon = data["weather"][0]["icon"]

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