import pygame
import random
import sys
import math
import time

class Point:

	def __init__(self, position):
		self.position = position
		self.old_position = position
		self.used_positions = [position]
		#self.colour = (random.randint(0, 1), random.randint(0, 1), random.randint(0, 1))
		self.colour = (255, 255, 255)

	def move(self, screen_array):
		self.old_position = (self.position[0], self.position[1])
		#choice = [random.random(), random.random()]
		stuck = True
		if screen_array[self.position[0] + 1][self.position[1] + 1][0] == 128:
			stuck = False
		if stuck and screen_array [self.position[0] + 1][self.position[1] - 1][0] == 128:
			stuck = False
		if stuck and screen_array [self.position[0] - 1][self.position[1] + 1][0] == 128:
			stuck = False
		if stuck and screen_array [self.position[0] - 1][self.position[1] - 1][0] == 128:
			stuck = False
		if stuck and screen_array [self.position[0]][self.position[1] - 1][0] == 128:
			stuck =  False
		if stuck and screen_array [self.position[0]][self.position[1] + 1][0] == 128:
			suck = False
		if stuck and screen_array [self.position[0] + 1][self.position[1]][0] == 128:
			stuck = False
		if stuck and screen_array [self.position[0] - 1][self.position[1]][0] == 128:
			stuck = False
		if stuck:
			print 'Stuck'
			return True
		while True:
			#choice = [random.randint(-1, 1), random.randint(-1, 1)]
			choice1 = random.randint(0, 1)
			choice2 = random.randint(0, 1)
			choice2 *= 2
			choice2 -= 1
			#if screen_array[self.position[0] + choice[0]][self.position[1] + choice[1]][0] == 128:
			test_position = [self.position[0], self.position[1]]
			test_position[choice1] += choice2
			if test_position[0] < len(screen_array) and test_position[1] < len(screen_array[test_position[0]]):
				if screen_array[test_position[0]][test_position[1]][0] == 128:
					self.position = [test_position[0], test_position[1]]
					return False

	def teleport(self, new_position):
		self.position = new_position
		self.old_position = new_position

	def draw(self, screen_array):
		#pygame.draw.line(screen, self.colour, self.old_position, self.position)
		#pygame.draw.line(screen, (255, 0, 0), self.position, self.position)
		screen_array[self.old_position[0]][self.old_position[1]][0] = 255
		screen_array[self.old_position[0]][self.old_position[1]][1] = 255
		screen_array[self.old_position[0]][self.old_position[1]][2] = 255

		screen_array[self.position[0]][self.position[1]][0] = 255
		screen_array[self.position[0]][self.position[1]][1] = 0
		screen_array[self.position[0]][self.position[1]][2] = 0

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	screen.fill((128, 128, 128))
	screen_array = pygame.surfarray.pixels3d(screen)
	points = []
	point_number = 1
	stuck = False
	for x in range(0, point_number):
		points.append(Point([400, 300]))
	while True:
		time.sleep(0.001)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		for point in points:
			stuck = point.move(screen_array)
			if stuck:
				point.teleport([random.randint(100, 400), random.randint(100, 400)])
				stuck= False
			else:
				point.draw(screen_array)
		pygame.display.update()
	while True:
		time.sleep(0.1)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		pygame.display.update()
