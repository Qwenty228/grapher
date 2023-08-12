import pygame as pg

from script.grapher import Grapher




class Window:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((800, 600), pg.RESIZABLE|pg.SCALED)
        pg.display.set_caption("Complex plot")
        self.clock = pg.time.Clock()
        self.grapher = Grapher((700, 400), (50, 100))



    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
                        pg.quit()
                        exit()

                    if event.key == pg.K_a:
                        self.grapher.movement[0] = True
                    if event.key == pg.K_d:
                        self.grapher.movement[1] = True
                    if event.key == pg.K_w:
                        self.grapher.movement[2] = True
                    if event.key == pg.K_s:
                        self.grapher.movement[3] = True
                
                if event.type == pg.KEYUP:
                    if event.key == pg.K_a:
                        self.grapher.movement[0] = False
                    if event.key == pg.K_d:
                        self.grapher.movement[1] = False
                    if event.key == pg.K_w:
                        self.grapher.movement[2] = False
                    if event.key == pg.K_s:
                        self.grapher.movement[3] = False
                

            self.grapher.render(self.screen)
            
            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    Window().run()