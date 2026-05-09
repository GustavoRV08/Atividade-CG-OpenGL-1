import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random
import math

class Pontos:
  def __init__(self):
    self.x = 0
    self.y = 0

  def set_x(self, x):
    self.x = x

  def set_y(self, y):
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
bases = []
alturas = []

def desenhar_triangulo():
  for i in range(0, len(triangulos)):
    gl.glShadeModel(gl.GL_FLAT)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(triangulos[i].r, triangulos[i].g, triangulos[i].b, 0)
    gl.glVertex3f(triangulos[i].pontos[0].x-i/10, triangulos[i].pontos[0].y, 0)
    gl.glVertex3f(triangulos[i].pontos[1].x-i/10, triangulos[i].pontos[1].y, 0)
    gl.glVertex3f(triangulos[i].pontos[2].x-i/10, triangulos[i].pontos[2].y, 0)
    gl.glEnd()
    glut.glutPostRedisplay()


def display():
  desenhar_triangulo()
  glut.glutSwapBuffers()


face = Faces()

for i in range(0, 5):
  bases.append(int(input(f"Digite o tamanho da base do triângulo {i+1}: ")))
  alturas.append(int(input(f"Digite a altura do triângulo {i+1}: ")))
  face = Faces()
  p1 = Pontos()
  p1.set_x(0)
  p1.set_y(0)
  face.add_ponto(p1)
  p2 = Pontos()
  p2.set_x(((bases[i]/2)/100))
  p2.set_y(alturas[i]/100)
  face.add_ponto(p2)
  p3 = Pontos()
  p3.set_x((bases[i]/100))
  p3.set_y(0)
  face.add_ponto(p3)
  face.set_r(random.random())
  face.set_g(random.random())
  face.set_b(random.random())
  triangulos.append(face)

glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutMainLoop()
