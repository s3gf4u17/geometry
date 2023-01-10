import pygame as pg
from OpenGL.GL import *
import numpy as np
import ctypes
from OpenGL.GL.shaders import compileProgram,compileShader
from classes import Square, Material

class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((1000,580),pg.OPENGL|pg.DOUBLEBUF)
        self.clock=pg.time.Clock()
        glClearColor(0.1,0.2,0.2,1)
        self.shader=self.createShader("shaders/triangle.vert","shaders/triangle.frag")
        glUseProgram(self.shader)
        glUniform1i(glGetUniformLocation(self.shader,"imageTexture"),0)
        self.figure=Square()
        self.texture=Material("textures/stone.jpg")
        self.mainLoop()

    def createShader(self,vertexFilePath,fragmentFilePath):
        with open(vertexFilePath,"r") as f:
            vertex_src=f.readlines()
        with open(fragmentFilePath,"r") as f:
            fragment_src=f.readlines()
        shader = compileProgram(
            compileShader(vertex_src,GL_VERTEX_SHADER),
            compileShader(fragment_src,GL_FRAGMENT_SHADER)
        )
        return shader

    def mainLoop(self):
        running=True
        while running:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    running=False
            glClear(GL_COLOR_BUFFER_BIT)
            glUseProgram(self.shader)
            glBindVertexArray(self.figure.vao)
            glDrawArrays(GL_POLYGON,0,self.figure.vertex_count)
            pg.display.flip()
            self.clock.tick(60)
        self.quit()

    def quit(self):
        self.figure.destroy()
        self.texture.destroy()
        glDeleteProgram(self.shader)
        pg.quit()

if __name__ == "__main__":
    app=App()