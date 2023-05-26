import numpy as np
import math
import matplotlib.pyplot as plt
from loguru import logger


from reader import read_ini
from visual import show_plot, show_field


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

        self.count = self.count_x * self.count_z

        self.delta_x = round((self.x_end - self.x_start)/self.count_x)
        self.delta_z = round((self.z_end - self.z_start)/self.count_z)

        self.n_receivers = kwargs['n_receivers']
        self.x_rec_start = kwargs['x_rec_start']
        self.x_rec_end = kwargs['x_rec_end']
        self.z_rec = kwargs['z_rec']

        self.init_cells()
        self.init_receivers()
        self.volume_cells()

        self.I = kwargs['I']

    def init_cells(self):

        self.x_cells = [[self.x_start + i * self.delta_x, self.x_start +
                         (i + 1) * self.delta_x] for j in range(self.count_z) for i in range(self.count_x)]

        self.y_cells = [[self.y_start, self.y_end] for i in range(self.count)]

        self.z_cells = [[self.z_end - (i + 1) * self.delta_z, self.z_end - i * self.delta_z]
                        for i in range(self.count_z) for j in range(self.count_x)]

        # TODO if i in range(1,3) else [0, 0, 0] 
        self.p_cells = [[1, 0, 0] if i in [5,6,9,10] else [0, 0, 0] for i in range(self.count)]
        # print(self.p_cells)

        # self.p_cells = [[1, 0, 0] for i in range(self.count)]


        self.center_cells = [[(self.x_cells[i][0] + self.x_cells[i][1])/2, (self.y_cells[i][0] + self.y_cells[i]
                                                                            [1])/2, (self.z_cells[i][0] + self.z_cells[i][1])/2] for i in range(self.count)]

    def init_receivers(self):

        self.x_receiver = np.linspace(self.x_rec_start, self.x_rec_end, self.n_receivers)
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


def calculation_B(ini: InitialConditions):
    '''Возвращает список со заначениями полей в приёмниках, а также матрицу L'''

    pi = math.pi

    p = ini.p_cells
    I = ini.I
    vol = ini.volume
    n_receivers = ini.n_receivers
    count = ini.count
    coords_rec = ini.coords_rec
    center_cells = ini.center_cells

    Bx = []
    By = []
    Bz = []
    L_all = np.zeros((3 * n_receivers, 3 * count))

    for i, element in enumerate(coords_rec):
        x_rec = element[0]
        y_rec = element[1]
        z_rec = element[2]

        res_x = 0
        res_y = 0
        res_z = 0

        for j, item in enumerate(center_cells):
            x_unit = item[0]
            y_unit = item[1]
            z_unit = item[2]
            volume_unit = vol[j]

            px = p[j][0]
            py = p[j][1]
            pz = p[j][2]

            x_rec_new = x_rec - x_unit
            y_rec_new = y_rec - y_unit
            z_rec_new = z_rec - z_unit

            r = math.sqrt((x_rec_new) ** 2 + (y_rec_new)
                          ** 2 + (z_rec_new) ** 2)
            coef = volume_unit * I / (4 * pi * r ** 3)

            Lxx = coef * ((3 * x_rec_new ** 2 / r ** 2) - 1)
            Lxy = coef * (3 * x_rec_new * y_rec_new / r ** 2)
            Lxz = coef * (3 * x_rec_new * z_rec_new / r ** 2)

            Lyx = coef * (3 * y_rec_new * x_rec_new / r ** 2)
            Lyy = coef * ((3 * y_rec_new ** 2 / r ** 2) - 1)
            Lyz = coef * (3 * y_rec_new * z_rec_new / r ** 2)

            Lzx = coef * (3 * z_rec_new * x_rec_new / r ** 2)
            Lzy = coef * (3 * z_rec_new * y_rec_new / r ** 2)
            Lzz = coef * ((3 * z_rec_new ** 2 / r ** 2) - 1)

            res_x += px * Lxx + py * Lxy + pz * Lxz
            res_y += px * Lyx + py * Lyy + pz * Lyz
            res_z += px * Lzx + py * Lzy + pz * Lzz

            L_part = np.array(
                [[Lxx, Lxy, Lxz], [Lyx, Lyy, Lyz], [Lzx, Lzy, Lzz]])
            L_all[3*i:(3*i+3), 3*j:(3*j+3)] = L_part[0:3, 0:3]

        Bx.append(res_x)
        By.append(res_y)
        Bz.append(res_z)

    return [Bx, By, Bz, L_all]


