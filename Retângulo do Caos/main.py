import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random

class Retangulo:
  altura = 0
  largura = 0


def teclado(tecla, x, y):
  print(f"teclou, tecla digitada: {tecla}")
  if tecla[0] == 32:
    glut.glutSwapBuffers()
    gl.glClearColor(random.random(), random.random(), random.random(), 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glShadeModel(gl.GL_FLAT)
    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(random.random(), random.random(), random.random(), 1)
    gl.glVertex3f(0, 0, 0)
    gl.glVertex3f(r.altura/100, 0, 0)
    gl.glVertex3f(r.altura/100, r.largura/100, 0)
    gl.glVertex3f(0, r.largura/100, 0)
    gl.glEnd()
    gl.glFlush()
    glut.glutPostRedisplay()

def display():
  glut.glutSwapBuffers()
  gl.glShadeModel(gl.GL_FLAT)
  gl.glBegin(gl.GL_QUADS)
  gl.glColor3f(random.random(), random.random(), random.random(), 1)
  gl.glVertex3f(0, 0, 0)
  gl.glVertex3f(r.altura/100, 0, 0)
  gl.glVertex3f(r.altura/100, r.largura/100, 0)
  gl.glVertex3f(0, r.largura/100, 0)
  gl.glEnd()
  gl.glFlush()


r = Retangulo
r.altura = int(input("Digite a altura do retângulo: "))
r.largura = int(input("Digite a largura do retângulo: "))

glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
