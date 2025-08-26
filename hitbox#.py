from __future__ import annotations


class Hitbox_t:

	SQUARE = 0
	CIRCLE = 1 

class Hitbox:

	def __init__(self, x : int, y : int, w : int, h : int, t : int):

		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.t = t

	@staticmethod
	def hits(a: Hitbox, b: Hitbox) -> bool:

		if a.t == Hitbox_t.SQUARE and b.t == Hitbox_t.SQUARE:

			return not (a.x+a.w < b.x or a.x > b.x+b.w or a.y + a.h < b.y or a.y > b.y+b.h)

		elif a.t == Hitbox_t.SQUARE and b.t == Hitbox_t.CIRCLE:

			
