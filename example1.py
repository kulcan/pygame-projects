import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
background = pygame.Surface((400,300))

surface = pygame.Surface((10,10))
surface.fill((0,255,0))

pos = [175, 125]

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				pos[0] += 10
			if event.key == pygame.K_LEFT:
				pos[0] -= 10
			if event.key == pygame.K_UP:
				pos[1] -= 10
			if event.key == pygame.K_DOWN:
				pos[1] += 10
	screen.blit(background, (0,0))
	screen.blit(surface,pos)
	pygame.display.update()

