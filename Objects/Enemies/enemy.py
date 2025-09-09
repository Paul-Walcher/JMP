import pygame

from interactable_object import InteractableObject

class Enemy(InteractableObject):

	def __init__(self, x, y, w, h, hitboxes, engine, player_ref=None, lives=100):

		super().__init__(x, y, w, h, hitboxes, engine)

		self.lives = lives
		self.player_ref = player_ref