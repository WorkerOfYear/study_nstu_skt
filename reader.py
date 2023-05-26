from configparser import ConfigParser


def read_ini(path):

    config = ConfigParser()
    config.read(path)

    content={}

    content['x_start'] = int(config.get("InCoords", "x_start"))
    content['x_end'] = int(config.get("InCoords", "x_end"))

    content['y_start'] = int(config.get("InCoords", "y_start"))
    content['y_end'] = int(config.get("InCoords", "y_end"))

    content['z_start'] = int(config.get("InCoords", "z_start"))
    content['z_end'] = int(config.get("InCoords", "z_end"))

    content['x_rec_start'] = int(config.get("InCoords", "x_rec_start"))
    content['x_rec_end'] = int(config.get("InCoords", "x_rec_end"))

    content['count_x'] = int(config.get("InValues", "count_x"))
    content['count_z'] = int(config.get("InValues", "count_z"))

    content['n_receivers'] = int(config.get("InValues", "n_receivers"))
    content['I'] = int(config.get("InValues", "I"))
    content['z_rec'] = int(config.get("InValues", "z_rec"))

    return content