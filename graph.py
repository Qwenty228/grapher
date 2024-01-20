import pygame as pg 
from pygame import Vector2 as vec
from utils.fullscreen import Mouse
import pygame.freetype

SIZE = 40 # size of the grid square


x = lambda t: -2 - t/3 
x2 = lambda t: 1
x3 = lambda t: 1 -t/3


def make_function(functions_with_domain):
    def function(t):
        for func, (x1, x2) in functions_with_domain:
            if x1 <= t <= x2:
                return func(t)
        return 0
    return function


class Graph:
    def __init__(self) -> None:
        pg.freetype.init()
        self.positions = vec(0, 0) # position of the graph at the center of the screen
        self.font = pg.freetype.SysFont('arial', 20, True, True)
        


        # [[function, domain], ...]
        self.function = make_function([[x, (-6, -3)], [x2, (-3, 0)], [x3, (0, 3)]])
        #self.function = lambda t: function((1-t)/2)



    def update(self, dt):
        global SIZE
        # self.positions.x += dt * 10
        keys= pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.positions.x -= dt * 100
        if keys[pg.K_RIGHT]:
            self.positions.x += dt * 100
        if keys[pg.K_UP]:
            self.positions.y -= dt * 100
        if keys[pg.K_DOWN]:
            self.positions.y += dt * 100
        
        if keys[pg.K_KP_PLUS]:
            SIZE += 1
        if keys[pg.K_KP_MINUS]:
            SIZE -= 1
            if SIZE < 1:
                SIZE = 1



        

    def draw(self, screen, offset=None):
        if not offset:
            x, y = self.positions - screen.get_rect().center  # render the graph in the center of the screen
            offset = int(x), int(y)
       
        points = []
        for x in range(offset[0]//SIZE - 1, (screen.get_width() + offset[0])//SIZE + 2):
            if x == 0:
                self.draw_line(screen, (x*SIZE - offset[0], 0), (x*SIZE-offset[0], screen.get_height()), 'blue')
            else:
                self.draw_line(screen, (x*SIZE - offset[0], 0), (x*SIZE-offset[0], screen.get_height()))

            # draw function:
            points.append((x*SIZE - offset[0], -self.function(x) * SIZE - offset[1]))
        

        for y in range(offset[1]//SIZE, (screen.get_height() + offset[1])// SIZE + 2):
            if y == 0:
                self.draw_line(screen, (0, y*SIZE - offset[1]), (screen.get_width(), y*SIZE - offset[1]), 'blue')
            else:
                self.draw_line(screen, (0, y*SIZE - offset[1]), (screen.get_width(), y*SIZE - offset[1]))

        pg.draw.lines(screen, 'red', False, points, 3)
        
        x, y = Mouse.pos
        self.font.render_to(screen, (x + 15, y) , f'({(x + offset[0])//SIZE:.2f}, {-(y + offset[1])//SIZE:.2f})', 'gold')
   
        # screen.blit(self.image, (0 - offset[0], 0 - offset[1]))
      
    def draw_line(self, screen, start, end, color='white', width=1):
        pg.draw.line(screen, color, start, end, width)