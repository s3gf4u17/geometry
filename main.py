### testing opengl features
import pygame as pg
from OpenGL.GL import *
import numpy as np
import ctypes
from OpenGL.GL.shaders import compileProgram,compileShader

# we need vertex shader and fragment shader
# vertex runs once for the vertex, to position it on the screen (possibly transformations later)
# fragment shader runs once per pixel and is responsible for calculating pixel's color

class Square:
    def __init__(self):
        # x, y, z, r, g, b
        self.vertices = np.array((
            -0.9,-0.9,0.0,1.0,0.0,0.0,
            0.9,-0.9,0.0,0.0,1.0,0.0,
            0.9,0.9,0.0,0.0,0.0,1.0,
            -0.9,0.9,0.0,0.0,0.0,1.0,
        ),dtype=np.float32)
        self.vertex_count=4
        self.vao=glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo=glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER,self.vbo)
        glBufferData(GL_ARRAY_BUFFER,self.vertices.nbytes,self.vertices,GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,24,ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1,3,GL_FLOAT,GL_FALSE,24,ctypes.c_void_p(12))
    
    def destroy(self):
        glDeleteVertexArrays(1,(self.vao,))
        glDeleteBuffers(1,(self.vbo,))

class Triangle:
    def __init__(self):
        # x, y, z, r, g, b
        self.vertices = (
            -0.9,-0.9,0.0,1.0,0.0,0.0, # vertex is not only position but also all other data connected to vertex
            0.9,-0.9,0.0,0.0,1.0,0.0, # x and y go from -1 to 1 # z represents depth (either flat or no)
            0.9,0.9,0.0,0.0,0.0,1.0,
        )
        self.vertices=np.array(self.vertices,dtype=np.float32) # data type is perfect for c data reading
        self.vertex_count = 3
        self.vao=glGenVertexArrays(1) # declare vertex data (how opengl should display them)
        glBindVertexArray(self.vao)
        self.vbo=glGenBuffers(1) # vertex buffer object 
        glBindBuffer(GL_ARRAY_BUFFER,self.vbo) # bind buffer vbo to GL_ARRAY_BUFFER name
        glBufferData(GL_ARRAY_BUFFER,self.vertices.nbytes,self.vertices,GL_STATIC_DRAW) # ship our vertices to graphics card, STATIC_DRAW - saving data once and reading more times
        glEnableVertexAttribArray(0) # define an vbo attribute
        glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,24,ctypes.c_void_p(0)) # describe it (vertices are 12 bits long, and they start in 0 pos, going 3 bytes and skipping 3)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1,3,GL_FLOAT,GL_FALSE,24,ctypes.c_void_p(12)) # (colors are 12 bits long, and they start in 0 pos, going 3 bytes and skipping 3)

    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,)) # glDeleteVertexArrays requires list of arguments - thats what comma is for
        glDeleteBuffers(1,(self.vbo,))

class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((640,480),pg.OPENGL|pg.DOUBLEBUF)
        self.clock=pg.time.Clock()
        # initialize opengl
        glClearColor(0.1,0.2,0.2,1)
        self.shader=self.createShader("shaders/triangle.vert","shaders/triangle.frag")
        glUseProgram(self.shader)
        self.triangle=Triangle()
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
            # check events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running=False
            # refresh screen
            glClear(GL_COLOR_BUFFER_BIT)
            glUseProgram(self.shader)
            glBindVertexArray(self.triangle.vao)
            glDrawArrays(GL_POLYGON,0,self.triangle.vertex_count)
            pg.display.flip()
            # timing
            self.clock.tick(60)
        self.quit()

    def quit(self):
        self.triangle.destroy()
        glDeleteProgram(self.shader)
        pg.quit()

if __name__ == "__main__":
    app=App()