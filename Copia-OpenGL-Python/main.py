#Constelação dos Guardiões
import xml.parsers
import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random
import math

class Pontos:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Circulos():
  def __init__(self, x, y, raio, r, g, b):
    self.x = x
    self.y = y
    self.raio = raio
    self.r = r
    self.g = g
    self.b = b
    self.rAnt = 1
    self.gAnt = 1
    self.bAnt = 1
  def trocar_tema(self):
    aux = self.r
    self.r = self.rAnt
    self.rAnt = aux
    aux = self.g
    self.g = self.gAnt
    self.gAnt = aux
    aux = self.b
    self.b = self.bAnt
    self.bAnt = aux
  def set_rAnt(self, r):
    self.rAnt = r
  def set_gAnt(self, g):
    self.gAnt = g
  def set_bAnt(self, b):
    self.bAnt = b
    

class Fundo():
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b
    self.rAnt = 0
    self.gAnt = 0
    self.bAnt = 0
    self.escuro = False
  def set_r(self, r):
    self.r = r
  def set_g(self, g):
    self.g = g
  def set_b(self, b):
    self.b = b
  def trocar_tema(self):
    if self.escuro == True:
      self.escuro = False
    else:
      self.escuro = True
    aux = self.r
    self.r = self.rAnt
    self.rAnt = aux
    aux = self.g
    self.g = self.gAnt
    self.gAnt = aux
    aux = self.b
    self.b = self.bAnt
    self.bAnt = aux
    

estrelas = []
estrelasextras = []
fundo = Fundo(0, 0, 0.3)

def desenhar_estrela(x, y, raio, r, g, b):
  passos = 100
  angulo = 2.0*math.pi/passos
  gl.glBegin(gl.GL_TRIANGLE_FAN)
  for i in range(0, passos):
    teta = 2.0*math.pi*i/passos
    cx = raio*math.cos(teta)
    cy = raio*math.sin(teta)
    gl.glColor(r, g, b)
    gl.glVertex3f(x + cx, y+cy, 0)
  gl.glEnd()

def desenhar_linha(x1, x2, y1, y2):
  gl.glBegin(gl.GL_LINES)
  gl.glColor3f(1, 1, 1)
  gl.glVertex3f(x1, y1, 0)
  gl.glVertex3f(x2, y2, 0)
  gl.glEnd()


def teclado(tecla, x, y):
  #tecla n
  if tecla[0] == 110:
    if fundo.escuro == True:
      est = Circulos(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(0, 0.5), 1, 1, 1)
      est.set_rAnt(random.random())
      est.set_gAnt(random.random())
      est.set_bAnt(random.random())
      estrelasextras.append(est)
    else:
      est = Circulos(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(0, 0.5), random.random(), random.random(), random.random())
      estrelasextras.append(est)
      
    for i in range(0, len(estrelasextras)):
      desenhar_estrela(estrelasextras[i].x, estrelasextras[i].y, estrelasextras[i].raio, estrelasextras[i].r, estrelasextras[i].g, estrelasextras[i].b)
    glut.glutSwapBuffers()

  #tecla x
  if tecla[0] == 120:
    if estrelasextras:
      estrelasextras.pop()
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    for i in range(0, len(estrelas)):
      desenhar_estrela(estrelas[i].x, estrelas[i].y, estrelas[i].raio, estrelas[i].r, estrelas[i].g, estrelas[i].b)
      if(i>0):
        desenhar_linha(estrelas[i-1].x, estrelas[i].x, estrelas[i-1].y, estrelas[i].y, )
    glut.glutSwapBuffers()
    
    for i in range(0, len(estrelasextras)):
      desenhar_estrela(estrelasextras[i].x, estrelasextras[i].y, estrelasextras[i].raio, estrelasextras[i].r, estrelasextras[i].g, estrelasextras[i].b)
      glut.glutSwapBuffers()

  #tecla r
  if tecla[0] == 114:
    estrelasextras.clear()
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    for i in range(0, len(estrelas)):
      desenhar_estrela(estrelas[i].x, estrelas[i].y, estrelas[i].raio, estrelas[i].r, estrelas[i].g, estrelas[i].b)
      if(i>0):
        desenhar_linha(estrelas[i-1].x, estrelas[i].x, estrelas[i-1].y, estrelas[i].y, )
    glut.glutSwapBuffers()

  #tecla t
  if tecla[0] == 116:
    fundo.trocar_tema()
    gl.glClearColor(fundo.r, fundo.g, fundo.b, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    for i in range (0, len(estrelas)):
      estrelas[i].trocar_tema()
    for i in range (0, len(estrelasextras)):
      estrelasextras[i].trocar_tema()
    #desenhando as estrelas
    for i in range (0, len(estrelas)):
      desenhar_estrela(estrelas[i].x, estrelas[i].y, estrelas[i].raio, estrelas[i].r, estrelas[i].g, estrelas[i].b)
      if(i>0):
        desenhar_linha(estrelas[i-1].x, estrelas[i].x, estrelas[i-1].y, estrelas[i].y, )
    for i in range(0, len(estrelasextras)):
      desenhar_estrela(estrelasextras[i].x, estrelasextras[i].y, estrelasextras[i].raio, estrelasextras[i].r, estrelasextras[i].g, estrelasextras[i].b)
      
    glut.glutSwapBuffers()
      
      
      
def display():
  gl.glClearColor(fundo.r, fundo.g, fundo.b, 1)
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  for i in range(0, len(estrelas)):
    desenhar_estrela(estrelas[i].x, estrelas[i].y, estrelas[i].raio, estrelas[i].r, estrelas[i].g, estrelas[i].b)
    if(i>0):
      desenhar_linha(estrelas[i-1].x, estrelas[i].x, estrelas[i-1].y, estrelas[i].y, )
  glut.glutSwapBuffers()
  
estrelas.append(Circulos(0, 0.7, 0.035, 0.8, 0, 0))
estrelas.append(Circulos(0.4, 0.5, 0.008, 0.5, 0.8, 0))
estrelas.append(Circulos(0.4, 0.2, 0.03, 0.1, 0.8, 0.8))
estrelas.append(Circulos(0, 0, 0.05, 1, 1, 0))
estrelas.append(Circulos(-0.4, -0.2, 0.025, 1, 1, 1))
estrelas.append(Circulos(-0.4, -0.5, 0.01, 0.7, 0.3, 1))
estrelas.append(Circulos(0, -0.7, 0.029, 0.5, 0.5, 0.5))
glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
