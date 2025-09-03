from enum import Enum
from Objects.Blocks.brick import Brick

class ObjectEnum(Enum):

	NONE = 0
	BRICK = 1

class Map:

	"""
	container for all items 
	"""

	def __init__(self, w=10, h=10):

		self.w = w
		self.h = h
		self.map = map=[[ObjectEnum.NONE for i in range(h)] for j in range(w)]
