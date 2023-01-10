### testing opengl features
import pygame as pg
from OpenGL.GL import *

class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((640,480),pg.OPENGL|pg.DOUBLEBUF)
        self.clock=pg.time.Clock()
        # initialize opengl
        glClearColor(1,0.2,0.2,1)
        self.mainLoop()

    def mainLoop(self):
        running=True
        while running:
            # check events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running=False
            # refresh screen
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()
            # timing
            self.clock.tick(60)
        self.quit()

    def quit(self):
        pg.quit()

if __name__ == "__main__":
    app=App()