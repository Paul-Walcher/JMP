import pygame
from interactable_object import InteractableObject, Direction
from hitbox import Hitbox

from math import cos, sin

class TestPlayer(InteractableObject):

	def __init__(self, x: int, y: int, w: int, h: int, hitboxes = []):

		super().__init__(x, y, w, h, hitboxes)

		self.speed = 4.2
		self.jump_height = 7.5
		self.maxspeed = 20
		self.image = pygame.image.load("Images\\sprite_0.png")
		self.image = pygame.transform.scale(self.image, (w, h))

		self.hitboxes.append(Hitbox(x, y, w, h))
		self.jumping = False

		self.up_pressed = False

		self.circle_radius = self.w

		self.downhit_obj = None
		self.next_hit_obj = None
		self.jump_ctr = 2

		self.cw, self.ch = self.w+5, self.h+5

		self.angle = 0
		self.radius = 100
		self.angular_speed = 0.1 #per tick
		self.endpoint = (0, 0)


	def onHit(self, other: InteractableObject, direction: int) -> None:
		
		self.jump_ctr = 2


	def action(self, keys) -> None:
		
		if keys[pygame.K_LEFT] and self.x_vel > -self.maxspeed:
			self.x_vel -= self.speed
		elif keys[pygame.K_RIGHT] and self.x_vel < self.maxspeed:
			self.x_vel += self.speed

		if keys[pygame.K_SPACE] and abs(self.y_vel) < self.maxspeed and self.jump_ctr > 0:
			self.y_vel -= self.jump_height
			self.jump_ctr -= 1


		if keys[pygame.K_UP]:
			self.up_pressed = True
		else:
			self.up_pressed = False



	def draw(self, screen) -> None:
		
		screen.blit(self.image, (int(self.x), int(self.y), int(self.w), int(self.h)))

		#drawing the aim line

		
		if self.up_pressed:

			self.angle += self.angular_speed
			if self.angle > 360:
				self.angle -= 360

			self.endpoint = (int(cos(self.angle) * self.radius + self.x + self.w//2), int(sin(self.angle)*self.radius + self.y + self.h//2))

			pygame.draw.line(screen, (0xFF, 0x0, 0x0), (self.x + self.w//2, self.y + self.h//2), self.endpoint, 5)








