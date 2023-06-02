import tkinter as tk


def get_win_canvas_panel():

    WIN_H = 600
    WIN_W = 900
    PANEL_H = WIN_H
    PANEL_W = 450
    CANVAS_H = WIN_H
    CANVAS_W = WIN_W-PANEL_W

    win = tk.Tk()
    photo = tk.PhotoImage(file='./gui/fpmi_full.png', master=win)
    win.iconphoto(False, photo)
    win.title('Обработка данных магниторазведки')
    win.geometry(f'{WIN_W}x{WIN_H}+100+100')

    win.resizable(False, False)
    win.config(bg='#fff')

    canvas = tk.Canvas(win, width=CANVAS_W, height=CANVAS_H, bg='#fff')
    canvas.place(x=PANEL_W, y=0, width=CANVAS_W, height=CANVAS_W)
    
    panel = tk.Frame(win, width=PANEL_W, height=PANEL_H,
                     bd=0, relief=tk.GROOVE)
    panel.place(x=0, y=0, width=PANEL_W, height=PANEL_H)

    return win, canvas, panel