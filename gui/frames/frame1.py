import tkinter as tk


def get_frame1(panel, ini):

    frame1 = tk.LabelFrame(panel, text='Прямая задача')
    frame1.grid(row=0, column=0, ipadx=10, ipady=1, padx=10, pady=10)

    lablel_1 = tk.Label(frame1, text='Ячеистая структура')
    lablel_1.grid(row=0, column=0, columnspan=2, sticky='ew')

    lablel_1 = tk.Label(frame1, text='x_start')
    lablel_1.grid(row=1, column=0)

    lablel_2 = tk.Label(frame1, text='x_end')
    lablel_2.grid(row=1, column=1)

    x_start_val = tk.StringVar(frame1)
    entry_1 = tk.Entry(frame1, textvariable=x_start_val)
    entry_1.grid(row=2, column=0)

    x_end_val = tk.StringVar(frame1)
    entry_2 = tk.Entry(frame1, textvariable=x_end_val)
    entry_2.grid(row=2, column=1)

    lablel_3 = tk.Label(frame1, text='y_start')
    lablel_3.grid(row=3, column=0)

    lablel_4 = tk.Label(frame1, text='y_end')
    lablel_4.grid(row=3, column=1)

    y_start_val = tk.StringVar(frame1)
    entry_3 = tk.Entry(frame1, textvariable=y_start_val)
    entry_3.grid(row=4, column=0)

    y_end_val = tk.StringVar(frame1)
    entry_4 = tk.Entry(frame1, textvariable=y_end_val)
    entry_4.grid(row=4, column=1)

    lablel_5 = tk.Label(frame1, text='z_start')
    lablel_5.grid(row=5, column=0)

    lablel_6 = tk.Label(frame1, text='z_end')
    lablel_6.grid(row=5, column=1)

    z_start_val = tk.StringVar(frame1)
    entry_5 = tk.Entry(frame1, textvariable=z_start_val)
    entry_5.grid(row=6, column=0)

    z_end_val = tk.StringVar(frame1)
    entry_6 = tk.Entry(frame1, textvariable=z_end_val)
    entry_6.grid(row=6, column=1)

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
    l_pinfo.grid(row=10, column=0, columnspan=4, sticky='ew', pady=5)

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

    btn_direct_grafs = tk.Button(frame1, text='График распределения B')
    btn_direct_grafs.grid(row=13, column=0, columnspan=2, sticky='ew', pady=10)

    btn_direct_task = tk.Button(frame1, text='Решить прямую задачу')
    btn_direct_task.grid(row=13, column=2, columnspan=2, sticky='ew', pady=10)

    variables = {}

    variables['x_start_val'] = x_start_val
    variables['x_end_val'] = x_end_val
    variables['y_start_val'] = y_start_val
    variables['y_end_val'] = y_end_val
    variables['z_start_val'] = z_start_val
    variables['z_end_val'] = z_end_val

    variables['count_x'] = count_x
    variables['count_z'] = count_z

    variables['x_rec_start'] = x_rec_start
    variables['x_rec_end'] = x_rec_end
    variables['n_receivers'] = n_receivers
    variables['z_rec_val'] = z_rec_val

    variables['I_val'] = I_val

    variables['P_val'] = P_val
    variables['p_rectangle_start'] = p_rectangle_start
    variables['p_rectangle_width'] = p_rectangle_width
    variables['p_rectangle_heigth'] = p_rectangle_heigth

    buttons = {}

    buttons['btn_direct_task'] = btn_direct_task
    buttons['btn_direct_grafs'] = btn_direct_grafs

    return variables, buttons
