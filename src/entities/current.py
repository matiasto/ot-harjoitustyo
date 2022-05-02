from datetime import datetime


class Current:
    """Responsible for current weather data."""

    def __init__(self, data: dict) -> None:
        self.__time = datetime.fromtimestamp(data["dt"]).strftime("%H:%M")
        self.__temperature = data["temp"]
        self.__wind_speed = data["wind_speed"]
        self.__wind_deg = None
        self.__feels_like = data["feels_like"]
        self.__sunrise = datetime.fromtimestamp(
            data["sunrise"]).strftime("%H:%M")
        self.__uvi = data["uvi"]
        self.__sunset = datetime.fromtimestamp(
            data["sunset"]).strftime("%H:%M")
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
    def time(self) -> object:
        """Current time, UTC
        
        Datetime object
        """

        return self.__time

    @property
    def temperature(self) -> float:
        """In Celsius degrees."""

        return self.__temperature

    @property
    def wind_deg(self) -> str:
        """In Cardinal form eg. North East.

        Initially in degrees(meteorological)."""

        return self.__wind_deg

    @property
    def wind_speed(self) -> float:
        """Metre/sec."""

        return self.__wind_speed

    @property
    def feels_like(self) -> float:
        """Accounts for the human perception of weather.
        
        Celsius degrees.
        """
        return self.__feels_like

    @property
    def sunrise(self) -> object:
        """Sunrise time, UTC.
        
        Datetime object.
        """

        return self.__sunrise

    @property
    def sunset(self) -> object:
        """Sunset time, UTC.

        Datetime object.
        """

        return self.__sunset

    @property
    def uvi(self) -> int:
        """Current UV index."""

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
