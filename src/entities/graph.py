from datetime import datetime
from pandas import DataFrame


class Graph:
    def __init__(self, data: list) -> None:
        self.__data = None
        self.__parse(data)

    @property
    def data(self) -> object:
        return self.__data

    def __sort_data(self):
        self.__data = self.__data.set_index('time')
        self.__data = self.__data.sort_index()

    def __parse(self, data: list) -> None:
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
