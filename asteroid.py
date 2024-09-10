import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self, score):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            score += 3
            return score
        score += 1 
        new_angle = random.uniform(20,50)
        vector1 = pygame.math.Vector2.rotate(self.velocity, new_angle)
        vector2 = pygame.math.Vector2.rotate(self.velocity, -new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid1.velocity = vector1 * 1.2
        new_asteroid2.velocity = vector2 * 1.2

        return score