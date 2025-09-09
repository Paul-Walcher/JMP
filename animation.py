from interactable_object import InteractableObject
from time import perf_counter
import pygame

class Animation:

	def __init__(self, x: int, y: int, w: int, h: int,
		images: list[str], animation_speed: list[float], loop: bool = True):

		self.x, self.y, self.w, self.h = x, y, w, h

		self.images = [pygame.image.load(image) for image in images]
		self.images = [pygame.transform.scale(image, (w, h)) for image in self.images]
		self.animation_speed = animation_speed
		self.loop = loop
		self.visible = True
		self.paused = False

		self.image_index: int = 0
		self.last_count: float = perf_counter()
		self.revolutions = 0

		self.n_runs = 0

	def pause(self):
		self.paused = True

	def _continue(self):
		self.paused = False
		self.last_count = perf_counter()

	def hide(self):
		self.visible = False

	def show(self):
		self.visible = True

	def reset(self):
		self.image_index = 0
		self.last_count = perf_counter()


	def play_n(self, x):

		self.revolutions = x
		self.n_runs = 0
		self._continue()


	def run(self):

		if self.n_runs >= self.revolutions:

			return

		if self.paused:
			return

		time_passed = perf_counter() - self.last_count

		if time_passed >= self.animation_speed[self.image_index]:

			self.image_index += 1

			if self.image_index >= len(self.images):
				print(self.image_index, len(self.images))
				self.image_index = 0
				self.n_runs += 1
				
				if self.n_runs >= self.revolutions and self.revolutions != -1:
					self.pause()

			self.last_count = perf_counter()

	
	def draw(self, screen):

		#now drawing
		if self.visible:
			screen.blit(self.images[self.image_index], 
				(self.x, self.y, self.w, self.h))



