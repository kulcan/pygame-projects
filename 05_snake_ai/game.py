import pygame
from pygame import Vector2
import random
from enum import Enum
import numpy as np

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 25)

COLOR_WHITE = (255,255,255)
COLOR_GREEN = (0,255,0)
COLOR_RED = (255,0,0)
COLOR_BLUE = (0,0,255)
COLOR_BLACK = (0,0,0)

BLOCK_SIZE = 20
FPS = 100

# reset

# reward

# play(action) -> direction

# game iteration

# is_collition

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

class SnakeGameAI:

    def __init__(self, w = 800, h = 600):
        if (h + w) % BLOCK_SIZE != 0:
            print("Incompatible sizes")
            pygame.quit()
            quit()

        self.w = w
        self.h = h

        self.display = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Snake AI")
        self.clock = pygame.time.Clock()

        # init game state
        self.reset()
    
    def reset(self):
        self.direction = Direction.RIGHT
        self.score = 0
        self.food = 0
        self.head = Vector2(self.w/2,self.h/2)
        self.snake = [
            self.head, 
            self.head - (BLOCK_SIZE,0),
            self.head - (2*BLOCK_SIZE,0)
        ]
        self._place_food()
        self.frame_iteration = 0

    def _place_food(self):
        x = random.randint(0, ((self.w - BLOCK_SIZE)//BLOCK_SIZE))*BLOCK_SIZE
        y = random.randint(0, ((self.h - BLOCK_SIZE)//BLOCK_SIZE))*BLOCK_SIZE
        new_place = Vector2(x,y)
        if new_place in self.snake:
            self._place_food()
        else:
            self.food = new_place
        
    def play_step(self, action):
        self.frame_iteration += 1
        # collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # removed key input
        # move snake
        self._move(action)
        self.snake.insert(0,self.head)
        # check if game over and reward conditions
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            reward = -10
            game_over = True
            return reward, game_over, self.score
        # place new food and update reward or just move
        if self.head == self.food:
            reward = 10
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
        # update ui and clock
        self._update_ui()
        self.clock.tick(FPS)
        # return gameover and score
        game_over = False
        return reward, game_over, self.score
    
    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # hits boundary
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        # hits itself
        if pt in self.snake[1:]:
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
    
    def _move(self, action):
        # [straig, right, left]
        clock_wise = [
            Direction.RIGHT, 
            Direction.DOWN,
            Direction.LEFT,
            Direction.UP
        ]
        # obtain index in array by current direction
        idx = clock_wise.index(self.direction)
            
        if np.array_equal(action, [0,1,0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx] # right turn r -> d -> l -> u
        elif np.array_equal(action, [0,0,1]):
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx] # left turn r -> u -> l -> d
        else: #[1,0,0]
            new_dir = clock_wise[idx] # no change
        
        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        
        self.head = Vector2(x,y)