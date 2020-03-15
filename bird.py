import pygame

class Bird:

    def __init__(self, window_height, gravity):
        self.width = 10
        self.height = 10
        self.position = [15, int(window_height / 2)]
        self.velocity = 0
        self.gravity = gravity
        self.acceleration = gravity
        self.max_velocity = 20
        self.jump_velocity = 10
        self.rect = pygame.Rect(self.position[0] - int(self.width/2), self.position[1] - int(self.height/2), self.width, self.height)
        self.color = pygame.Color(255,0,0)
    
    def update(self):
        self.velocity += self.acceleration
        self.velocity = max(self.velocity, -self.max_velocity)
        self.velocity = min(self.velocity, self.max_velocity)
        self.position[1] += self.velocity
        self.rect = pygame.Rect(self.position[0] - int(self.width/2), self.position[1] - int(self.height/2), self.width, self.height)
    
    def jump(self):
        self.velocity -= self.jump_velocity
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)