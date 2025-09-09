import pygame

from animation import Animation
from interactable_object import InteractableObject
import time

class Explosion(InteractableObject):

	def __init__(self, x, y, w, h, engine):

		super().__init__(x, y, w, h,[], engine)


		self.explosion = Animation(self.x, self.y, self.w,self.h,
									["Images\\Explosion\\Explosion_blue_circle\\Explosion_blue_circle"+str(i+1)+".png" for i in range(10)],
									[0.05 for i in range(10)])
		self.explosion.play_n(1)

		self.sound = pygame.mixer.Sound("Sounds\\explosion-42132.mp3")
		#self.sound.play()
		self.own_gravity = 0




	def onHit(self, other: InteractableObject, direction: int) -> None:
		pass


	def action(self, keys) -> None:

		if self.explosion.n_runs == 1:
			self.engine.remove_object(self)

		self.explosion.run()

	def draw(self, screen) -> None:
		
		self.explosion.draw(screen)