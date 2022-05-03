from datetime import datetime
from pandas import DataFrame


class Graph:
    """Responsible for graph data.

    Temperature and rain from past 120h (5 days) and upcoming 48h (2 days)
    is combined into one dataframe.

    Attributes:
        data: DataFrame object, where each row represents an hour.

        Example row includes datetime object as the index,
        "temp" column, and a "rain" column.
    """

    def __init__(self, data: list) -> None:
        """Class constructor.

        Args:
            data (list): List of "hours". each hour is a dictionary
                        representing weather conditions.
        """
        self.__data = None
        self.__parse(data)

    @property
    def data(self) -> object:
        """Graphs DataFrame."""

        return self.__data

    def __sort_data(self):
        """Uses datetime as primary key."""

        self.__data = self.__data.set_index("time")
        self.__data = self.__data.sort_index()

    def __parse(self, data: list) -> None:
        """Filters data and creates the DataFrame."""

        parsed_data = {"time": [], "temp": [], "rain": []}
        for hour in data:
            parsed_data["time"].append(datetime.fromtimestamp(hour["dt"]))
            parsed_data["temp"].append(hour["temp"])
            if "rain" in hour:
                parsed_data["rain"].append(hour["rain"]["1h"])
            else:
                parsed_data["rain"].append(0)
        self.__data = DataFrame.from_dict(parsed_data)
        self.__sort_data()
