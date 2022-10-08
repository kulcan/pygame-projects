#https://es.wikipedia.org/wiki/P%C3%A9ndulo_doble

import pygame
import sys
from math import sin, cos, pi, pow

# constants set
COLOR_WHITE = (255,255,255)
COLOR_GREEN = (0,255,0)
COLOR_RED = (255,0,0)
COLOR_BLUE = (0,0,255)
COLOR_BLACK = (0,0,0)
ORIGIN = (0,0)
G = 1

# init
pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
background = pygame.Surface((800,500))
background.fill(COLOR_BLACK)

# line lenght
l1 = 100
l2 = 100
# masses
m1 = 10
m2 = 10
# angles
a1 = pi/2
a2 = pi/2
# velocity
a1_v = 0
a2_v = 0
# origin vector
v0 = pygame.Vector2(400,250)

# loop
while True:

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	num_1 = -G*(2*m1+m2)*sin(a1) - m2*G*sin(a1-2*a2) - 2*sin(a1-a2)*m2*((a2_v**2)*l2 + (a1_v**2)*l1*cos(a1-a2))
	num_2 = 2*sin(a1-a2)*((a1_v**2)*l1*(m1+m2) + G*(m1+m2)*cos(a1) + (a2_v**2)*l2*m2*cos(a1-a2))
	deno = (2*m1 + m2 - m2*cos(2*a1-2*a2))
	# acceleration
	a1_a = num_1/(l1*deno)
	a2_a = num_2/(l2*deno)
	# velocity
	a1_v += a1_a
	a2_v += a2_a
	# angle
	a1 += a1_v
	a2 += a2_v

	#a1_v *= 0.9
	#a2_v *= 0.9

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
	
	pygame.display.update()
	clock.tick(60)
	screen.blit(background, ORIGIN)
	
	
