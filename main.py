#!
# x′ = x * cos(θ) - y * sin(θ)
# y′ = x * sin(θ) + y * cos(θ)
# Turning a line using a trigonometry charts
import pygame
from sys import exit
import math
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


def set_0(x: int , y: int)-> tuple:
    '''Correct coordinates as the center of the graph is point(start)'''
    x = start[0] + x
    y = start[1] - y 
    return(round(x),round(y))

def fill():
    print("Panting black")
    screen.fill("black")
    
while True:
    fill()
    
    mouse = pygame.mouse.get_pos()
    start = mouse
    sleep(1)
    # Drawing the first line
    pygame.draw.line(screen,"white",start_pos=(start),end_pos=(set_0(end[0],end[1])),width=3)
    sleep(1)
    
    # New coordinates to end
    # Using trigonometric values of 60º
    # x′ = x * cos(θ) - y * sin(θ)
    # y′ = x * sin(θ) + y * cos(θ)
    new_x_end = (end[0]* 0.5000 ) - (end[1] * 0.8660)
    new_y_end = (end[0]* 0.8660) + (end[1]* 0.5000)
    end = new_x_end,new_y_end
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        mouse = pygame.mouse.get_pos()
    
    pygame.display.update()

    clock.tick()

    

    
