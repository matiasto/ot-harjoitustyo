from tkinter import ttk, constants
from .details_frame import DetailsFrame
from services import IconService


class ForecastFrame:
    """Displays forecast.

    This Frame presents the forecast weather information
    devolved from the WeatherView.

    Managed by the WeatherView.

    Attributes:
        root: The root window for the frame.
        frame: The Frame instance.
        data: List of forecast entitys.
        details_frame: The frame that shows the details for
                       the selected day.
        icon_service: Service for retrieving the weather icons.
        options: General style options.
        icons: A list of all the active icons.
               Required for icon rendering.
    """

    def __init__(self, root: object, data: list) -> None:
        """Class constructor.

        Args:
            root (object): The root window.
            data (list): List of forecast days, 
                         each day is represented as a forecast entity.
        """

        self.__root = root
        self.__frame = None
        self.__data = data
        self.__details_frame = None
        self.__icon_service = IconService()
        self.__options = {'padx': 5, 'pady': 5}
        self.__icons = []
        self.__initialize()

    def pack(self) -> None:
        """Pack widgets."""

        self.__frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self.__frame.destroy()

    def __handle_details(self, index: int) -> None:
        """Manages the DetailsFrame.

        Selects the day and icon from the attributes and
        calls DetailsFrame update method.

        Args:
            index (int): Used to pinpoint the selected day.
        """

        self.__details_frame.update(self.__data[index], self.__icons[index])

    def __set_header(self) -> None:
        """Generates the forecast header."""

        forecast_header = ttk.Label(
            self.__frame, text="Forecast", font=("Arial", 25))
        forecast_header.grid(row=1, column=0)

    def __forecast(self) -> None:
        """Generates a row of forecast days.

        Each forecast day displays general information
        about that days forecast and a bind that opens the days detailed view
        in DetailsFrame.
        """

        for i, day in enumerate(self.__data):
            self.__icons.append(self.__icon_service.geticon(day.icon))
            label_frame = ttk.Labelframe(
                self.__frame, text="Click for details")

            time = ttk.Label(label_frame, text=day.time)
            icon = ttk.Label(label_frame, image=self.__icons[i])
            temp = ttk.Label(
                label_frame, text=f"{day.temperature_max} | {day.temperature_min} C")
            report = ttk.Label(label_frame, text=day.report)

            def handler(event, self=self, i=i):
                """The event handler

                Used in the bind function.
                Index points to clicked day.

                Args:
                    event: required, description of the event.
                    i: Index. Defaults to i. 
                       Used to retrieve the days data from attributes.
                """
                
                self.__handle_details(i)

            time.bind("<Button-1>", handler)
            icon.bind("<Button-1>", handler)
            temp.bind("<Button-1>", handler)
            report.bind("<Button-1>", handler)

            time.grid(row=1, column=0)
            icon.grid(row=2, column=0)
            temp.grid(row=3, column=0)
            report.grid(row=4, column=0)
            label_frame.bind("<Button-1>", handler)
            label_frame.grid(row=2, column=i, rowspan=4, **self.__options)

    def __initialize(self) -> None:
        """Intialize the frame."""

        self.__frame = ttk.Frame(master=self.__root)
        self.__details_frame = DetailsFrame(self.__frame)
        self.__set_header()
        self.__forecast()
        self.__handle_details(0)
