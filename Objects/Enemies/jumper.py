import pygame

import time
import random

from interactable_object import Direction
from hitbox import Hitbox
from Objects.Enemies.enemy import Enemy
from Objects.Blocks.block import Block

from Objects.Projectiles.evil_projectile import EvilProjectile

class Jumper(Enemy):

	def __init__(self, x, y, w, h, engine, player_ref=None, lives=100):

		super().__init__(x, y, w, h, [Hitbox(x+w//10, y, w-w//5, h)], engine, player_ref, lives)


		self.image_left = pygame.image.load("Images\\eye_left.png")

		self.image_right = pygame.image.load("Images\\eye_right.png")
		self.image_left = pygame.transform.scale(self.image_left, (self.w, self.h))
		self.image_right = pygame.transform.scale(self.image_right, (self.w, self.h))

		self.jump_height = 10
		self.hit_ground = False
		self.shoot_times = (0.5, 1.5)

		self.last_check = time.perf_counter()
		self.shoot_time = random.uniform(*self.shoot_times)

	def onHit(self, other, direction: int) -> None:
		

		if direction == Direction.DOWN:

			self.hit_ground = True


	def action(self, keys) -> None:
		
		if self.hit_ground:
			self.hit_ground = False
			self.y_vel -= self.jump_height

		T = time.perf_counter()
		
		if T-self.last_check > self.shoot_time:

			self.last_check = time.perf_counter()
			self.shoot_time = random.uniform(*self.shoot_times)

			midpoint = (self.x + self.w//2, self.y+self.h//2)
			x_dir = self.player_ref.x - midpoint[0]
			y_dir = self.player_ref.y - midpoint[1]

			x_dir /= (x_dir + y_dir)
			y_dir /= (x_dir + y_dir)

			proj = EvilProjectile(midpoint[0], midpoint[1], 10, 10, self.engine, -x_dir, -y_dir)
			self.engine.add_extra_object(proj)


		if self.lives <= 0:
			self.engine.remove_extra_object(self)




	def draw(self, screen) -> None:
		
		blit_image = (self.image_left if self.player_ref.x < self.x else self.image_right)

		screen.blit(blit_image, (self.x, self.y))