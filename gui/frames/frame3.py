from tkinter import ttk
import tkinter as tk

def get_frame3(panel, ini):

    frame3 = ttk.Frame(panel)
    frame3.grid(row=2, column=0, columnspan=1)

    btn_default = tk.Button(frame3, text='По умолчанию', width=10, height=1)
    btn_default.grid(row=0, column=0, columnspan=1, padx=7, pady=5)

    btn_load = tk.Button(frame3, text='Загрузить', width=10, height=1)
    btn_load.grid(row=0, column=1, columnspan=1, padx=7, pady=5)

    btn_save = tk.Button(frame3, text='Сохранить', width=10, height=1)
    btn_save.grid(row=0, column=2, columnspan=1, padx=7, pady=5)

    variables = {}
    buttons = {}

    return variables, buttons