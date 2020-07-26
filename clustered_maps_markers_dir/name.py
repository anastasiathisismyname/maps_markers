import numpy as np


def check_if_point_is_inside_box(box, point):

    latitude1, longitude1 = float(box[0][0]), float(box[0][1])
    latitude2, longitude2 = float(box[1][0]), float(box[1][1])

    result = False

    if latitude1 < point[0] < latitude2 and longitude1 < point[1] < longitude2:
        result = True

    return result


# print(check_if_point_is_inside_box([[1, 8], [5, 10]], [3.18, 7.36]))
print(check_if_point_is_inside_box([[1, 8], [5, 10]], [3.15, 8.15]))
