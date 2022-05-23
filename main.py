#!
# x′ = x * cos(θ) - y * sin(θ)
# y′ = x * sin(θ) + y * cos(θ)
# Turning a line using a trigonometry charts
import pygame
from sys import exit
from intersection import line_intersection as li



clock = pygame.time.Clock()


pygame.init
display = (500,500)
screen = pygame.display.set_mode((display))
imag = pygame.Surface((500,500))

# Inicial coordinates
mouse = [250,250]
start = [10,10]

#This variable defines the end of the first line to draw, for consequence the lengh of the lines.
end = [100,100]


def set_0(x:float , y: float, s = ())-> tuple:
    '''
    ---This function sets the point (0,0) to the "s" argument---

    The formula to rotate a line its used to rotate around the(0,0)
    point,so after you calculate the lines around the mouse position 
    you have to correct this value as its has been calculated using 
    this point.
    Pygame uses a quadrant that dosn't exits in a traditional graph,
    to uses trigonometric formulas we have trasform the (y) value to 
    a negative side.
    '''

    if s == ():
        s = start

    x = s[0] + x
    y = s[1] + y 
    return(round(x),round(y))


def set_list_coor(start=None,end=None, angle=5):
    
    '''Angle's sine and cosine must be programed to be choosen inside a 
    trigonometric chart.
    Due to the problems python have with small decimal numbers, 
    the math's library is not reliable in this case, for consequence
    pygame.Vector is not reliable too.
    '''
    
    lista = []

    #Using values as angle = 5°
    
    for n in range(360//angle):
        new_x_end = (end[0]* 0.9962 ) - (end[1] * 0.0872)
        new_y_end = (end[0]* 0.0872) + (end[1]* 0.9962)
        end = new_x_end,new_y_end
        
        
        
        a = set_0(end[0],end[1])

        #testing lines collision
        b = li((start, a), ((400, 100), (400, 400)))
        c = li((start, a), ((100, 100), (100, 400)))
        d = li((start, a), ((200, 200), (300, 300)))

        if b != False:
            lista.extend([start, b])
        elif c != False:
            lista.extend([start, c])
        elif d != False:
            lista.extend([start, d])

        else:
            lista.extend([start, a])
        
 
   
    return lista

    
while True:


    start = pygame.mouse.get_pos()
    coordinates  = set_list_coor(start=start,end=end,angle=5)

    #screen.blit must be used before the first draw
    screen.fill("black")
    pygame.draw.lines(screen,"white",closed=True,points=coordinates,width=2)

    
    # Drawing colisions lines
    pygame.draw.line(screen, "white", start_pos=(400,100), end_pos=(400,400))
    pygame.draw.line(screen, "white", start_pos=(100,100), end_pos=(100,400))
    pygame.draw.line(screen, "white", start_pos=(200,200), end_pos=(300,300))
    
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
            exit()
        mouse = pygame.mouse.get_pos()
    
    pygame.display.update()

    clock.tick()

    

    