from bird import Bird
from pipe import Pipe
import pygame
import time

class Environment:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bird = Bird(height, 1)
        self.pipes = []
        self.pipe_speed = 2
        self.pipe_speed_increment = 0.1
        self.max_pipe_speed = 5
        self.hole_range = (50,100)
        self.pipe_interval = 60
        self.score = 0
        self.game_over = False
        pygame.init()
        self.surface = pygame.display.set_mode((width,height))
        background = pygame.Surface((width,height))
        self.surface.blit(background, (0,0))
    
    def update(self):
        self.bird.update()
        self.bird.draw(self.surface)        
        for pipe in self.pipes:
            pipe.update()
            if pipe.x_position + pipe.width <= 0:
                self.pipes.remove(pipe)
                self.score += 1
            pipe.draw(self.surface)

        if self.check_collision():
            print('Score: ', str(self.score))
            self.game_over = True
    
    def run(self):
        white = pygame.Color(255,255,255)
        pygame.display.set_caption('Flappy Bird')
        clock = pygame.time.Clock()
        timestamp = 0
        keypressed = False
        while not self.game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    break
                elif event.type == pygame.KEYDOWN:
                    if not keypressed and event.key == pygame.K_SPACE:
                        self.bird.jump()
                        keypressed = True
                        print('Key Pressed')
                elif event.type == pygame.KEYUP:
                    if keypressed and event.key == pygame.K_SPACE:
                        keypressed = False

            self.surface.fill(white)
            self.update()
            if timestamp % self.pipe_interval == 0:
                self.pipes.append(Pipe(self.width, self.height, self.hole_range, self.pipe_speed))
            pygame.display.update()
            clock.tick(10)
            timestamp += 1
        time.sleep(2)
    
    def check_collision(self):
        bird = self.bird
        for pipe in self.pipes:
            if bird.rect.colliderect(pipe.rect_top) or bird.rect.colliderect(pipe.rect_bottom):
                return True
        if bird.position[1] + bird.height >= self.height:
            return True
        return False
