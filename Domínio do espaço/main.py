import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random
import math

class Pontos:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Faces:
  def __init__(self):
    self.pontos = []
    self.r = 0
    self.g = 0
    self.b = 0
    self.a = 0

  def add_ponto(self, ponto):
    self.pontos.append(ponto)

  def set_r(self, r):
    self.r = r

  def set_g(self, g):
    self.g = g

  def set_b(self, b):
    self.b = b

  def set_a(self, a):
    self.a = a

triangulos = []
  
def display():
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glShadeModel(gl.GL_FLAT)
  gl.glBegin(gl.GL_TRIANGLES)
  gl.glColor3f(1, 0, 0)
  gl.glVertex3f(triangulos[0].pontos[0].x, triangulos[0].pontos[0].y, 0)
  gl.glVertex3f(triangulos[0].pontos[1].x, triangulos[0].pontos[1].y, 0)
  gl.glVertex3f(triangulos[0].pontos[2].x, triangulos[0].pontos[2].y, 0)
  gl.glEnd()

  gl.glShadeModel(gl.GL_FLAT)
  gl.glBegin(gl.GL_TRIANGLES)
  gl.glColor3f(0, 1, 0)
  gl.glVertex3f(triangulos[1].pontos[0].x, triangulos[1].pontos[0].y, 0)
  gl.glVertex3f(triangulos[1].pontos[1].x, triangulos[1].pontos[1].y, 0)
  gl.glVertex3f(triangulos[1].pontos[2].x, triangulos[1].pontos[2].y, 0)
  gl.glEnd()

  gl.glShadeModel(gl.GL_FLAT)
  gl.glBegin(gl.GL_TRIANGLES)
  gl.glColor3f(0, 0, 1)
  gl.glVertex3f(triangulos[2].pontos[0].x, triangulos[2].pontos[0].y, 0)
  gl.glVertex3f(triangulos[2].pontos[1].x, triangulos[2].pontos[1].y, 0)
  gl.glVertex3f(triangulos[2].pontos[2].x, triangulos[2].pontos[2].y, 0)
  gl.glEnd()

  gl.glShadeModel(gl.GL_FLAT)
  gl.glBegin(gl.GL_LINES)
  gl.glColor3f(1, 1, 1)
  gl.glVertex3f(-1, 0, 0)
  gl.glVertex3f(1, 0, 0)
  gl.glEnd()

  gl.glShadeModel(gl.GL_FLAT)
  gl.glBegin(gl.GL_LINES)
  gl.glColor3f(1, 1, 1)
  gl.glVertex3f(0, -1, 0)
  gl.glVertex3f(0, 1, 0)
  gl.glEnd()
  glut.glutSwapBuffers()
  

face1 = Faces()
p1 = Pontos(-0.7, 0.2)
p2 = Pontos(-0.7, 0.7)
p3 = Pontos(-0.4, 0.2)
face1.pontos.append(p1)
face1.pontos.append(p2)
face1.pontos.append(p3)
triangulos.append(face1)

face2 = Faces()
p1 = Pontos(0.7, 0.2)
p2 = Pontos(0.7, 0.7)
p3 = Pontos(0.4, 0.2)
face2.pontos.append(p1)
face2.pontos.append(p2)
face2.pontos.append(p3)
triangulos.append(face2)

face3 = Faces()
p1 = Pontos(-0.7, -0.2)
p2 = Pontos(-0.7, -0.7)
p3 = Pontos(-0.4, -0.2)
face3.pontos.append(p1)
face3.pontos.append(p2)
face3.pontos.append(p3)
triangulos.append(face3)

glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutMainLoop()
