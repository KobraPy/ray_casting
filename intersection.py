# Wikipedia "Line-line intersection"
from math import sqrt


def line_intersection(line1, line2):

    """
    Check if two lines intersect and return the point where they intersect or false
    """

    # Coordenates first line
    x1 = line1[0][0]
    y1 = line1[0][1]

    x2 = line1[1][0]
    y2 = line1[1][1]

    # Coordinates second line
    x3 = line2[0][0]
    y3 = line2[0][1]

    x4 = line2[1][0]
    y4 = line2[1][1]

    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    # Acording to the wikipedia article if this denomintor is 0 the lines are parallel
    if denominator == 0:
        return False

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
    u = -1 * ((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator

    if t > 0 and t < 1 and u > 0 and u < 1:
        inter_x = x1 + (t * (x2 - x1))
        inter_y = y1 + (t * (y2 - y1))
        return (inter_x, inter_y)
    else:
        return False


def distance_two_points(point1: tuple, point2: tuple) -> float:

    """
    Calcule the distance between the origin point and the intersection point
    to the draw the smallest
    """

    # d = sqr((x2-x1)**2 + (y2-y1)**2)
    x1 = point1[0]
    y1 = point1[1]

    x2 = point2[0]
    y2 = point2[1]

    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d
