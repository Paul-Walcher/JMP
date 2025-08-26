import pygame 

class Engine:

	def __init__(self):
		pass

	def redraw(self, screen):

		screen.fill((0xFF, 0xFF, 0xFF))
		pygame.display.flip()
		