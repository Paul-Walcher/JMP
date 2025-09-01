import pygame
from engine import Engine

pygame.init()

def main():

	width, height = 800, 600

	quit : bool = False

	main_engine = Engine(width, height)

	clock = pygame.time.Clock()
	fps = 60

	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("JMP")

	while not quit:

		clock.tick(fps)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				quit = True

		main_engine.manage_keys(pygame.key.get_pressed())
		main_engine.manage_movement()

		main_engine.redraw(screen)







if __name__ == "__main__":

	main()