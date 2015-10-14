import sys
import time
import multiprocessing

try:
	import pygame
except:
	print """This program needs PyGame installed. In Debian and Ubuntu,
this is in the package "python-pygame"."""
	sys.exit()
import random
import math

class Point:

	def __init__(self, position, colour, shift):
		self.position = position
		self.old_position = position
		self.shift = shift
		## Set the desired colour here, stored as values for red, green and blue
		## between 0 (none) and 255 (full). A function can also be used, the example
		## given choosing a random integer from 0 to 32 for each

		#self.colour = (random.randint(0, 32), random.randint(0, 32), random.randint(0, 32))
		self.colour = colour

	def move(self):
		self.old_position = (self.position[0], self.position[1])

		## The values in this line determine the size and resolution of
		## the pattern with small values meaning smaller. Giving uneven
		## values can make the pattern stretch and drift.
		choice = [random.randint(self.shift[0], self.shift[1]), random.randint(self.shift[2], self.shift[3])]

		self.position[0] += choice[0]
		self.position[1] += choice[1]

	def draw(self, screen):
		if 0 <= self.position[0] < screen.get_width() and 0 <= self.position[1] < screen.get_height() \
		and 0 <= self.old_position[0] < screen.get_width and 0 <= self.old_position[1] < screen.get_height():
			colour = [self.colour[0] + screen.get_at((self.position))[0], self.colour[1] + screen.get_at((self.position))[1], self.colour[2] + screen.get_at((self.position))[2]]

			if colour[0] > 255:
				colour[0] = 255
			elif colour[0] < 0:
				colour[0] = 0
			if colour[1] > 255:
				colour[1] = 255
			elif colour[1] < 0:
				colour[1] = 0
			if colour[2] > 255:
				colour[2] = 255
			elif colour[2] < 0:
				colour[2] = 0
			pygame.draw.aaline(screen, colour, self.old_position, self.position, 1)

class Pattern:

	def __init__(self, position, density, shift, colour):
		self.colour = colour
		self.position = position
		self.shift = shift
		self.points = []
		for x in range(0, density):
			self.points.append(Point([position[0], position[1]], colour, shift))
			#self.points.append(Point([position[0], position[1]], [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)], shift))

	def move(self):
		for point in self.points:
			point.move()

	def draw(self, screen):
		for point in self.points:
			point.draw(screen)

class PatternProcess(multiprocessing.Process):

	def __init__(self, pattern, queue):
		super(PatternProcess, self).__init__()
		self.pattern = pattern
		self.queue = queue

	def run(self):
		while True:
			self.pattern.move()
			self.queue.put(self.pattern)

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((800, 600))

	processes = []
	for number in range(1, random.randint(2, 6)):
		size = random.randint(1, 3)
		queue = multiprocessing.Queue()
		processes.append((PatternProcess(Pattern([random.randint(100, 700), random.randint(100, 500)], 500, [-1 * size, size, -1 * size, size], [random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)]), queue), queue))

	for process in processes:
		process[0].start()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#time.sleep(1.0/12.0)
		for queue in processes:
			if not queue[1].empty():
				queue[1].get().draw(screen)
		pygame.display.update()
