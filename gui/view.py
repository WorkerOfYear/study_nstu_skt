import numpy as np

from magnetic_survey import calculation_B
from magnetic_survey import calculation_P
from reader import read_ini
from visual import get_plot

from .model import Panel, Canvas, Ini, MagnField, Cache
from .frames import *


def direct():
    get_var1()
    get_var2()
    ini = Ini.obj
    ini.init_cells()
    ini.fill_p_nonzero()
    ini.init_receivers()
    ini.volume_cells()

    b_direct_x, b_direct_y, b_direct_z, L = calculation_B(ini)

    MagnField.b_direct_x = b_direct_x
    MagnField.b_direct_y = b_direct_y
    MagnField.b_direct_z = b_direct_z
    MagnField.L = L
    Canvas.delete_canvas()


def inverse():
    ini = Ini.obj

    P_res = calculation_P(MagnField.b_direct_x, MagnField.b_direct_y,
                          MagnField.b_direct_z, MagnField.L, ini)
    
    fig = get_plot(ini, np.round(P_res, 2))
    Canvas.set_canvas(fig)


def set_frame1():
    ini = Ini.obj
    var = Cache.var1
    but = Cache.but1

    var['x_start_val'].set(ini.x_start)
    var['x_end_val'].set(ini.x_end)
    var['y_start_val'].set(ini.y_start)
    var['y_end_val'].set(ini.y_end)
    var['z_start_val'].set(ini.z_start)
    var['z_end_val'].set(ini.z_end)

    var['count_x'].set(ini.count_x)
    var['count_z'].set(ini.count_z)

    var['x_rec_start'].set(ini.x_rec_start)
    var['x_rec_end'].set(ini.x_rec_end)
    var['n_receivers'].set(ini.n_receivers)
    var['z_rec_val'].set(ini.z_rec)

    var['I_val'].set(ini.I)

    var['P_val'].set(ini.p_val)
    var['p_rectangle_start'].set(ini.p_rectangle_start)
    var['p_rectangle_width'].set(ini.p_rectangle_width)
    var['p_rectangle_heigth'].set(ini.p_rectangle_heigth)

    but['btn_direct_task']['command'] = direct



def set_frame2():
    ini = Ini.obj
    var = Cache.var2
    but = Cache.but2

    var['gamma_start_value'].set(ini.initial_gamma)
    but['btn_solve_back_task']['command'] = inverse


def get_var1():
    ini = Ini.obj
    var = Cache.var1
    but = Cache.but1

    ini.x_start = float(var['x_start_val'].get())
    ini.x_end = float(var['x_end_val'].get())
    ini.y_start = float(var['y_start_val'].get())
    ini.y_end = float(var['y_end_val'].get())
    ini.z_start = float(var['z_start_val'].get())
    ini.v = float(var['z_end_val'].get())

    ini.count_x = int(var['count_x'].get())
    ini.count_z = int(var['count_z'].get())

    ini.x_rec_start = float(var['x_rec_start'].get())
    ini.x_rec_end = float(var['x_rec_end'].get())
    ini.n_receivers = int(var['n_receivers'].get())
    ini.z_rec = float(var['z_rec_val'].get())

    ini.I = float(var['I_val'].get())

    ini.p_val = float(var['P_val'].get())
    ini.p_rectangle_start = int(var['p_rectangle_start'].get())
    ini.p_rectangle_width = int(var['p_rectangle_width'].get())
    ini.p_rectangle_heigth = int(var['p_rectangle_heigth'].get())


def get_var2():
    ini = Ini.obj
    var = Cache.var2
    but = Cache.but2

    ini.initial_gamma = float(var['gamma_start_value'].get())


def start_programm():
    ini = Ini.obj
    panel = Panel.obj

    var1, but1 = get_frame1(panel, ini)
    var2, but2 = get_frame2(panel, ini)
    var3, but3 = get_frame3(panel, ini)

    Cache.var1 = var1
    Cache.but1 = but1

    Cache.var2 = var2
    Cache.but2 = but2

    Cache.var3 = var3
    Cache.but3 = but3

    set_frame1()
    set_frame2()
