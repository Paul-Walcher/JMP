from __future__ import annotations

from abc import ABC, abstractmethod

class Direction:

	LEFT = -1
	RIGHT = 0
	UP = 1
	DOWN = 2

class InteractableObject(ABC):

	def __init__(self, x: int, y: int, w: int, h: int, hitboxes, engine, static_object = False, solid=True, own_gravity=-1):

		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.engine = engine
		self.x_vel = 0
		self.y_vel = 0
		self.hitboxes = hitboxes
		self.static_object = static_object
		self.solid = solid #if the player can go through
		self.no_friction = False
		self.own_gravity = own_gravity

	@abstractmethod
	def onHit(self, other: InteractableObject, direction: int) -> None:
		pass

	@abstractmethod
	def action(self, keys) -> None:
		pass

	@abstractmethod
	def draw(self, screen) -> None:
		pass

	def hits(self, other):

		for h1 in self.hitboxes:
			for h2 in other.hitboxes:

				if h1.hits(h2):
					return (h1, h2)
		return None

	def move_absolute(self):

		self.x += int(self.x_vel)
		self.y += int(self.y_vel)

		for hitbox in self.hitboxes:

			hitbox.x += int(self.x_vel)
			hitbox.y += int(self.y_vel)

	def set_position(self, x, y, w, h):

		diff = (x - self.x, y-self.y, w-self.w, h - self.h)
		self.x = x
		self.y = y
		self.w = w
		self.h = h

		for hitbox in self.hitboxes:

			hitbox.x, hitbox.y, hitbox.w, hitbox.h = hitbox.x + diff[0], hitbox.y+diff[1], hitbox.w + diff[2], hitbox.h + diff[3]
