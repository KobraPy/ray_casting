#!
# x′ = x * cos(θ) - y * sin(θ)
# y′ = x * sin(θ) + y * cos(θ)
# Turning a line using a trigonometry charts

import pygame
from sys import exit


from intersection import line_intersection as li
from intersection import distance_two_points as dp


clock = pygame.time.Clock()


pygame.init()
display = (500, 500)
screen = pygame.display.set_mode((display))

# Inicial coordinates
mouse = [300, 300]
start = [10, 10]

# This variable defines the end of the first line to draw,
#  for consequence the lengh of the lines.
end = [150, 150]


def set_0(x: float, y: float, s=()) -> tuple:
    """
    ---This function sets the point (0,0) to the "s" argument---

    The formula to rotate a line its used to rotate around the(0,0)
    point,so after you calculate the lines around the mouse position
    you have to correct this value as if the mouse was on (0,0) point
    in the graph.
    """

    if s == ():
        s = start

    x = s[0] + x
    y = s[1] + y
    return (round(x), round(y))


def set_list_coor(start=None, end=None, angle=5):

    """
    Angle's sine and cosine must be programed to be choosen inside a
    trigonometric chart.
    Due to the problems python have with small decimal numbers,
    the math's library is not reliable in this case, for consequence
    pygame.Vector is not reliable too.
    """

    lista = []
    lista_to_circles = []

    # Using values as angle = 5°

    for n in range(360 // angle):
        new_x_end = (end[0] * 0.9962) - (end[1] * 0.0872)
        new_y_end = (end[0] * 0.0872) + (end[1] * 0.9962)
        end = new_x_end, new_y_end

        a = set_0(end[0], end[1])

        # Checking if there is a intersection, and returing the point where they intersect
        b = li((start, a), ((400, 100), (400, 400)))
        c = li((start, a), ((100, 100), (100, 400)))
        d = li((start, a), ((200, 200), (300, 300)))

        # If there is a intercection, it calculate the distance between the 
        # start point and the intersection point
        if b:
            b_distance = dp(start, b)
        if c:
            c_distance = dp(start, c)
        if d:
            d_distance = dp(start, d)

        if all([b, c, d]):
            # Checking if the line intesect with all three obstacles and returnig the smallest distance
            # all function retutrns true if all elemntes on a interable are valid values

            if b_distance < c_distance and b_distance < d_distance:
                lista.extend([start, b])
                lista_to_circles.append(b)

            elif c_distance < b_distance and c_distance < d_distance:
                lista.extend([start, c])
                lista_to_circles.append(c)

            elif d_distance < b_distance and d_distance < c_distance:
                lista.extend([start, d])
                lista_to_circles.append(d)

        # Checking when the lines intersect with two obstacles and returning the smallest distance
        elif b and c and not d:
            if b_distance < c_distance:
                lista.extend([start, b])
                lista_to_circles.append(b)
            else:
                lista.extend([start, c])
                lista_to_circles.append(c)

        elif b and d and not c:
            if b_distance < d_distance:
                lista.extend([start, b])
                lista_to_circles.append(b)
            else:
                lista.extend([start, d])
                lista_to_circles.append(d)

        elif c and d and not b:
            if c_distance < d_distance:
                lista.extend([start, c])
                lista_to_circles.append(c)
            else:
                lista.extend([start, d])
                lista_to_circles.append(d)

        # Checking when the line intersect with just one obstacle
        elif b and not c and not d:
            lista.extend([start, b])
            lista_to_circles.append(b)

        elif c and not b and not d:
            lista.extend([start, c])
            lista_to_circles.append(c)

        elif d and not b and not c:
            lista.extend([start, d])
            lista_to_circles.append(d)

        else:
            lista.extend([start, a])

    return lista, lista_to_circles


while True:

    start = pygame.mouse.get_pos()
    coordinates = set_list_coor(start=start, end=end, angle=5)

    # screen.blit must be used before the first draw
    screen.fill('black')
    pygame.draw.lines(
        screen, 'white', closed=True, points=coordinates[0], width=2
    )
    for point in coordinates[1]:
        pygame.draw.circle(screen, 'white', point, radius=3)
        pygame.draw.circle(screen, 'white', point, radius=7, width=1)

    # Drawing colisions lines
    pygame.draw.line(screen, 'white', start_pos=(400, 100), end_pos=(400, 400))
    pygame.draw.line(screen, 'white', start_pos=(100, 100), end_pos=(100, 400))
    pygame.draw.line(screen, 'white', start_pos=(200, 200), end_pos=(300, 300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            exit()
        mouse = pygame.mouse.get_pos()

    pygame.display.update()

    clock.tick()
