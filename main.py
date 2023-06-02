from reader import read_ini
from initial import InitialConditions

from gui.win import get_win_canvas_panel
from gui.model import Panel, Canvas, Ini
from gui.view import start_programm


def main(path):

    content = read_ini(path)
    ini = InitialConditions(**content)

    win, canvas, panel = get_win_canvas_panel()

    Ini.init_ini(ini)
    Panel.init_panel(panel)
    Canvas.init_canvas(canvas)

    start_programm()

    win.mainloop()


if __name__ == '__main__':

    path = 'settings.ini'
    main(path)
