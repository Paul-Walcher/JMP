import pygame
from interactable_object import InteractableObject
from hitbox import Hitbox

class InvisibleWall(InteractableObject):

	def __init__(self, x, y, w, h):

		super().__init__(x, y, w, h, [Hitbox(x, y, w, h)], True)


	def onHit(self, other: InteractableObject) -> None:
		pass


	def onKeys(self, keys) -> None:
		pass

	def draw(self, screen) -> None:
		
		pygame.draw.rect(screen, (0x0, 0x0, 0x0), (self.x, self.y, self.w, self.h))