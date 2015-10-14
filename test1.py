import pygame
import random
import sys
import math

class Point:

	def __init__(self, position):
		self.position = position
		self.old_position = position
		#self.colour = (random.randint(0, 1), random.randint(0, 1), random.randint(0, 1))
		self.colour = (2, 2, 3)

	def move(self, bias):
		self.old_position = (self.position[0], self.position[1])
		#choice = [random.random(), random.random()]
		choice = [random.randint(-1, 1), random.randint(-1, 1)]
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

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	points = []
	point_number = 1000
	for x in range(0, point_number):
		points.append(Point([400, 300]))
	average_x = Point([400, 599])
	average_x.colour = (255, 255, 255)
	x_counter = 0
	bias = [1, 0]
	counter = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		counter += 1
		if counter == 1000:
			print "Reversing"
			for point in points:
				point.colour = [-4, -4, -6]
		for point in points:
			point.move([0, 0])
			point.draw(screen)
		pygame.display.update()
