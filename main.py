import pygame
from engine import Engine

pygame.init()
main_engine = Engine()

def main():

	width, height = 800, 600

	quit : bool = False

	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("JMP")

	while not quit:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				quit = True

		main_engine.redraw(screen)






if __name__ == "__main__":

	main()