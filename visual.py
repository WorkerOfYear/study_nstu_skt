import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


def show_field (B_practical_x, B_practical_y, B_practical_z, ini):
    plt.plot(ini.x_receiver, B_practical_x)
    plt.show()


def get_plot(ini, p):

    count_x = ini.count_x
    count_z = ini.count_z

    x_start = ini.x_start
    x_end = ini.x_end
    width = (x_end - x_start) / count_x

    z_start = ini.z_start
    z_end = ini.z_end
    heigth = (z_end - z_start) / count_z

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot()
    ax.set_xlim(-400, 400)
    ax.set_ylim(-300, 100)

    x_receiver = ini.x_receiver
    z = np.zeros((len(x_receiver))) + ini.z_rec

    

    # cmap = LinearSegmentedColormap.from_list('green_paradiase', ["lawngreen", "lightseagreen"])
    cmap = LinearSegmentedColormap.from_list('green_paradiase', ["white", "black"])

    ax.scatter(x_receiver, z, alpha=0.5, linewidths=1, cmap=cmap)
    
    
    count = 0
    for j in range(count_z):
        for i in range(count_x):
            x = x_start + i * width
            z = z_end - j * heigth
            rect = Rectangle((x, z), width, -1 * heigth, facecolor = cmap(abs(p[3*count])), edgecolor = 'w')
            ax.add_patch(rect)

            # x = ini.center_cells[count][0] - 0.1 * width
            # z = ini.center_cells[count][2] - 0.1 * heigth
            # ax.text(x,z,p[3 * count], fontsize=8)

            count += 1

    return fig