from interactable_object import InteractableObject
from hitbox import Hitbox

class Block(InteractableObject):

	def __init__(self, x, y, w, h, bounce=0, friction=4, breakable=False):

		super().__init__(x, y, w, h, [Hitbox(x, y, w, h)],  static_object=True)

		self.bounce = bounce
		self.friction = friction
		self.breakable = breakable