import numpy as np
import random
import pygame
class Pipe:

    def __init__(self, window_width, window_height, hole_range, speed):
        self.top_height = np.random.randint(10,70)
        self.hole_height = np.random.randint(hole_range[0], hole_range[1])
        self.bottom_height = window_height - self.top_height - self.hole_height
        self.width = 20
        self.x_position = window_width
        self.rect_top = pygame.Rect(self.x_position, 0, self.width, self.top_height)
        self.rect_bottom = pygame.Rect(self.x_position, window_height - self.bottom_height, self.width, self.bottom_height)
        self.speed = speed
        self.color = pygame.Color(0,255,0)

    def update(self):
        self.x_position -= self.speed
        self.rect_top.x -= self.speed
        self.rect_bottom.x -= self.speed
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect_bottom)
        pygame.draw.rect(surface, self.color, self.rect_top)