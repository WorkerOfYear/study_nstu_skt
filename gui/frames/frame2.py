import tkinter as tk
from tkinter import ttk


def get_frame2(panel, ini):

    frame2 = tk.LabelFrame(panel, text='Обратная задача')
    frame2.grid(row=1, column=0, sticky='ew',
                ipadx=1, ipady=1, padx=10, pady=5)

    enabled = tk.IntVar()

    enabled_checkbutton_gamma = ttk.Checkbutton(
        frame2, text="Гамма регуляризация", variable=enabled)
    enabled_checkbutton_gamma.grid(
        row=0, column=0, sticky='w', ipadx=5, ipady=5, padx=5, pady=5)

    l_gamma_start_value = tk.Label(
        frame2, text='Начальное значение гамма регуляризации:')
    l_gamma_start_value.grid(row=1, column=0, sticky='ew')

    gamma_start_value = tk.StringVar(frame2)
    e_gamma_start_value = tk.Entry(
        frame2, width=5, textvariable=gamma_start_value)
    e_gamma_start_value.grid(row=1, column=1, ipadx=0, ipady=0, padx=0, pady=0)

    sub_frame = tk.Frame(frame2)
    sub_frame.grid(row=2, column=0, columnspan=2, ipadx=1, ipady=1, padx=1, pady=5)

    btn_plot_b = tk.Button(sub_frame, text='График распределения B')
    btn_plot_b.grid(row=0, column=0, sticky='ew')

    btn_solve_back_task = tk.Button(sub_frame, text='Решить обратную задачу')
    btn_solve_back_task.grid(row=0, column=1, sticky='ew')

    # for widget in frame2.winfo_children():

    #     if isinstance(widget, ttk.Checkbutton):
    #         continue
    #     elif isinstance(widget, tk.StringVar):
    #         continue
    #     elif isinstance(widget, tk.Entry):
    #         continue
    #     else:
    #         widget.configure(padx=5, pady=5)

    
    variables = {} 
    variables['gamma_start_value'] = gamma_start_value

    buttons = {}
    buttons['btn_solve_back_task'] = btn_solve_back_task

    return variables, buttons
