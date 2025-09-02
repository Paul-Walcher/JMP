import pygame

from interactable_object import InteractableObject
from hitbox import Hitbox


class Brick(InteractableObject):

	def __init__(self, x, y, w, h):

		super().__init__(x, y, w, h, [Hitbox(x, y, w, h)], True)

		self.image = pygame.image.load("Images\\brick.png")
		self.image = pygame.transform.scale(self.image, (self.w, self.h))


	def onHit(self, other: InteractableObject) -> None:
		pass


	def onKeys(self, keys) -> None:
		pass

	def draw(self, screen) -> None:
		
		screen.blit(self.image, (self.x, self.y))