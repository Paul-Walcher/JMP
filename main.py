import pygame
from engine import Engine

from map import *
from Objects.Blocks.brick import Brick



pygame.init()

gmap = Map(50, 50)
gmap.map[5] = [ObjectEnum.BRICK for i in range(10)] + [ObjectEnum.NONE for i in range(40)]
gmap.map[10] = [ObjectEnum.BRICK for i in range(10)] + [ObjectEnum.NONE for i in range(40)]

def main():

	width, height = 800, 600

	quit : bool = False

	main_engine = Engine(width, height)

	main_engine.load_map(gmap)

	clock = pygame.time.Clock()
	fps = 60

	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("JMP")

	while not quit:

		clock.tick(fps)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				quit = True

		main_engine.render()

		main_engine.manage_action(pygame.key.get_pressed())
		main_engine.manage_movement()
		main_engine.garbage_collection()

		main_engine.redraw(screen)







if __name__ == "__main__":

	main()