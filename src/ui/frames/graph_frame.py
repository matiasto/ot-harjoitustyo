from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.ticker import StrMethodFormatter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk, constants


class GraphFrame:
    def __init__(self, root, data):
        self.__root = root
        self.__frame = None
        self.__graph = data
        self.__initialize()

    def pack(self):
        self.__frame.pack(fill=constants.X)

    def destroy(self):
        self.__frame.destroy()

    def __plot_data(self):
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
        ax1.yaxis.set_major_formatter("{x}°C")
        ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}mm'))

        h1, l1 = ax1.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        ax1.legend(h1+h2, l1+l2, loc="upper left")

        canvas = FigureCanvasTkAgg(fig, master=self.__frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=5, column=0, columnspan=15)

    def __initialize(self):
        self.__frame = ttk.Frame(master=self.__root)
        self.__plot_data()
