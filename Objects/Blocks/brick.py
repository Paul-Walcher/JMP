import pygame

from interactable_object import InteractableObject
from Objects.Blocks.block import Block
from hitbox import Hitbox


class Brick(Block):

	def __init__(self, x, y, w, h):

		super().__init__(x, y, w, h, 0.5, 4, False)

		self.image = pygame.image.load("Images\\brick.png")
		self.image = pygame.transform.scale(self.image, (self.w, self.h))


	def onHit(self, other: InteractableObject, direction: int) -> None:
		pass


	def action(self, keys) -> None:
		pass

	def draw(self, screen) -> None:
		
		screen.blit(self.image, (self.x, self.y))