from pickle import FALSE
import pygame
from pygame import Vector2
import random
from enum import Enum
from collections import namedtuple

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 25)

COLOR_WHITE = (255,255,255)
COLOR_GREEN = (0,255,0)
COLOR_RED = (255,0,0)
COLOR_BLUE = (0,0,255)
COLOR_BLACK = (0,0,0)

BLOCK_SIZE = 20
FPS = 10

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

class SnakeGame:

    def __init__(self, w = 800, h = 600):
        if (h + w) % BLOCK_SIZE != 0:
            print("Incompatible sizes")
            pygame.quit()
            quit()

        self.w = w
        self.h = h

        self.display = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        # init game state
        self.direction = Direction.RIGHT
        self.score = 0
        self.food = 0

        self.head = Vector2(w/2,h/2)
        print(self.head)
        self.snake = [
            self.head, 
            self.head - (BLOCK_SIZE,0),
            self.head - (2*BLOCK_SIZE,0)
        ]

        self._place_food()
        print(self.food)

    def _place_food(self):
        x = random.randint(0, ((self.w - BLOCK_SIZE)//BLOCK_SIZE))*BLOCK_SIZE
        y = random.randint(0, ((self.h - BLOCK_SIZE)//BLOCK_SIZE))*BLOCK_SIZE
        new_place = Vector2(x,y)
        if new_place in self.snake:
            self._place_food()
        else:
            self.food = new_place
        
    def play_step(self):
        # collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = Direction.UP
                if event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                if event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
        # move snake
        self._move(self.direction)
        self.snake.insert(0,self.head)
        # check if game over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score
        # place new food or just move
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
        # update ui and clock
        self._update_ui()
        self.clock.tick(FPS)
        # return gameover and score
        game_over = False
        return game_over, self.score
    
    def _is_collision(self):
        # hits boundary
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True
        # hits itself
        if self.head in self.snake[1:]:
            return True
        return False

    def _update_ui(self):
        self.display.fill(COLOR_BLACK)
        
        for block in self.snake:
            pygame.draw.rect(self.display, COLOR_BLUE, pygame.Rect(block.x, block.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, COLOR_GREEN, pygame.Rect(block.x+2, block.y+2, BLOCK_SIZE-4, BLOCK_SIZE-4))
        
        pygame.draw.rect(self.display, COLOR_RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        
        text = font.render("Score:" + str(self.score), True, COLOR_WHITE)
        self.display.blit(text, (0,0))

        pygame.display.update()
    
    def _move(self, direction):
        x = self.head.x
        y = self.head.y

        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        
        self.head = Vector2(x,y)

if __name__ == '__main__':
    game = SnakeGame()

    while True:
        game_over, score = game.play_step()

        if game_over:
            break
    
    print("Final score", score)
    
    pygame.quit()