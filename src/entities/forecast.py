from datetime import datetime


class Forecast:
    """Responsible for forecast data."""

    def __init__(self, data: dict) -> None:
        self.__time = datetime.fromtimestamp(data["dt"]).strftime("%A")
        self.__tempature_max = data["temp"]["max"]
        self.__tempature_min = data["temp"]["min"]
        self.__temperature = {
            "morning": data["temp"]["morn"],
            "day": data["temp"]["day"],
            "evening": data["temp"]["eve"],
            "night": data["temp"]["night"]
        }
        self.__feels_like = {
            "morning": data["feels_like"]["morn"],
            "day": data["feels_like"]["day"],
            "evening": data["feels_like"]["eve"],
            "night": data["feels_like"]["night"]
        }
        self.__wind_speed = data["wind_speed"]
        self.__wind_deg = None
        self.__sunrise = datetime.fromtimestamp(
            data["sunrise"]).strftime("%H:%M")
        self.__sunset = datetime.fromtimestamp(
            data["sunset"]).strftime("%H:%M")
        self.__uvi = data["uvi"]
        self.__report = data["weather"][0]["description"]
        self.__icon = data["weather"][0]["icon"]

        self.__deg_to_str(data["wind_deg"])

    def __deg_to_str(self, deg) -> None:
        """Converts degrees to cardinal form.

        e.g: "North East", "South", ...
        """

        value = int(deg / 45)
        lst = ["North", "North East", "East", "South East",
               "South", "South West", "West", "North West"]
        self.__wind_deg = lst[(value % 8)]

    @property
    def time(self) -> str:
        """Current time, UTC.

        Format "%A"
        i.e. "Tuesday".
        """

        return self.__time

    @property
    def temperature_max(self) -> float:
        """Forecast for maximum temperature during the day."""

        return self.__tempature_max

    @property
    def temperature_min(self) -> float:
        """Forecast for minimum temperature during the day."""

        return self.__tempature_min

    @property
    def temperature(self) -> dict:
        """Temperature for general parts of the day.

        Celsius.

        Returns:
            dict:
                "morning": _,
                "day": _,
                "evening":_,
                "night": _
        }
        """

        return self.__temperature

    @property
    def wind_speed(self) -> float:
        """Metre/sec."""

        return self.__wind_speed

    @property
    def wind_deg(self) -> str:
        """In Cardinal form eg. North East.

        Initially in degrees(meteorological)."""

        return self.__wind_deg

    @property
    def feels_like(self) -> dict:
        """Feels like for general parts of the day.

        Celsius.

        Returns:
            dict:
                "morning": _,
                "day": _,
                "evening":_,
                "night": _
        }
        """

        return self.__feels_like

    @property
    def sunrise(self) -> str:
        """Sunrise time, UTC.

        Format "%H:%M"
        i.e. "05:40".
        """

        return self.__sunrise

    @property
    def sunset(self) -> str:
        """Sunset time, UTC.

        Format "%H:%M"
        i.e. "19:40".
        """

        return self.__sunset

    @property
    def uvi(self) -> float:
        """UV index."""

        return self.__uvi

    @property
    def report(self) -> str:
        """Short description of the weather."""

        return self.__report

    @property
    def icon(self) -> str:
        """Weather icon id.

        Used to retrieve icons from the API."""

        return self.__icon
