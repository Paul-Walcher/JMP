from abc import ABC, abstractmethod
from __future__ import annotations

class InteractableObject(ABC):

	def __init__(self, x: int, y: int, w: int, h: int, hitboxes = []):

		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.hitboxes = hitboxes

	@abstractmethod
	def onHit(self, other: InteractableObject) -> None:
		pass

	@abstractmethod
	def move(self, keys) -> None:
		pass

	@abstractmethod
	def draw(self, screen, blocksize) -> None:
		pass