def get_neighbors(count_x, count_z):
    '''Возвращает список со списками соседей для каждой ячейки'''
    count = count_x * count_z
    k = count_x
    neighbors_list = []

    for i in range(count):

        if i < count_x:
            if (i + 1) % count_x == 0:
                neighbors_list.append([i - 1, i + k])
            elif (i + 1) % count_x == 1:
                neighbors_list.append([i + 1, i + k])
            else:
                neighbors_list.append([i - 1, i + 1, i + k])
        elif i >= count - count_x:
            if (i + 1) % count_x == 0:
                neighbors_list.append([i - 1, i - k])
            elif (i + 1) % count_x == 1:
                neighbors_list.append([i + 1, i - k])
            else:
                neighbors_list.append([i - 1, i + 1, i - k])
        else:
            if (i + 1) % count_x == 0:
                neighbors_list.append([i - 1, i + k, i - k])
            elif (i + 1) % count_x == 1:
                neighbors_list.append([i + 1, i + k, i - k])
            else:
                neighbors_list.append([i - 1, i + 1, i + k, i - k])

    return neighbors_list


def reg_c(count_x, count_z, gamma, neighbors_list):
    '''Рассчёт С-матрицы регуляризации'''

    # Полное колличество ячеек - count
    count = count_x * count_z

    # Нулевая матрица размером = count * 3, count * 3
    C = np.zeros((count * 3, count * 3))

    for k in range(count):
        for m in range(count):

            if m != k:
                if k in neighbors_list[m]:
                    for i in range(3):
                        C[3*k + i][3*m + i] = - \
                            (gamma[3*k + i] + gamma[3*m + i])

            elif m == k:
                for i in range(3):

                    sum = 0
                    neighbors_count = 0
                    for j in neighbors_list[m]:
                        sum += gamma[3*j + i]
                        neighbors_count += 1
                        pass

                    C[3*k + i][3*m + i] = neighbors_count * gamma[3*k + i] + sum

            else:
                print('Некорректное заполнение матрицы')

    return C


def reg_alfa(A, alfa=1, state=True) -> np.array:
    '''
    Альфа регуляризация
    '''
    if state == True:
        ones_matrix = np.ones((len(A), len(A)))
        I = np.diag(np.diag(ones_matrix))

        return alfa * I


def calculation_P(B_practical_x, B_practical_y, B_practical_z, L, ini: InitialConditions):

    count_x = ini.count_x
    count_z = ini.count_z

    count = count_x * count_z
    initial_val = 10**(-18)

    # Формируем матрицу A
    L_t = L.T
    A = L_t.dot(L)
    # logger.debug(f'Матрица A: {A}')

    # Формируем матрицу b
    S = np.zeros(3 * len(B_practical_x)).T
    for i, _ in enumerate(B_practical_x):
        S[3*i] = B_practical_x[i]
        S[3*i+1] = B_practical_y[i]
        S[3*i+2] = B_practical_z[i]
    b = L_t.dot(S)
    # logger.debug(f'Матрица b: {b}')

    
    # Начальное значение параметра регуляризации gamma для всех ячеек
    gamma = np.zeros((count * 3)) + initial_val

    # logger.debug(f'Начальное значение параметра регуляризации gamma для всех ячеек: {gamma}')
    neighbors_list = get_neighbors(count_x, count_z)

    # Процесс регуляризации
    while True:
        C = reg_c(count_x, count_z, gamma, neighbors_list)
        # logger.debug(f'Матрица С: {C}')
        Alfa = reg_alfa(A, alfa=0.01, state=True)
        # A_new = A + C  
        A_new = A + Alfa

        # Решаем СЛАУ
        P_res = np.linalg.solve(A_new, b)
        # logger.info(f'\nВектор намагниченности Px:\n{np.round(P_res[::3], 5)}')
        # logger.info(f'\nВектор намагниченности Py:\n{np.round(P_res[1::3], 5)}')
        # logger.info(f'\nВектор намагниченности Pz:\n{np.round(P_res[2::3], 5)}')

        break_point = True

        # for i in range(count):
        #     for j in neighbors_list[i]:
        #         if P_res[3*i] > 10 * P_res[3*j]:
        #             gamma[3*j] = gamma[3*j] * 2
        #             break_point = False

        if break_point:
            return P_res


def main(path):

    # Начальные условия
    content = read_ini(path)
    ini = InitialConditions(**content)

    # Решение прямой задачи
    B_practical_x, B_practical_y, B_practical_z, L = calculation_B(ini)

    # show_field(B_practical_x, B_practical_y, B_practical_z, ini)

    # Решение обратной задачи
    P_res = calculation_P(B_practical_x, B_practical_y,
                          B_practical_z, L, ini)

    show_plot(ini, np.round(P_res, 2))

if __name__ == '__main__':

    path = 'settings.ini'
    main(path)
