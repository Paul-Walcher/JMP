import pygame

from animation import Animation

from Objects.Projectiles.projectile import Projectile
from interactable_object import InteractableObject
from hitbox import Hitbox
from explosion import Explosion

class SimpleProjectile(Projectile):

	def __init__(self, x, y, w, h, engine, initial_x_vel, initial_y_vel):

		super().__init__(x, y, w, h, engine, initial_x_vel, initial_y_vel, 20)

		self.image = pygame.image.load("Images\\simple_bullet.png")

		self.image = pygame.transform.scale(self.image, (self.w, self.h))
		self.degrees = 0
		self.angular_speed = 0.01


	def onHit(self, other: InteractableObject, direction: int) -> None:
		
		w, h = self.w * 10, self.h * 10
		self.engine.remove_extra_object(self)
		explosion = Explosion(self.x-w//2, self.y-h//2, w, h, self.engine)
		self.engine.add_object(explosion)


	def action(self, keys) -> None:
		
		self.degrees += self.angular_speed

		if self.degrees > 360:
			self. degrees -= 360

		self.image = pygame.transform.rotate(self.image, int(self.degrees))


	def draw(self, screen) -> None:
		
		screen.blit(self.image,(self.x, self.y))