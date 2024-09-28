 import sys
import pygame
from pygame.locals import *
#Kolory
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


# Kształty tetrisa
SHAPES = [
    [[1, 1, 1, 1]], # I
    [[1, 1], [1, 1]], # O
    [[0, 1, 0], [1, 1, 1]], # T
    [[1, 1, 0], [0, 1, 1]], # S
    [[0, 1, 1], [1, 1, 0]], # Z
    [[1, 1, 1], [1, 0, 0]], # L
    [[1, 1, 1], [0, 0, 1]]  # J
]
BLOCK_SIZE = 50
FallSpeed = 5
pygame.init()

#w 1080
#h 2270
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

surface = pygame.display.set_mode((screen_height, screen_width))
surfrect = surface.get_rect()

scr_width = surfrect.width - 400 
scr_height = surfrect.height // 2
scr = pygame.Rect(screen_width /2, 0, scr_width, scr_height)
#scr.midtop = ()




brick = pygame.Rect((scr.w/2, 0), (50 ,50))


clock = pygame.time.Clock()

touched = False
c = BLUE

# Funkcja rysowania klocka
def draw_shape(surface, shape, offset):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(surface, BLUE, 
                                 (offset[0] + x * BLOCK_SIZE, offset[1] + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
def game():
    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()
                
        surface.fill(BLACK)
        pygame.draw.rect(surface, GREEN, scr) 
        
        
        pygame.draw.rect(surface,BLUE,brick)
   
        pygame.display.flip()
   
        clock.tick(60)   
                
game()
pygame.quit                
                import sys
import pygame
from pygame.locals import *
#Kolory
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


# Kształty tetrisa
SHAPES = [
    [[1, 1, 1, 1]], # I
    [[1, 1], [1, 1]], # O
    [[0, 1, 0], [1, 1, 1]], # T
    [[1, 1, 0], [0, 1, 1]], # S
    [[0, 1, 1], [1, 1, 0]], # Z
    [[1, 1, 1], [1, 0, 0]], # L
    [[1, 1, 1], [0, 0, 1]]  # J
]
BLOCK_SIZE = 50
FallSpeed = 5
pygame.init()

#w 1080
#h 2270
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

surface = pygame.display.set_mode((screen_height, screen_width))
surfrect = surface.get_rect()

scr_width = surfrect.width - 400 
scr_height = surfrect.height // 2
scr = pygame.Rect(screen_width /2, 0, scr_width, scr_height)
#scr.midtop = ()




brick = pygame.Rect((scr.w/2, 0), (50 ,50))


clock = pygame.time.Clock()

touched = False
c = BLUE

# Funkcja rysowania klocka
def draw_shape(surface, shape, offset):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(surface, BLUE, 
                                 (offset[0] + x * BLOCK_SIZE, offset[1] + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
def game():
    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()
                
        surface.fill(BLACK)
        pygame.draw.rect(surface, GREEN, scr) 
        
        
        pygame.draw.rect(surface,BLUE,brick)
   
        pygame.display.flip()
   
        clock.tick(60)   
                
game()
pygame.quit                
                 