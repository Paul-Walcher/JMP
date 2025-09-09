import pygame

from animation import Animation

from Objects.Projectiles.projectile import Projectile
from interactable_object import InteractableObject
from hitbox import Hitbox
from explosion import Explosion

class EvilProjectile(Projectile):

	def __init__(self, x, y, w, h, engine, initial_x_vel, initial_y_vel):

		super().__init__(x, y, w, h, engine, initial_x_vel, initial_y_vel, 15)

		self.image = pygame.image.load("Images\\simple_bullet.png")

		self.image = pygame.transform.scale(self.image, (self.w, self.h))
		self.degrees = 0
		self.angular_speed = 0.01
		self.own_gravity = 0


	def onHit(self, other: InteractableObject, direction: int) -> None:
		
		self.engine.remove_extra_object(self)
		explosion = Explosion(self.x, self.y, 3*self.w, 3*self.h, self.engine)
		self.engine.add_object(explosion)

		


	def action(self, keys) -> None:
		
		self.degrees += self.angular_speed

		if self.degrees > 360:
			self. degrees -= 360

		self.image = pygame.transform.rotate(self.image, int(self.degrees))


	def draw(self, screen) -> None:
		
		screen.blit(self.image,(self.x, self.y))