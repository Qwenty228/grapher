import pygame as pg
from typing import Tuple, Dict
from pygame.math import Vector2 
import pygame.freetype
import math


class Font:
    loaded:Dict[Tuple[str, int], pg.freetype.Font]  = {}
    def __new__(cls, name, size) -> pg.freetype.Font:
        if (name, size) not in cls.loaded:
            cls.loaded[(name, size)] = pg.freetype.Font(name, size)
        return cls.loaded[(name, size)]


class Grapher:
    def __init__(self, size, pos) -> None:
        self.w, self.h = self.size =  size
        self.pos = Vector2(pos)
        self.display = pg.Surface(self.size)


        self.movement = [False]*4
        self.origin = Vector2(self.w/2, self.h/2)

        self.divisions = 100              # scale of the graph
        self.division_interval = 10      # interval between each division
        self.step = round(self.divisions/self.division_interval)


        # self.function = lambda x: - math.sin(x)
        

    def function_plot(self, function):
        points = []
        for x in range(-10, 10+1):
            y = -function(x) * self.step
            x *= self.step
            points.append((x + self.origin.x, y  + self.origin.y))
        
        
        pg.draw.lines(self.display, 'black', False, points, 2)
        

    def render(self, surface):
        self.origin.x += self.movement[0] - self.movement[1]
        self.origin.y += self.movement[2] - self.movement[3]

        self.display.fill('white')
        self.draw_grid()

        # self.function_plot(math.sin)

        surface.blit(self.display, self.pos)

    def draw_grid(self):
        for x in range(int(self.origin.x % self.divisions), self.w, self.divisions):
            pg.draw.line(self.display, 'gray', (x, 0), (x, self.h))
            Font(None, 20).render_to(self.display, (x, self.origin.y), str(int(self.division_interval*(x-self.origin.x)/self.divisions)), 'black')

        for y in range(int(self.origin.y % self.divisions), self.h, self.divisions):
            pg.draw.line(self.display, 'gray', (0, y), (self.w, y))
            Font(None, 20).render_to(self.display, (self.origin.x, y), str(int(self.division_interval*(y-self.origin.y)/self.divisions)), 'black')

        pg.draw.line(self.display, 'red', (self.origin.x, 0), (self.origin.x, self.h))
        pg.draw.line(self.display, 'red', (0, self.origin.y), (self.w, self.origin.y))
