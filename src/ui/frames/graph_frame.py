from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.ticker import StrMethodFormatter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk, constants


class GraphFrame:
    """Displays the graph.

    This Frame, using matplotlib, plots the DataFrame data
    devolved from the WeatherView.

    Managed by the WeatherView.

    Attributes:
        root: The root window for the frame.
        frame: The Frame instance.
        graph: DataFrame object from Graph entity.
    """

    def __init__(self, root: object, data: object) -> None:
        """Class constructor.

        Args:
            root (object): the root TK() window
            data (object): DataFrame
        """

        self.__root = root
        self.__frame = None
        self.__graph = data
        self.__initialize()

    def pack(self) -> None:
        """Pack widgets."""

        self.__frame.pack(fill=constants.X)

    def destroy(self) -> None:
        """Destroy the frame."""

        self.__frame.destroy()

    def __set_header(self) -> None:
        """Generates the graph header."""

        header = ttk.Label(
            self.__frame, text="Weather Graph", font=("Ariel", 25))
        header.grid(row=12, column=0)

    def __plot_data(self) -> None:
        """Plots the data.

        x-axis: Time (Datetime).
        temperature: Red line(first y-axis).
        rain: Blue bar (second y-axis).
        vertical-line: Today.
        """

        fig = Figure(figsize=(15, 5), dpi=100)
        ax1 = fig.add_subplot()
        ax2 = ax1.twinx()

        ax1.plot(self.__graph.data[["temp"]], label="Temperature", color="red")
        ax2.bar(self.__graph.data.index.values,
                self.__graph.data["rain"], label="Rain", width=0.05, alpha=0.6)
        x_vert = datetime.today()
        ax1.axvline(x=x_vert, label="Today", color="green")

        ax1.margins(0.2)
        ax2.axis(ymin=0)

        ax1.set_title("Past 5 Days", loc="left", fontsize=16)
        ax1.set_title("Upcoming 2 days", loc="right", fontsize=16)
        ax1.yaxis.set_major_formatter("{x}??C")
        ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}mm'))

        h1, l1 = ax1.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        ax1.legend(h1+h2, l1+l2, loc="upper left")

        canvas = FigureCanvasTkAgg(fig, master=self.__frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=13, column=0, columnspan=15, pady=10)

    def __initialize(self) -> None:
        """Initializes the Frame."""

        self.__frame = ttk.Frame(master=self.__root)
        self.__set_header()
        self.__plot_data()
