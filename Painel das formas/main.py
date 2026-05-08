import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random
import math

passos = 100
angulo = 3.1415926 * 2.0/passos

def display():
  glut.glutSwapBuffers()
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  #circulos
  gl.glShadeModel(gl.GL_FLAT)
  posX = 0
  posY = 0
  raio = 0.3
  antX = posX
  antY = posY - raio
  for i in  range(1, passos+1):
    novoX = raio * math.sin(angulo*i)
    novoY = -raio * math.cos(angulo*i)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(1, 0, 0)
    gl.glVertex3f(0, 0, 0)
    gl.glVertex3f(antX, antY, 0)
    gl.glVertex3f(novoX, novoY, 0)
    gl.glEnd()
    antX = novoX
    antY = novoY
  #triangulo
  gl.glShadeModel(gl.GL_FLAT)
  gl.glBegin(gl.GL_TRIANGLES)
  gl.glColor3f(0, 1, 0)
  gl.glVertex3f(-0.7, 0.0, 0.0)
  gl.glVertex3f(-0.7, 0.5, 0)
  gl.glVertex3f(-0.5, 0.0, 0)
  gl.glEnd()
  #quadrado
  gl.glShadeModel(gl.GL_FLAT)
  gl.glBegin(gl.GL_QUADS)
  gl.glColor3f(0, 0, 1)
  gl.glVertex3f(0.4, 0, 0)
  gl.glVertex3f(0.4, 0.4, 0)
  gl.glVertex3f(0.8, 0.4, 0)
  gl.glVertex3f(0.8, 0.0, 0)
  gl.glEnd()
  #forma extra
  gl.glShadeModel(gl.GL_FLAT)
  gl.glBegin(gl.GL_POLYGON)
  gl.glColor3f(1, 0, 1)
  gl.glVertex3f(0.9, 0.0, 0)
  gl.glVertex3f(0.9, 0.5, 0)
  gl.glVertex3f(0.94, 0.54, 0)
  gl.glVertex3f(0.98, 0.5, 0)
  gl.glVertex3f(0.98, 0, 0)
  gl.glVertex3f(0.94, -0.05, 0)
  gl.glEnd()


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutMainLoop()
