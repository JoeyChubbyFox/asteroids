import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        print("Shot init called")
        # Call the parent's __init__ with x, y, radius
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self)  # Initialize the Sprite base class
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity; player will set this in `shoot`

    def draw(self, screen):
        # Draw the shot as a circle
        pygame.draw.circle(screen, "gray", self.position, SHOT_RADIUS, 2)
    
    def update(self, dt):
        # Update the position of the shot based on its velocity
        self.position += self.velocity * dt
        
        # Remove the shot if it goes off-screen
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or 
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()  # The `kill()` method removes the sprite from all groups