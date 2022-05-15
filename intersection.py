
from random import randint


#Wikipedia "Line-line intersection"

def line_intersection(line1, line2):
    
    #Coordenates first line
    x1 = line1[0][0]
    y1 = line1[0][1]
    
    x2 = line1[1][0]
    y2 = line1[1][1]
    
    #Coordinates second line
    x3 = line2[0][0]
    y3 = line2[0][1]
    
    x4 = line2[1][0]
    y4 = line2[1][1]


    denominator = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    #Acording to the wikipedia article if this denomintor is 0 the lines are parallel
    if denominator == 0:
        return

    t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/denominator
    u = -1*((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/denominator

    if t > 0 and t < 1 and u > 0:
        inter_x = x1 + (t*(x2-x1))
        inter_y = y1 + (t*(y2-y1))
        return(inter_x,inter_y)
    else: 
        print(False)



import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

while True:
    
    mouse = pygame.mouse.get_pos()
    print(mouse)

    screen.fill("black")
    pygame.draw.line(screen, "white", start_pos=(mouse),end_pos=(500,500))
    pygame.draw.line(screen, "white", start_pos=(500,100),end_pos=(100,500))

    inter = line_intersection([(mouse),(500,500)],[(500,100),(100,500)])

    if inter:
        pygame.draw.line(screen,"red",start_pos=mouse, end_pos=inter, width=3)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        mouse = pygame.mouse.get_pos()
    
    pygame.display.update()

    clock.tick()
