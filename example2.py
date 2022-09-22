import pygame
import sys
from math import sin, cos, pi


pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
background = pygame.Surface((800,500))

COLOR_WHITE = (255,255,255)

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
v1 = pygame.Vector2(l1*sin(a1),l1*cos(a1)) + v0
v2 = pygame.Vector2(l2*sin(a2),l2*cos(a2)) + v1
# lines draw
line1 = pygame.draw.line(background, COLOR_WHITE, v0, v1, 2)
line2 = pygame.draw.line(background, COLOR_WHITE, v1, v2, 2)
# masses draw
mass1 = pygame.draw.circle(background, COLOR_WHITE, v1, m1, 0)
mass2 = pygame.draw.circle(background, COLOR_WHITE, v2, m2, 0)

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	a1 += 0.01
	
	print(v1,v2)
	v1.update(a1,a1)
	line1.update()
	
	screen.blit(background, (0,0))
	pygame.display.update()
	clock.tick(1)
