#https://es.wikipedia.org/wiki/P%C3%A9ndulo_doble

import pygame
import sys
from math import sin, cos, pi

# constants set
COLOR_WHITE = (255,255,255)
COLOR_GREEN = (0,255,0)
COLOR_RED = (255,0,0)
COLOR_BLUE = (0,0,255)
COLOR_BLACK = (0,0,0)
ORIGIN = (0,0)

# init
pygame.init()
pygame.font.init() 
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
background = pygame.Surface((800,500))
background.fill(COLOR_BLACK)

Vc = pygame.Vector2(150,250)

t = 0
wave = []
N = 3

my_font = pygame.font.SysFont('Comic Sans MS', 30)

# loop
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                N += 1
            if event.key == pygame.K_DOWN:
                N -= 1

    text = my_font.render("N="+str(N), True, COLOR_WHITE)
    screen.blit(text, (50, 50))

    #x = r*cos(t)
    #y = r*sin(t)
    
    x = 0
    y = 0
    
    for i in range(N):

        prev_x = x
        prev_y = y

        n = 2*i + 1
        r = 100 * (4/(n*pi))
        x += r  * cos(n*t)
        y += r  * sin(n*t)
    
        #wave.insert(0,y)

        v0 = pygame.Vector2(prev_x, prev_y) + Vc
        v1 = pygame.Vector2(x,y) + Vc

        pygame.draw.circle(screen, COLOR_GREEN, v0, r, width=1)
        pygame.draw.line(screen, COLOR_GREEN, v0, v1, 2)
        pygame.draw.circle(screen, COLOR_WHITE, v1, 5)

    wave.insert(0,y)
    wave_origin = pygame.Vector2(200,0) + Vc

    wave_len = len(wave)
    for i in range(wave_len):
        vp = pygame.Vector2(i,wave[i]) + wave_origin 
        pygame.draw.circle(screen, COLOR_WHITE, vp, 1)
    #print(len(wave))
    if wave_len > 400:
        wave.pop()

    v_f = pygame.Vector2(0,wave[0]) + wave_origin
    pygame.draw.line(screen, COLOR_WHITE, v1, v_f, 2)

    t += 0.05

    pygame.display.update()
    clock.tick(30)
    screen.blit(background, ORIGIN)
    
    
