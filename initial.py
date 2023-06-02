import numpy as np


class InitialConditions():

    def __init__(self, *args, **kwargs) -> None:

        self.x_start = kwargs['x_start']
        self.x_end = kwargs['x_end']
        self.y_start = kwargs['y_start']
        self.y_end = kwargs['y_end']
        self.z_start = kwargs['z_start']
        self.z_end = kwargs['z_end']

        self.count_x = kwargs['count_x']
        self.count_z = kwargs['count_z']

        self.p_val = kwargs['p_val']
        self.p_rectangle_start = kwargs['p_rectangle_start']
        self.p_rectangle_width = kwargs['p_rectangle_width']
        self.p_rectangle_heigth = kwargs['p_rectangle_heigth']

        self.p_nonzero = []
        self.fill_p_nonzero()

        self.n_receivers = kwargs['n_receivers']
        self.x_rec_start = kwargs['x_rec_start']
        self.x_rec_end = kwargs['x_rec_end']
        self.z_rec = kwargs['z_rec']

        self.init_cells()
        self.init_receivers()
        self.volume_cells()

        self.I = kwargs['I']
        self.initial_gamma = kwargs['initial_gamma']

    def fill_p_nonzero(self):

        for i in range(self.p_rectangle_heigth):
            for j in range(self.p_rectangle_width):
                self.p_nonzero.append(self.p_rectangle_start + j + self.count_x * i)

    def init_cells(self):

        self.count = self.count_x * self.count_z
        self.delta_x = round((self.x_end - self.x_start)/self.count_x)
        self.delta_z = round((self.z_end - self.z_start)/self.count_z)

        self.x_cells = [[self.x_start + i * self.delta_x, self.x_start +
                         (i + 1) * self.delta_x] for j in range(self.count_z) for i in range(self.count_x)]

        self.y_cells = [[self.y_start, self.y_end] for i in range(self.count)]

        self.z_cells = [[self.z_end - (i + 1) * self.delta_z, self.z_end - i * self.delta_z]
                        for i in range(self.count_z) for j in range(self.count_x)]

        self.p_cells = [[self.p_val, 0, 0] if i in self.p_nonzero else [0, 0, 0]
                        for i in range(self.count)]

        self.center_cells = [[(self.x_cells[i][0] + self.x_cells[i][1])/2, (self.y_cells[i][0] + self.y_cells[i]
                                                                            [1])/2, (self.z_cells[i][0] + self.z_cells[i][1])/2] for i in range(self.count)]

    def init_receivers(self):

        self.x_receiver = np.linspace(
            self.x_rec_start, self.x_rec_end, self.n_receivers)
        self.coords_rec = [[i, 0, self.z_rec] for i in self.x_receiver]

    def volume_cells(self):

        lenx = []
        leny = []
        lenz = []
        res = []

        for i in self.x_cells:
            lenx.append(i[1] - i[0])

        for i in self.y_cells:
            leny.append(i[1] - i[0])

        for i in self.z_cells:
            lenz.append(i[1] - i[0])

        for i, item in enumerate(lenx):
            res.append(abs(lenx[i] * leny[i] * lenz[i]))

        self.volume = res