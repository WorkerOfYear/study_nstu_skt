import numpy as np
import math
import matplotlib.pyplot as plt


# Решаем прямую задачу
# Задаем ячейки с намагниченостью

# Способ 1 (вручную)
# x_cells = [[-100, 0], [0, 100], [-100, 0], [0, 100]]
# y_cells = [[-1000, 1000], [-1000, 1000], [-1000, 1000], [-1000, 1000]]
# z_cells = [[-150, -100], [-150, -100], [-200, -150], [-200, -150]]
# p_cells = [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]
# # центр ячеек
# center_cells = [(-50, 0, -125), (50, 0, -125), (-50, 0, -175), (50, 0, -175)]
# # Число ячеек
# K = len(center_cells)

# Способ 2 (задаём область и колличество ячеек)
start = [-100, -1000, -200]
end = [100, 1000, -100]

count_x = 2
count_z = 2

count = count_x * count_z

delta_x = round((end[0] - start[0])/count_x)
# delta_y = round((end[1] - start[1])/count)
delta_z = round((end[2] - start[2])/count_z)

x_cells = [[start[0] + i * delta_x, start[0] +
            (i + 1) * delta_x] for j in range(count_z) for i in range(count_x)]
y_cells = [[start[1], end[1]] for i in range(count)]
z_cells = [[end[2] - (i + 1) * delta_z, end[2] - i * delta_z]
           for i in range(count_z) for j in range(count_x)]
p_cells = [[1, 0, 0] for i in range(count)]

center_cells = [[(x_cells[i][0] + x_cells[i][1])/2, (y_cells[i][0] + y_cells[i]
                                                     [1])/2, (z_cells[i][0] + z_cells[i][1])/2] for i in range(count)]

K = len(center_cells)

# Задаём расположением приемников
number_receivers = 500
x_receiver = np.linspace(-1000, 1000, number_receivers)
coordinates_receivers = [[i, 0, 25] for i in x_receiver]


def volume_cells(x_cells, y_cells, z_cells):
    '''Выводит список с объёмом всех ячеек'''

    lenx = []
    leny = []
    lenz = []
    res = []

    for i in x_cells:
        lenx.append(i[1] - i[0])

    for i in y_cells:
        leny.append(i[1] - i[0])

    for i in z_cells:
        lenz.append(i[1] - i[0])

    for i, item in enumerate(lenx):
        res.append(abs(lenx[i] * leny[i] * lenz[i]))

    return res


def calculation_B(p, center_cells, coordinates_receivers, vol, I):
    '''Возвращает список со заначениями полей в приёмниках, а также матрицу L'''
    pi = math.pi
    Bx = []
    By = []
    Bz = []
    L_all = np.zeros((3 * number_receivers, 3 * K))

    for i, element in enumerate(coordinates_receivers):
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


def regul_c(count_x, count_z, initial_val = 0.001):
    '''Рассчёт С-матрицы регуляризации'''

    # Полное колличество ячеек - count
    count = count_x * count_z
    # Нулевая матрица размером = count * 3, count * 3
    C = np.zeros((count * 3, count * 3))
    # Начальное значение параметра регуляризации gamma для всех ячеек
    gamma = np.zeros((count * 3)) + initial_val

    # Колличество соседей
    M = 1

    neighbors_list = get_neighbors(count_x, count_z)

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
                    for j in neighbors_list[m]:
                        sum += gamma[3*j + i]
                        pass

                    C[3*k + i][3*m + i] = M * gamma[3*k + i] + sum

            else:
                print('Некорректное заполнение матрицы')

    return C


# мощность источника
I = 10

# Расчет объёма ячеек
vol = volume_cells(x_cells, y_cells, z_cells)

# Расчет значений практических сигналов
B_practical_x, B_practical_y, B_practical_z, L = calculation_B(
    p_cells, center_cells, coordinates_receivers, vol, I)

# выводим графики

# plt.plot(x_receiver, B_practical_x)
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# Решаем обратную задачу (с помощью практических B в приёмниках находим P в ячейках)

# Формируем матрицу A
L_t = L.T
A = L_t.dot(L)

# Альфа регуляризация
# ones_matrix = np.ones((len(A), len(A)))
# I = np.diag(np.diag(ones_matrix))
# alfa = 1

# С - регуляризация
C = regul_c(count_x, count_z, initial_val = 0.001)

A_new = A + C # + alfa * I

# Формируем матрицу b
S = np.zeros(3 * len(B_practical_x)).T
for i, item in enumerate(B_practical_x):
    S[3*i] = B_practical_x[i]
    S[3*i+1] = B_practical_y[i]
    S[3*i+2] = B_practical_z[i]

b = L_t.dot(S)

# Решаем СЛАУ
P_res = np.linalg.solve(A_new, b)
print(P_res)
