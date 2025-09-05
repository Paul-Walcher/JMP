
import pygame
from math import sqrt

def draw_circle(screen, color, x, y, r, steps = 100):

	dots_1 = [(i/steps, sqrt(r*r - (r*r*i*i/(steps*steps)))) for i in range(steps)]

	for d in dots_1:

		screen.set_at((int(d[0]*r + x), int(d[1]+y)), color)