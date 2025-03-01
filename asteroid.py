import pygame  # Add this import
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, SCREEN_WIDTH, SCREEN_HEIGHT

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        print("Asteroid init called")
        # Call the parent's __init__ with x, y, radius
        CircleShape.__init__(self, x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        print("Asteroid split called")
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Don't split tiny asteroids
        
        # Create two new asteroids with half the radius
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a = Asteroid(self.position.x, self.position.y, new_radius)
        b = Asteroid(self.position.x, self.position.y, new_radius)
        # Rotate the original velocity by a random angle in opposite directions
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        # Also scale up by 1.2
        a.velocity = velocity1 * 1.2
        b.velocity = velocity2 * 1.2
        return a, b    
