from datetime import datetime


class Forecast:
    def __init__(self, data: dict) -> None:
        self.__time = datetime.fromtimestamp(data["dt"]).strftime("%A")
        self.__tempature_max = data["temp"]["max"]
        self.__tempature_min = data["temp"]["min"]
        self.__temperature = {"morn": data["temp"]["morn"], "day": data["temp"]
                              ["day"], "evening": data["temp"]["eve"], "night": data["temp"]["night"]}
        self.__feels_like = {"morn": data["feels_like"]["morn"], "day": data["feels_like"]
                             ["day"], "evening": data["feels_like"]["eve"], "night": data["feels_like"]["night"]}
        self.__wind_speed = data["wind_speed"]
        self.__wind_deg = None
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
    def temperature_max(self) -> float:
        return self.__tempature_max

    @property
    def temperature_min(self) -> float:
        return self.__tempature_min

    @property
    def temperature(self) -> dict:
        return self.__temperature

    @property
    def wind_speed(self) -> float:
        return self.__wind_speed

    @property
    def wind_deg(self) -> str:
        return self.__wind_deg

    @property
    def feels_like(self) -> dict:
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
