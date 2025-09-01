import pygame 
from hitbox import Hitbox
from animation import Animation
from test_player import TestPlayer
from invisible_wall import InvisibleWall
from interactable_object import InteractableObject

class Engine:

	def __init__(self, width, height):
		

		self.width = width
		self.height = height
		self.screen_objects = []
		self.test_ground = InvisibleWall(
											0, height-100, width-100, 100,
											)
		self.test_ground_2 = InvisibleWall(0, height-300, width-200, 100)
		self.test_ground_3 = InvisibleWall(0, 200, 20, 100)

		self.test_player = TestPlayer(100, 100, 50, 50)
		self.screen_objects.append(self.test_ground)
		self.screen_objects.append(self.test_ground_2)
		self.screen_objects.append(self.test_ground_3)
		self.screen_objects.append(self.test_player)



	def manage_keys(self, keys):

		for obj in self.screen_objects:
			obj.onKeys(keys)

	def manage_movement(self):
		"""
		this method manages the movement of all 
		"""

		#calculate the velocities
		gravity = 0.5
		friction = 4

		for obj in self.screen_objects:
			if not obj.static_object:
				obj.y_vel += gravity

		#applying friction

		for obj in self.screen_objects:
			
			if obj.x_vel < 0:

				obj.x_vel += min(friction, abs(obj.x_vel))

			elif obj.x_vel > 0:

				obj.x_vel -= min(friction, abs(obj.x_vel))

		#tracing the collision
		trace_steps = 10
		x_hit: bool = False
		y_hit: bool = False

		for obj in self.screen_objects:


			x_hitboxes = None
			y_hitboxes = None

			if obj.static_object:
				continue

			x_vels = obj.x_vel / trace_steps
			y_vels = obj.y_vel / trace_steps



			for i in range(1, trace_steps+1):

				if y_hit and x_hit:
					break

				x, y = int(obj.x + x_vels), int(obj.y + y_vels)

				y_hit_object = None

				#checking for collision on the y axis
				if not y_hit:
					for obj2 in self.screen_objects:

						if y_hit:
							break

						if obj is obj2 or not obj2.solid:
							continue

						for h1 in obj.hitboxes:
							if y_hit:
								break
							h1_org = h1
							h1 = Hitbox(h1.x, int(h1.y+ i * y_vels), h1.w, h1.h)

							for h2 in obj2.hitboxes:

								if y_hit:
									break

								if h1.hits(h2):
									y_hitboxes = (h1, h2, i)
									y_hit_object = obj2
									y_hit = True

				#checking for collision on the x axis
				if not x_hit:
					for obj2 in self.screen_objects:

						if x_hit:
							break

						if obj is obj2 or not obj2.solid:
							continue

						for h1 in obj.hitboxes:
							if x_hit:
								break

							h1_org = h1
							h1 = Hitbox(int(h1.x+ i * x_vels), h1.y, h1.w, h1.h)

							for h2 in obj2.hitboxes:

								if x_hit:
									break

								if (h1_org.x + h1_org.w < h2.x and h1.x + h1.w >= h2.x and not ((h1.y > h2.y + h2.h) or (h1.y + h1.h < h2.y)))\
								 or (h1_org.x > h2.x + h2.w and h1.x  <= h2.x + h2.w) and not ((h1.y > h2.y + h2.h) or (h1.y + h1.h < h2.y)):
									print(True)
									x_hitboxes = (h1, h2, i)
									x_hit = True

			#TODO: sort hitboxes by left, right, up down

			#if there was a hit, set the velocity to 0, then adjust the position


			if x_hit:

				right = obj.x_vel > 0
				obj.x_vel = 0

				if right:

					x = obj.x - (x_hitboxes[0].x + x_hitboxes[0].w - x_hitboxes[1].x) + x_hitboxes[0].x - obj.x
					obj.set_position(x, obj.y, obj.w, obj.h)


				else:
					x = obj.x + (x_hitboxes[1].x + x_hitboxes[1].w - x_hitboxes[0].x) - x_hitboxes[0].x + obj.x
					obj.set_position(x, obj.y, obj.w, obj.h)
					print(x)


			if y_hit:

				down = obj.y_vel > 0

				obj.y_vel = 0

				if down:

					y = obj.y - (y_hitboxes[0].y + y_hitboxes[0].h - y_hitboxes[1].y) + y_hitboxes[0].y - obj.y
					obj.set_position(obj.x, y, obj.w, obj.h)

				else:

					y = obj.y + (y_hitboxes[1].y + y_hitboxes[1].h - y_hitboxes[0].y) - y_hitboxes[0].y + obj.y
					obj.set_position(obj.x, y, obj.w, obj.h)















		for obj in self.screen_objects:
			obj.move_absolute()


	def redraw(self, screen):

		screen.fill((0xFF, 0xFF, 0xFF))
		
		for obj in self.screen_objects:
			obj.draw(screen)

		pygame.display.flip()
		