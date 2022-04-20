#!
# x′ = x * cos(θ) - y * sin(θ)
# y′ = x * sin(θ) + y * cos(θ)
# Turning a line using a trigonometry charts
import pygame
from sys import exit
from time import sleep


clock = pygame.time.Clock()


pygame.init
display = (500,500)
screen = pygame.display.set_mode((display))
imag = pygame.Surface((500,500))

# Inicial coordinates
mouse = [250,250]
start = [10,10]
end = [100,100]

coord = []


count =  0

def set_0(x: int , y: int)-> tuple:
    '''Correct coordinates as the center of the graph is point(start)'''
    x = start[0] + x
    y = start[1] - y 
    return(round(x),round(y))

def fill():
    sleep(0.0001)
    #print("Panting black")
    screen.fill("black")

def set_list_coor(start,end,angle):

    '''Angle's sine and cosine must be programed to be choosen inside a 
    trigonometric chart.
    Due to the problems python have with small decimal numbers, 
    the math's library is not reliable in this case, for consequence
    pygame.Vector too.
    '''
    
    lista = []
    #Using values as angle = 5°
    for n in range(360/angle):
        new_x_end = (end[0]* 0.9962 ) - (end[1] * 0.0872)
        new_y_end = (end[0]* 0.0872) + (end[1]* 0.9962)
        end = new_x_end,new_y_end
    lista.extend([start,set_0(end[0],end[1])])
    
    return lista

    
while True:

    if count == 360/5:
        pygame.draw.lines(screen,"white",closed=False,points=coord, width=1)
        coord = []
        count = 0
    
    mouse = pygame.mouse.get_pos()
    start = mouse
    
    # New coordinates to end
    # Using trigonometric values of 60º
    # x′ = x * cos(θ) - y * sin(θ)
    # y′ = x * sin(θ) + y * cos(θ)
    new_x_end = (end[0]* 0.9962 ) - (end[1] * 0.0872)
    new_y_end = (end[0]* 0.0872) + (end[1]* 0.9962)
    end = new_x_end,new_y_end
    coord.extend([start,set_0(end[0],end[1])])
    #coord.append(set_0(end[0],end[1]))
    
    #Counting the itens add to list de coordinates
    count += 1
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        mouse = pygame.mouse.get_pos()
    
    pygame.display.update()

    clock.tick()

    

    
