import pygame

from animation import Animation
from interactable_object import InteractableObject

class Explosion(InteractableObject):

	def __init__(self, x, y, w, h, engine):

		super().__init__(x, y, w, h,[], engine)

		self.image = pygame.image.load("Images\\brick.png")
		self.image = pygame.transform.scale(self.image, (self.w, self.h))

		self.explosion = Animation(self.x, self.y, self.w,self.h,
									["Images\\Explosion\\sprite_"+str(i)+".png" for i in range(3)],
									[0.5,0.5, 0.5])

		self.sound = pygame.mixer.Sound("Sounds\\explosion-42132.mp3")
		self.sound.play()


	def onHit(self, other: InteractableObject, direction: int) -> None:
		pass


	def action(self, keys) -> None:
		pass

	def draw(self, screen) -> None:
		
		screen.blit(self.image, (self.x, self.y))


	def onHit(self, other: InteractableObject, direction: int) -> None:
		pass


	def action(self, keys) -> None:
		
		if self.explosion.n_runs == 1:
			self.engine.remove_object(self)

	def draw(self, screen) -> None:
		
		self.explosion.draw(screen)