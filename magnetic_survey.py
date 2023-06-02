import numpy as np
import math
import matplotlib.pyplot as plt
from loguru import logger

from initial import InitialConditions


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
    initial_val = ini.initial_gamma

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
        Alfa = reg_alfa(A, alfa=10**-8, state=True)

        A_new = A + Alfa + C

        # Решаем СЛАУ
        P_res = np.linalg.solve(A_new, b)

        # logger.info(f'\nВектор намагниченности Px:\n{np.round(P_res[::3], 5)}')
        # logger.info(f'\nВектор намагниченности Py:\n{np.round(P_res[1::3], 5)}')
        # logger.info(f'\nВектор намагниченности Pz:\n{np.round(P_res[2::3], 5)}')

        _break_point = True
        _up_gamma = set()

        for i in range(count):
            for j in neighbors_list[i]:
                if P_res[3*i] > 4 * P_res[3*j]:
                    _up_gamma.add(i)
                    _up_gamma.add(j)
                    _break_point = False

        for i in _up_gamma:
            gamma[3*i] = gamma[3*i] * 2

        # logger.info(f'\ngamma:\n{np.round(gamma[::3], 3)}')
        # logger.info(f'\ngamma:\n{gamma[2::3]}')
        # logger.info(f'\ngamma:\n{_up_gamma}')

        if _break_point:
            return P_res