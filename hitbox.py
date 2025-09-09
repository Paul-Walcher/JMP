from __future__ import annotations


class Hitbox:

	def __init__(self, x : int, y : int, w : int, h : int):

		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def hits(self, b: Hitbox) -> bool:
		return not (self.x+self.w < b.x or self.x > b.x+b.w or self.y + self.h < b.y or self.y > b.y+b.h)


	def __str__(self):

		return "{},{},{},{}".format(self.x, self.y, self.w, self.h)

			
