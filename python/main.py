import pygame as pg
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram,compileShader
import numpy as np
import pyrr

from lib import CubeMesh,Mesh,Material,Shader

class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((640,480), pg.OPENGL|pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(0.1, 0.2, 0.2, 1)
        self.shader = Shader("../shaders/shader.vert", "../shaders/shader.frag").program
        glUniform1i(glGetUniformLocation(self.shader, "imageTexture"), 0)
        self.figure = CubeMesh()
        glEnable(GL_DEPTH_TEST)
        self.texture = Material("../textures/mitten.png")
        self.mesh = Mesh(position=[0,0,-5],eulers=[-25,0,0])

        projection_transform = pyrr.matrix44.create_perspective_projection(
            fovy = 45, aspect = 640/480, 
            near = 0.1, far = 10, dtype=np.float32
        )
        glUniformMatrix4fv(
            glGetUniformLocation(self.shader,"projection"),
            1, GL_FALSE, projection_transform
        )
        self.modelMatrixLocation = glGetUniformLocation(self.shader,"model")

    def mainloop(self):
        running = True
        while (running):
            #check events
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    running = False
            
            #update mesh
            self.mesh.eulers[2] += 0.25
            if self.mesh.eulers[2] > 360:
                self.mesh.eulers[2] -= 360
            self.mesh.eulers[1] += 0.5
            if self.mesh.eulers[1] > 360:
                self.mesh.eulers[1] -= 360
            self.mesh.eulers[0] += 0.75
            if self.mesh.eulers[0] > 360:
                self.mesh.eulers[0] -= 360
            
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            model_transform = pyrr.matrix44.create_identity(dtype=np.float32)
            """
                pitch: rotation around x axis
                roll:rotation around z axis
                yaw: rotation around y axis
            """
            model_transform = pyrr.matrix44.multiply(
                m1=model_transform, 
                m2=pyrr.matrix44.create_from_eulers(
                    eulers=np.radians(self.mesh.eulers), dtype=np.float32
                )
            )
            model_transform = pyrr.matrix44.multiply(
                m1=model_transform, 
                m2=pyrr.matrix44.create_from_translation(
                    vec=np.array(self.mesh.position),dtype=np.float32
                )
            )
            glUniformMatrix4fv(self.modelMatrixLocation,1,GL_FALSE,model_transform)
            # self.texture.use()
            glBindVertexArray(self.figure.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.figure.vertex_count)
            pg.display.flip()
            #timing
            self.clock.tick(60)
        self.quit()

    def quit(self):
        self.figure.destroy()
        pg.quit()

app=App()
app.mainloop()