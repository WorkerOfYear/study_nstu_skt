import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np

def get_interface(ini, fig):

    WIN_H=600
    WIN_W=900
    PANEL_H=WIN_H
    PANEL_W=450
    CANVAS_H=WIN_H
    CANVAS_W=WIN_W-PANEL_W

    win = tk.Tk()


    # photo = tk.PhotoImage(file='fpmi_full.png')
    # win.iconphoto(False, photo)
    win.title('Обработка данных магниторазведки')
    win.geometry(f'{WIN_W}x{WIN_H}+100+100')

    win.resizable(False, False)
    win.config(bg='#fff')

    canvas=tk.Canvas(win, width=CANVAS_W, height=CANVAS_H, bg='#fff')
    canvas.place(x=PANEL_W, y=0, width=CANVAS_W, height=CANVAS_W)

    canvas1 = FigureCanvasTkAgg(fig, master = canvas)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE, expand=0)


    panel=tk.Frame(win, width=PANEL_W, height=PANEL_H, bd=0, relief=tk.GROOVE)
    panel.place(x=0, y=0, width=PANEL_W, height=PANEL_H)

    frame1 = tk.LabelFrame(panel, text='Прямая задача')
    frame1.grid(row=0, column=0, ipadx=10, ipady=1, padx=10, pady=10)

    lablel_1 = tk.Label(frame1, text='Ячеистая структура')
    lablel_1.grid(row=0, column=0, columnspan=2, sticky='ew')

    lablel_1 = tk.Label(frame1, text='x_start')
    lablel_1.grid(row=0+1, column=0)

    lablel_2 = tk.Label(frame1, text='x_end')
    lablel_2.grid(row=0+1, column=1)

    x_start_val = tk.StringVar(frame1)
    entry_1 = tk.Entry(frame1, textvariable=x_start_val)
    entry_1.grid(row=1+1, column=0)

    x_end_val = tk.StringVar(frame1)
    entry_2 = tk.Entry(frame1, textvariable=x_end_val)
    entry_2.grid(row=1+1, column=1)


    lablel_3 = tk.Label(frame1, text='y_start')
    lablel_3.grid(row=2+1, column=0)

    lablel_4 = tk.Label(frame1, text='y_end')
    lablel_4.grid(row=2+1, column=1)

    y_start_val = tk.StringVar(frame1)
    entry_3 = tk.Entry(frame1, textvariable=y_start_val)
    entry_3.grid(row=3+1, column=0)

    y_end_val = tk.StringVar(frame1)
    entry_4 = tk.Entry(frame1, textvariable=y_end_val)
    entry_4.grid(row=3+1, column=1)


    lablel_5 = tk.Label(frame1, text='z_start')
    lablel_5.grid(row=4+1, column=0)

    lablel_6 = tk.Label(frame1, text='z_end')
    lablel_6.grid(row=4+1, column=1)

    z_start_val = tk.StringVar(frame1)
    entry_5 = tk.Entry(frame1, textvariable=z_start_val)
    entry_5.grid(row=5+1, column=0)

    z_end_val = tk.StringVar(frame1)
    entry_6 = tk.Entry(frame1, textvariable=z_end_val)
    entry_6.grid(row=5+1, column=1)


    lablel_7 = tk.Label(frame1, text='Приёмники')
    lablel_7.grid(row=0, column=2, columnspan=2, sticky='ew')

    lablel_8 = tk.Label(frame1, text='x_start')
    lablel_8.grid(row=1, column=2)

    lablel_9 = tk.Label(frame1, text='x_end')
    lablel_9.grid(row=1, column=3)

    x_rec_start = tk.StringVar(frame1)
    entry_8 = tk.Entry(frame1, textvariable=x_rec_start)
    entry_8.grid(row=2, column=2)

    x_rec_end = tk.StringVar(frame1)
    entry_9 = tk.Entry(frame1, textvariable=x_rec_end)
    entry_9.grid(row=2, column=3)


    l_n_cells = tk.Label(frame1, text='Колличество ячеек')
    l_n_cells.grid(row=7, column=0, columnspan=2, sticky='ew')

    l_ncellsx = tk.Label(frame1, text='по x')
    l_ncellsx.grid(row=8, column=0)

    l_ncellsz = tk.Label(frame1, text='по z')
    l_ncellsz.grid(row=8, column=1)

    count_x = tk.StringVar(frame1)
    e_ncellsx = tk.Entry(frame1, textvariable=count_x)
    e_ncellsx.grid(row=9, column=0)

    count_z = tk.StringVar(frame1)
    e_ncellsz = tk.Entry(frame1, textvariable=count_z)
    e_ncellsz.grid(row=9, column=1)


    l_n_rec = tk.Label(frame1, text='Колличество приёмников')
    l_n_rec.grid(row=3, column=2, columnspan=2, sticky='ew')

    n_receivers = tk.StringVar(frame1)
    e_n_rec = tk.Entry(frame1, textvariable=n_receivers)
    e_n_rec.grid(row=4, column=2, columnspan=2)

    l_z_rec = tk.Label(frame1, text='Уровень приёмников z')
    l_z_rec.grid(row=5, column=2, columnspan=2, sticky='ew')

    z_rec_val = tk.StringVar(frame1)
    e_n_rec = tk.Entry(frame1, textvariable=z_rec_val)
    e_n_rec.grid(row=6, column=2, columnspan=2)

    l_I = tk.Label(frame1, text='Мощность источника, Вт')
    l_I.grid(row=7, column=2, columnspan=2, sticky='ew')

    I_val = tk.StringVar(frame1)
    e_I = tk.Entry(frame1, textvariable=I_val)
    e_I.grid(row=8, column=2, columnspan=2)


    for widget in frame1.winfo_children():
        widget.configure(width=7)


    l_pinfo = tk.Label(frame1, text='Конфигурация намагниченности')
    l_pinfo.grid(row=10, column=0, columnspan=4, sticky='ew',pady=5)
    
    l_p = tk.Label(frame1, text='Величина P')
    l_p.grid(row=11, column=0, sticky='ew')

    l_n_start = tk.Label(frame1, text='n_start')
    l_n_start.grid(row=11, column=1, sticky='ew')

    l_p_width = tk.Label(frame1, text='p_width')
    l_p_width.grid(row=11, column=2, sticky='ew')

    l_p_height = tk.Label(frame1, text='p_height')
    l_p_height.grid(row=11, column=3, sticky='ew')

    P_val = tk.StringVar(frame1)
    e_p = tk.Entry(frame1, width=7, textvariable=P_val)
    e_p.grid(row=12, column=0)

    p_rectangle_start = tk.StringVar(frame1)
    e_n_start = tk.Entry(frame1, width=7, textvariable=p_rectangle_start)
    e_n_start.grid(row=12, column=1)

    p_rectangle_width = tk.StringVar(frame1)
    e_p_width = tk.Entry(frame1,  width=7, textvariable=p_rectangle_width)
    e_p_width.grid(row=12, column=2)

    p_rectangle_heigth = tk.StringVar(frame1)
    e_p_height = tk.Entry(frame1, width=7, textvariable=p_rectangle_heigth)
    e_p_height.grid(row=12, column=3)

    for widget in frame1.winfo_children():
        widget.configure(justify=tk.CENTER)


    btn_direct_grafs = tk.Button(frame1, text='График распределения B', width=18)
    btn_direct_grafs.grid(row=13, column=0, columnspan=2, pady=10, padx=10)

    btn_direct_task = tk.Button(frame1, text='Решить прямую задачу', width=18)
    btn_direct_task.grid(row=13, column=2, columnspan=2, pady=10)



    frame2 = tk.LabelFrame(panel, text='Обратная задача')
    frame2.grid(row=1, column=0, sticky='ew', ipadx=10, ipady=1, padx=10, pady=5)


    enabled = tk.IntVar()

    enabled_checkbutton_gamma = ttk.Checkbutton(frame2, text="Гамма регуляризация", variable=enabled)
    enabled_checkbutton_gamma.grid(row=0, column=0, columnspan=3, sticky='ew', padx=5, pady=10)


    l_gamma_start_value = tk.Label(frame2, text='Начальное значение гамма регуляризации:')
    l_gamma_start_value.grid(row=2, column=0, columnspan=2, pady=5, padx=5)

    gamma_start_value = tk.StringVar(frame1)
    e_gamma_start_value = tk.Entry(frame2, width=5, textvariable=gamma_start_value)
    e_gamma_start_value.grid(row=2, column=3)

    btn_back_task_frame = tk.Frame(frame2)
    btn_back_task_frame.grid(row=3, column=0, columnspan=4, pady=5, padx=0, sticky='ew')

    btn_plot_b = tk.Button(btn_back_task_frame, text='График распределения B')
    btn_plot_b.grid(row=0, column=0, columnspan=2, pady=5, padx=2, sticky='ew')

    btn_solve_back_task = tk.Button(btn_back_task_frame, text='Решить обратную задачу')
    btn_solve_back_task.grid(row=0, column=2, columnspan=2, pady=5, padx=2, sticky='ew')

    
    frame3 = ttk.Frame(panel)
    frame3.grid(row=2, column=0, columnspan=1)

    btn_default = tk.Button(frame3, text='По умолчанию', width=10, height=1)
    btn_default.grid(row=0, column=0, columnspan=1, padx=7, pady=5)

    btn_load = tk.Button(frame3, text='Загрузить', width=10, height=1)
    btn_load.grid(row=0, column=1, columnspan=1, padx=7, pady=5)

    btn_save = tk.Button(frame3, text='Сохранить', width=10, height=1)
    btn_save.grid(row=0, column=2, columnspan=1, padx=7, pady=5)



    x_start_val.set(ini.x_start)
    x_end_val.set(ini.x_end)
    y_start_val.set(ini.y_start)
    y_end_val.set(ini.y_end)
    z_start_val.set(ini.z_start)
    z_end_val.set(ini.z_end)

    count_x.set(ini.count_x)
    count_z.set(ini.count_z)
    

    x_rec_start.set(ini.x_rec_start)
    x_rec_end.set(ini.x_rec_end)
    n_receivers.set(ini.n_receivers)
    z_rec_val.set(ini.z_rec)

    I_val.set(ini.I)

    P_val.set(ini.p_val)
    p_rectangle_start.set(ini.p_rectangle_start)
    p_rectangle_width.set(ini.p_rectangle_width)
    p_rectangle_heigth.set(ini.p_rectangle_heigth)

    gamma_start_value.set(ini.initial_gamma)

    win.mainloop()