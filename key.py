import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

vertices = (
	(0.75, -0.25, -0.5),
	(0.75, 0.25, -0.5),
	(-0.75, 0.25, -0.5),
	(-0.75, -0.25, -0.5),
	(0.75, -0.25, 0.5),
	(0.75, 0.25, 0.5),
	(-0.75, -0.25, 0.5),
	(-0.75, 0.25, 0.5),
	)

edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7),
	)

surfaces = (
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6),
	)

colors = (
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(0,0,0),
	(1,1,1),
	(0,1,1),
	)

def draw_cuboid():
	glBegin(GL_QUADS)
	for surface in surfaces:
		x = 0
		for vertex in surface:
			x+=1
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])
	glEnd()

	glBegin(GL_LINES)
	for egde in edges:
		for vertex in egde:
			glVertex3fv(vertices[vertex])
	glEnd()

def draw_cylinder():
	glRotatef(1, 1, 1.25, 12.5)
	glColor3f(1.0, 1.0, 0.0)
	quadratic = gluNewQuadric()
	gluQuadricNormals(quadratic, GLU_SMOOTH)
	gluQuadricTexture(quadratic, GL_TRUE)
	gluCylinder(quadratic, 0.15, 0.15, 2.5, 32, 32)

def draw_torus():
	glColor3f(0.0, 1.0, 0.0)
	glutWireTorus(0.2, 0.8, 50, 50)

def main():
	pygame.init()
	glutInit()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(75, (display[0]/display[1]), 0.1, 50.0)

	glTranslatef(0.0, 0.0, -10)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glTranslatef(-0.5, 0, 0)
				if event.key == pygame.K_RIGHT:
					glTranslatef(0.5, 0, 0)

				if event.key == pygame.K_UP:
					glTranslatef(0, 0.5, 0)
				if event.key == pygame.K_DOWN:
					glTranslatef(0, -0.5, 0)

				if event.key == pygame.K_SPACE:
					glRotatef(5, 0, 1, 0)	

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0, 0, 1.0)
				if event.button == 5:
					glTranslatef(0, 0, -1.0)


		glRotatef(1, 3, 1, 1)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		
		glTranslate(0.9, 0, 2)
		draw_cuboid()
		glTranslate(-0.9, 0, -2)
		glRotate(90,1,0,0)
		glTranslate(0,-1,0)
		draw_torus()
		glTranslate(0, 1, 0);
		glRotate(-90, 1, 0, 0)

		draw_cylinder()
		
		pygame.display.flip()
		pygame.time.wait(10)

main()