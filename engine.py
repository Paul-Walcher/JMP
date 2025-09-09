import pygame 
from hitbox import Hitbox
from animation import Animation
from test_player import TestPlayer
from invisible_wall import InvisibleWall
from interactable_object import InteractableObject, Direction

from Objects.Blocks.block import Block
from Objects.Blocks.brick import Brick

from Objects.Enemies.jumper import Jumper

from map import *

class Engine:

	def __init__(self, width, height):
		

		self.width = width
		self.height = height
		self.objects = []
		self.screen_objects = []


		self.blocksize = 50

		self.x_margin = 50
		self.y_margin = 50

		self.scrollx = 0
		self.scrolly = 0

		self.x_margin = 100
		self.y_margin = 100

		self.wall_left = InvisibleWall(0, 0, self.x_margin, self.height)
		self.wall_right = InvisibleWall(self.width-self.x_margin, 0, self.x_margin, self.height)
		self.wall_top = InvisibleWall(0, 0, self.width, self.y_margin)
		self.wall_bottom = InvisibleWall(0, self.height-self.y_margin, self.width, self.y_margin)

		self.screen_wall = InvisibleWall(0,0, self.width, self.height)

		self.test_player = TestPlayer(100, 100, 50, 50, [], self)

		self.objects.append(self.test_player)

		self.render_extra = []

		self.j1 = Jumper(200, 100, 200, 200, self, self.test_player)

		self.objects.append(self.j1)

		self.scrollx = 0
		self.scrolly = 0

	def load_map(self, MAP):
		"""
		loads the map for the jump and run level.
		"""

		self.map = MAP

		for y in range(MAP.h):
			for x in range(MAP.w):

				if MAP.map[y][x] == ObjectEnum.BRICK:

					brick = Brick(x * self.blocksize, y * self.blocksize, self.blocksize, self.blocksize, self)
					self.add_extra_object(brick)

	def render(self):

		#loads all visible objects into view
		self.screen_objects = []

		for obj in self.objects:

			hb = Hitbox(obj.x,obj.y,obj.w,obj.h)
			if hb.hits(self.screen_wall):

				self.screen_objects.append(obj)

		self.screen_objects.extend(self.render_extra)

	def garbage_collection(self):

		"""
		removes the objects that fly past the top, bottom,left and right walls
		"""

		outside = lambda obj: obj.x+obj.w < -self.scrollx or obj.x > self.map.w * self.blocksize - self.scrollx \
								or obj.y+obj.h < -self.scrolly or obj.y > self.map.h * self.blocksize - self.scrolly

		to_remove = []
		for i in range(len(self.objects)):

			if outside(self.objects[i]):
				to_remove.append(i)
		for i in to_remove:
			self.objects.pop(i)

		to_remove = []
		for i in range(len(self.render_extra)):

			test = lambda obj: obj.y+obj.h < -self.scrolly or obj.y > self.map.h * self.blocksize - self.scrolly


			if outside(self.render_extra[i]):
				to_remove.append(i)

		for i in to_remove:
			self.render_extra.pop(i)


				

	def manage_action(self, keys):

		for obj in self.screen_objects:
			obj.action(keys)


	def manage_movement(self):
		"""
		this method manages the movement of all 
		"""


		#calculate the velocities
		gravity = 0.5
		max_fallspeed = 10
		standard_friction = 2
		friction = 4


		#tracing the collision
		trace_steps = 10

		frictions = {}

		for obj in self.screen_objects:


			if obj.static_object:
				continue

			x_vels = obj.x_vel / trace_steps
			y_vels = obj.y_vel / trace_steps



			for i in range(1, trace_steps+1):

				x, y = int(obj.x + x_vels), int(obj.y + y_vels)

				y_hit_object = None
				x_hit_object = None

				x_hit: bool = False
				y_hit: bool = False

				x_hitboxes = None
				y_hitboxes = None

				direction = None

				#checking for collision on the y axis
				if not y_hit:
					for obj2 in self.screen_objects:

						if y_hit:
							break

						if obj is obj2:
							continue

						for h1 in obj.hitboxes:
							if y_hit:
								break
							h1_org = h1
							h1 = Hitbox(h1.x, int(h1.y+ i * y_vels), h1.w, h1.h)

							for h2 in obj2.hitboxes:

								if y_hit:
									break



								if (h1_org.y + h1_org.h <= h2.y and h1.y + h1.h >= h2.y and not ((h1.x >= h2.x + h2.w) or (h1.x + h1.w <= h2.x))\
								 or (h1_org.y >= h2.y + h2.h and h1.y  <= h2.y + h2.h) and not ((h1.x >= h2.x + h2.w) or (h1.x + h1.w <= h2.x))):
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

								if (h1_org.x + h1_org.w < h2.x and h1.x + h1.w >= h2.x and not ((h1.y >= h2.y + h2.h) or (h1.y + h1.h <= h2.y)))\
								 or (h1_org.x > h2.x + h2.w and h1.x  <= h2.x + h2.w) and not ((h1.y >= h2.y + h2.h) or (h1.y + h1.h <= h2.y)):
									x_hitboxes = (h1, h2, i)
									x_hit_object = obj2
									x_hit = True



			

			#if there was a hit, set the velocity to 0, then adjust the position
			if x_hit:


				right = obj.x_vel > 0
				left = obj.x_vel < 0
				x_vl_prev = obj.x_vel
				obj.x_vel = 0

				if right:

					x = x_hit_object.x - obj.w-5
					obj.set_position(x, obj.y, obj.w, obj.h)
					obj.onHit(x_hit_object, Direction.RIGHT)



				elif left:
					x = x_hit_object.x + x_hit_object.w + 5
					obj.set_position(x, obj.y, obj.w, obj.h)
					obj.onHit(x_hit_object, Direction.LEFT)


			if y_hit:


				down = obj.y_vel > 0 and abs(obj.y_vel) > gravity
				up = obj.y_vel < 0 and abs(obj.y_vel) > gravity

				if obj is self.j1 and y_hit_object is self.test_player:
					print(obj.y_vel)

				y_vel_prev = obj.y_vel
				obj.y_vel = 0

				if down:

					y = y_hit_object.y - obj.h
					obj.set_position(obj.x, y, obj.w, obj.h)

					obj.onHit(y_hit_object, Direction.DOWN)


					if isinstance(obj2, Block):

						obj.y_vel = int(-obj2.bounce * y_vel_prev)
						frictions[obj] = obj2.friction



				elif up:


					y = y_hit_object.y + y_hit_object.h
					obj.set_position(obj.x, y, obj.w, obj.h)
					obj.onHit(y_hit_object, Direction.UP)


		left_hit = False
		right_hit = False
		top_hit = False
		bottom_hit = False

		if self.test_player.hits(self.wall_left) and self.test_player.x_vel < 0:

			for obj in self.objects:
				obj.set_position(obj.x - self.test_player.x_vel, obj.y, obj.w, obj.h)
			for obj in self.render_extra:
				obj.set_position(obj.x - self.test_player.x_vel, obj.y, obj.w, obj.h)


			left_hit = True
			self.scrollx += self.test_player.x_vel


		if self.test_player.hits(self.wall_right) and self.test_player.x_vel > 0:

			for obj in self.objects:
				obj.set_position(obj.x - self.test_player.x_vel, obj.y, obj.w, obj.h)
			for obj in self.render_extra:
				obj.set_position(obj.x - self.test_player.x_vel, obj.y, obj.w, obj.h)

			right_hit = True

			self.scrollx += self.test_player.x_vel



		if self.test_player.hits(self.wall_top) and self.test_player.y_vel < 0:

			for obj in self.objects:
				obj.set_position(obj.x, obj.y- self.test_player.y_vel, obj.w, obj.h)
			for obj in self.render_extra:
				obj.set_position(obj.x, obj.y- self.test_player.y_vel, obj.w, obj.h)

			top_hit = True

			self.scrolly += self.test_player.y_vel


		if self.test_player.hits(self.wall_bottom) and self.test_player.y_vel > 0:

			for obj in self.objects:
				obj.set_position(obj.x, obj.y - self.test_player.y_vel, obj.w, obj.h)
			for obj in self.render_extra:
				obj.set_position(obj.x, obj.y- self.test_player.y_vel, obj.w, obj.h)

			bottom_hit = True

			self.scrolly += self.test_player.y_vel



		for obj in self.screen_objects:
			obj.move_absolute()


		for obj in self.screen_objects:
			if not obj.static_object and obj.y_vel < max_fallspeed:
				obj.y_vel += gravity

		#applying friction

		for obj in self.screen_objects:


			sf = (friction if obj not in frictions else frictions[obj])

			if obj not in frictions and obj.no_friction:
				continue

			if obj.x_vel < 0:

				obj.x_vel += min(sf, abs(obj.x_vel))

			elif obj.x_vel > 0:

				obj.x_vel -= min(sf, abs(obj.x_vel))
			

		if left_hit:
		 	self.test_player.set_position(self.x_margin, self.test_player.y, self.test_player.w, self.test_player.h)
		if right_hit:
		 	self.test_player.set_position(self.width - self.x_margin - self.test_player.w, self.test_player.y, self.test_player.w, self.test_player.h)
		if top_hit:
		 	self.test_player.set_position(self.test_player.x, self.y_margin, self.test_player.w, self.test_player.h)
		if bottom_hit:
			self.test_player.set_position(self.test_player.x, self.height - self.y_margin - self.test_player.h, self.test_player.w, self.test_player.h)



	def redraw(self, screen):

		screen.fill((0xFF, 0xFF, 0xFF))
		
		for obj in self.screen_objects:
			obj.draw(screen)

		pygame.display.flip()

	def add_object(self, obj):
		self.objects.append(obj)

	def add_extra_object(self, obj):
		self.render_extra.append(obj)

	def remove_extra_object(self, obj):
		self.render_extra.remove(obj)

	def remove_object(self, obj):
		self.objects.remove(obj)
		