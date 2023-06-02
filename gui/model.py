import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


class Cache:
    pass


class MagnField:
    pass


class Ini:
    obj = None

    @staticmethod
    def init_ini(ini):
        Ini.obj = ini


class Panel:
    obj = None

    @staticmethod
    def init_panel(panel):
        Panel.obj = panel

    @staticmethod
    def set_panel(ini):
        pass


class Canvas:
    obj = None

    @staticmethod
    def init_canvas(canvas):
        Canvas.obj = canvas

    @staticmethod
    def set_canvas(fig):
        
        canv = FigureCanvasTkAgg(fig, master=Canvas.obj)
        canv.draw()
        canv.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE, expand=0)
        toolbar = NavigationToolbar2Tk(canv, Canvas.obj)
        toolbar.update()
        canv.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        

    @staticmethod
    def delete_canvas():
        pass
