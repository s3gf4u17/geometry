import pygame as pg
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram,compileShader
import numpy as np
import pyrr

class Obj:
    def __init__(self,path,type):
        if type=="txt":
            with open (path,"r") as f:
                self.vertices=np.array([float(v) for v in "".join([v.strip() for v in f.readlines()]).split(",")],dtype=np.float32)
        elif type=="obj":
            with open(path,"r") as f:
                lines=f.readlines()

            v=[]
            vn=[]
            vt=[]
            f=[]
            merged=[]

            for line in lines:
                linetype=line.split(" ")[0]
                line=line.replace("\n","")
                if linetype=="v":
                    v.append([float(element) for element in line.split(" ")[1:]])
                elif linetype=="vt":
                    vt.append([float(element) for element in line.split(" ")[1:]])
                elif linetype=="vn":
                    vn.append([float(element) for element in line.split(" ")[1:]])
                elif linetype=="f":
                    f.append([element.split("/") for element in line.split(" ")[1:]])

            f = [item for sublist in f for item in sublist]

            for element in f:
                merged.append(v[int(element[0])-1][0])
                merged.append(v[int(element[0])-1][1])
                merged.append(v[int(element[0])-1][2])
                merged.append(vt[int(element[1])-1][0])
                merged.append(vt[int(element[1])-1][1])
                merged.append(vn[int(element[2])-1][0])
                merged.append(vn[int(element[2])-1][1])
                merged.append(vn[int(element[2])-1][2])

            ### merged
            ### x, y, z, s, t, nx, ny, nz

            self.vertices=np.array(merged,dtype=np.float32)

class Mesh:
    def __init__(self, position, eulers):
        self.position = np.array(position, dtype=np.float32)
        self.eulers = np.array(eulers, dtype=np.float32)

class CubeMesh:
    def __init__(self):
        # x, y, z, s, t, nx, ny, nz
        self.vertices=Obj("../blender/untitled.obj","obj").vertices
        self.vertex_count = len(self.vertices)//8

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))
    
    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1,(self.vbo,))

class Material:    
    def __init__(self, filepath):
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        image = pg.image.load(filepath).convert()
        image_width,image_height = image.get_rect().size
        img_data = pg.image.tostring(image,'RGBA')
        glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,image_width,image_height,0,GL_RGBA,GL_UNSIGNED_BYTE,img_data)
        glGenerateMipmap(GL_TEXTURE_2D)

    def use(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D,self.texture)

    def __del__(self):
        glDeleteTextures(1, (self.texture,))

class Shader:
    def __init__(self,vertexFilepath, fragmentFilepath):
        with open(vertexFilepath,"r") as f:
            vertex=f.readlines()
        with open(fragmentFilepath,"r") as f:
            fragment=f.readlines()
        self.program=compileProgram(compileShader(vertex,GL_VERTEX_SHADER),compileShader(fragment,GL_FRAGMENT_SHADER))
        glUseProgram(self.program)

    def __del__(self):
        glDeleteProgram(self.program)