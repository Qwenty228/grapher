import pygame as pg  
from graph import Graph
from utils.settings import *
from utils.fullscreen import Shader, Mouse


screen = pg.display.set_mode(SIZE, pg.RESIZABLE|pg.OPENGL|pg.DOUBLEBUF, vsync=1)



graph = Graph()
shader = Shader()


clock = pg.time.Clock()
running = True


while running:
    Mouse.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_F11:
                pg.display.toggle_fullscreen()
        shader.event(event)

    dt = clock.tick(60)/1000


    screen.fill('grey10')
    graph.update(dt)
    graph.draw(screen)

    shader.render(screen)
    pg.display.flip()

    pg.display.set_caption(f'FPS: {clock.get_fps():.2f}')   