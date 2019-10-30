import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_cylinder():
	glRotatef(1, 1, 1.25, 12.5)
	glColor3f(1.0, 1.0, 0.0)
	quadratic = gluNewQuadric()
	gluQuadricNormals(quadratic, GLU_SMOOTH)
	gluQuadricTexture(quadratic, GL_TRUE)
	gluCylinder(quadratic, 0.15, 0.15, 2.5, 32, 32)

def main():
	pygame.init()
	glutInit()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	glTranslatef(0.0, 0.0, -5)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		glRotatef(1, 2, 1.5, 0.3)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		
		draw_cylinder()
		
		pygame.display.flip()
		pygame.time.wait(10)

main()