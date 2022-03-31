import math
from OpenGL.arrays import vbo
from OpenGL.GLU import *
from OpenGL.GL import *
from pygame.locals import *
import pygame
import time
import numpy as np


def tick(i):
    # Draw sinewave
    for x in range(200):
        x = x/2.0
        y1 = math.sin(math.sin(math.radians(x+i) * 2) * 5 + 20) * 5 + 20
        quad_plotter((2*x, y1+30, 0), 3, (143, 0, 255))
        quad_plotter((2*x, y1+20, 0), 3, (143, 143, 255))
        quad_plotter((2*x, y1+10, 0), 3, (0, 143, 255))
        quad_plotter((2*x, y1, 0), 3, (0, 0, 255))
        quad_plotter((2*x, y1-10, 0), 3, (255, 0, 255))
        quad_plotter((2*x, y1-20, 0), 3, (255, 255, 255))


FPS_TARGET = 50


def quad_plotter(point, size, color):
    glBegin(GL_QUADS)
    glColor3f(*color)
    x, y, z = point
    s = size/5.0
    glVertex3fv((x-s, y-s, z))
    glVertex3fv((x+s, y-s, z))
    glVertex3fv((x+s, y+s, z))
    glVertex3fv((x-s, y+s, z))
    glEnd()


def main():

    pygame.init()
    pygame.display.set_mode((1200, 800), OPENGL | DOUBLEBUF)
    glEnable(GL_DEPTH_TEST)  # use our zbuffer

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # setup the camera
    glMatrixMode(GL_PROJECTION)
    glOrtho(-10, 110, -10, 70, -1, 1)

    nt = int(time.time() * 1000)

    for i in range(2**63):
        nt += 1000//FPS_TARGET

        event = pygame.event.poll()
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            break

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        tick(i)

        pygame.display.flip()

        ct = int(time.time() * 1000)
        pygame.time.wait(max(1, nt - ct))

        if i % FPS_TARGET == 0:
            print(nt-ct)


if __name__ == '__main__':
    main()
