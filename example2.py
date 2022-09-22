import pygame
import sys
from math import sin, cos, pi


COLOR_WHITE = (255,255,255)
COLOR_GREEN = (0,255,0)
COLOR_RED = (255,0,0)
COLOR_BLUE = (0,0,255)
COLOR_BLACK = (0,0,0)
ORIGIN = (0,0)

pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
background = pygame.Surface((800,500))
background.fill(COLOR_BLACK)



# line lenght
l1 = 100
l2 = 100
# mass of each circle
m1 = 10
m2 = 10
# angles
a1 = pi/4
a2 = pi/8
# masses position
v0 = pygame.Vector2(400,200)


while True:

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	v1 = pygame.Vector2(l1*sin(a1),l1*cos(a1)) + v0
	v2 = pygame.Vector2(l2*sin(a2),l2*cos(a2)) + v1

	# lines draw
	pygame.draw.line(screen, COLOR_GREEN, v0, v1, 2)
	pygame.draw.line(screen, COLOR_RED, v1, v2, 2)
	# masses draw
	pygame.draw.circle(screen, COLOR_GREEN, v1, m1, 0)
	pygame.draw.circle(screen, COLOR_RED, v2, m2, 0)
	# masses path draw
	pygame.draw.circle(background, COLOR_GREEN, v1, 1, 0)
	pygame.draw.circle(background, COLOR_RED, v2, 1, 0)
	
	a1 += 0.01
	a2 += 0.1
	
	pygame.display.update()
	clock.tick(30)
	screen.blit(background, ORIGIN)
	
	
