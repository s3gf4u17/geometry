import numpy as np
import pygame as pg
from OpenGL.GL import *

class Square:
    def __init__(self):
        # x, y, z, r, g, b, texX, texY
        self.vertices = np.array((
            -0.2,-0.2,0.0,1.0,1.0,1.0,0.0,1.0,
            0.2,-0.2,0.0,1.0,1.0,1.0,1.0,1.0,
            0.2,0.2,0.0,1.0,1.0,1.0,1.0,0.0,
            -0.2,0.2,0.0,1.0,1.0,1.0,0.0,0.0,
        ),dtype=np.float32)
        self.vertex_count=4
        self.vao=glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo=glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER,self.vbo)
        glBufferData(GL_ARRAY_BUFFER,self.vertices.nbytes,self.vertices,GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,32,ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1,3,GL_FLOAT,GL_FALSE,32,ctypes.c_void_p(12))
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2,2,GL_FLOAT,GL_FALSE,32,ctypes.c_void_p(24))
    
    def destroy(self):
        glDeleteVertexArrays(1,(self.vao,))
        glDeleteBuffers(1,(self.vbo,))

class Material:
    def __init__(self,filepath):
        self.texture=glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D,self.texture)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_REPEAT) # s = 0 <- left side of the texture, s = 1 <- right side of the texture
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_REPEAT) # t = 0 <- top side of the texture, t = 1 <- bottom side of the texture
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST) # what happens when we try to minify texture
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR) # what happens when we try to magnify texture
        image=pg.image.load(filepath).convert()
        image_width,image_height=image.get_rect().size
        image_data=pg.image.tostring(image,"RGBA")
        glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,image_width,image_height,0,GL_RGBA,GL_UNSIGNED_BYTE,image_data)
        glGenerateMipmap(GL_TEXTURE_2D)
    
    def use(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D,self.texture)

    def destroy(self):
        glDeleteTextures(1,(self.texture,))