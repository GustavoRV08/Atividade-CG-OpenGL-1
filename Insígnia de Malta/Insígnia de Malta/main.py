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
    self.r = 1
    self.g = 1
    self.b = 1
    self.a = 1

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

def teclado(tecla, x, y):
  r = random.random()
  g = random.random()
  b = random.random()
  match tecla[0]:
    case 99:
      for i in range(0, len(triangulos)):
        triangulos[i].set_r(r)
        triangulos[i].set_g(g)
        triangulos[i].set_b(b)
  desenhar_insignia()
  glut.glutSwapBuffers()

def desenhar_insignia():
  for i in range(0, len(triangulos)):
    gl.glShadeModel(gl.GL_FLAT)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(triangulos[i].r, triangulos[i].g, triangulos[i].b)
    gl.glVertex3f(triangulos[i].pontos[0].x, triangulos[i].pontos[0].y, 0)
    gl.glVertex3f(triangulos[i].pontos[1].x, triangulos[i].pontos[1].y, 0)
    gl.glVertex3f(triangulos[i].pontos[2].x, triangulos[i].pontos[2].y, 0)
    gl.glEnd()

def display():
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  desenhar_insignia()
  glut.glutSwapBuffers()

#baixo
face1 = Faces()
p1 = Pontos(0, 0)
p2 = Pontos(-0.3, -0.8)
p3 = Pontos(0, -0.4)
face1.pontos.append(p1)
face1.pontos.append(p2)
face1.pontos.append(p3)
triangulos.append(face1)

face2 = Faces()
p1 = Pontos(0, 0)
p2 = Pontos(0.3, -0.8)
p3 = Pontos(0, -0.4)
face2.pontos.append(p1)
face2.pontos.append(p2)
face2.pontos.append(p3)
triangulos.append(face2)

face3 = Faces()
p1 = Pontos(0, 0)
p2 = Pontos(0.3, 0.8)
p3 = Pontos(0, 0.4)
face3.pontos.append(p1)
face3.pontos.append(p2)
face3.pontos.append(p3)
triangulos.append(face3)

face4 = Faces()
p1 = Pontos(0, 0)
p2 = Pontos(-0.3, 0.8)
p3 = Pontos(0, 0.4)
face4.pontos.append(p1)
face4.pontos.append(p2)
face4.pontos.append(p3)
triangulos.append(face4)

face5 = Faces()
p1 = Pontos(0, 0)
p2 = Pontos(0.8, -0.3)
p3 = Pontos(0.4, 0)
face5.pontos.append(p1)
face5.pontos.append(p2)
face5.pontos.append(p3)
triangulos.append(face5)

face5 = Faces()
p1 = Pontos(0, 0)
p2 = Pontos(0.8, 0.3)
p3 = Pontos(0.4, 0)
face5.pontos.append(p1)
face5.pontos.append(p2)
face5.pontos.append(p3)
triangulos.append(face5)

face6 = Faces()
p1 = Pontos(0, 0)
p2 = Pontos(-0.8, 0.3)
p3 = Pontos(-0.4, 0)
face6.pontos.append(p1)
face6.pontos.append(p2)
face6.pontos.append(p3)
triangulos.append(face6)

face7 = Faces()
p1 = Pontos(0, 0)
p2 = Pontos(-0.8, -0.3)
p3 = Pontos(-0.4, 0)
face7.pontos.append(p1)
face7.pontos.append(p2)
face7.pontos.append(p3)
triangulos.append(face7)

glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()

