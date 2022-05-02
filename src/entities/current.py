from datetime import datetime


class Current:
    def __init__(self, data: dict) -> None:
        self.__time = datetime.fromtimestamp(data["dt"]).strftime("%H:%M")
        self.__temperature = data["temp"]
        self.__wind_speed = data["wind_speed"]
        self.__wind_deg = None
        self.__feels_like = data["feels_like"]
        self.__sunrise = datetime.fromtimestamp(data["sunrise"]).strftime("%H:%M")
        self.__sunset = datetime.fromtimestamp(data["sunset"]).strftime("%H:%M")
        self.__uvi = data["uvi"]
        self.__report = data["weather"][0]["description"]
        self.__icon = data["weather"][0]["icon"]

        self.__deg_to_str(data["wind_deg"])

    def __deg_to_str(self, deg) -> None:
        value = int(deg / 45)
        lst = ["North", "North East", "East", "South East", "South", "South West", "West", "North West"]
        self.__wind_deg = lst[(value % 8)]

    @property
    def time(self) -> object:
        return self.__time

    @property
    def temperature(self) -> float:
        return self.__temperature

    @property
    def wind_speed(self) -> float:
        return self.__wind_speed

    @property
    def wind_deg(self) -> str:
        return self.__wind_deg

    @property
    def feels_like(self) -> float:
        return self.__feels_like

    @property
    def sunrise(self) -> object:
        return self.__sunrise

    @property
    def sunset(self) -> object:
        return self.__sunset
        
    @property
    def uvi(self) -> int:
        return self.__uvi

    @property
    def report(self) -> str:
        return self.__report

    @property
    def icon(self) -> str:
        return self.__icon
