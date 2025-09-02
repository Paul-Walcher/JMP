import pygame
from interactable_object import InteractableObject
from hitbox import Hitbox

class TestPlayer(InteractableObject):

	def __init__(self, x: int, y: int, w: int, h: int, hitboxes = []):

		super().__init__(x, y, w, h, hitboxes)

		self.speed = 5
		self.image = pygame.image.load("Images\\sprite_0.png")
		self.image = pygame.transform.scale(self.image, (w, h))

		self.hitboxes.append(Hitbox(x, y, w, h))
		self.jumping = False


	def onHit(self, other: InteractableObject) -> None:
		pass


	def onKeys(self, keys) -> None:
		
		if keys[pygame.K_LEFT]:
			self.x_vel -= self.speed
		elif keys[pygame.K_RIGHT]:
			self.x_vel += self.speed

		if keys[pygame.K_SPACE]:
			self.y_vel -= 2

	def draw(self, screen) -> None:
		
		screen.blit(self.image, (self.x, self.y, self.w, self.h))
		for hb in self.hitboxes:
			pygame.draw.rect(screen, (0xFF, 0x0, 0x0), (hb.x, hb.y, hb.w, hb.h), 1)