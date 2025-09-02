from enum import Enum
from Objects.Blocks.brick import Brick

class ObjectEnum(Enum):

	NONE = 0
	BRICK = 1

class Map:

	"""
	container for all items 
	"""

	obj_map = {
					ObjectEnum.BRICK: Brick,
				}


	def __init__(self, w=10, h=10, map=[[ObjectEnum.NONE for i in range(w)] for j in range(h)]):

		self.w = w
		self.h = h
		self.map = map
