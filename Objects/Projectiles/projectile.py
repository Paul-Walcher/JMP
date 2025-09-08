from interactable_object import InteractableObject
from hitbox import Hitbox

class Projectile(InteractableObject):

	def __init__(self, x, y, w, h, engine, initial_x_vel=1, initial_y_vel=1, speed=10):

		super().__init__(x, y, w, h, [Hitbox(x, y, w, h)],  engine)

		self.x_vel = initial_x_vel * speed
		self.y_vel = initial_y_vel * speed
		self.speed = speed

		self.no_friction = True