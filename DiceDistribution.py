# from tkinter import *
# from itertools import product
# from collections import Counter
# from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# from matplotlib.figure import Figure
from Plotter import Plotter
from UI import Ui

max_dice = 5
geometry_size = '750x600'


def main():
    plot_manager = Plotter()
    ui_manager = Ui(max_dice, geometry_size, plot_manager)
    ui_manager.setup_ui()


if __name__ == "__main__":
    main()
