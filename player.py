import pygame  # Add this import
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y, shots):
        print("Player init called")
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = shots  # Link the player's shots to the global shots group
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # The assignment says to use pygame.draw.polygon with:
        # - screen object
        # - "white" color
        # - self.triangle() for points
        # - line width of 2
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        # Decrease the timer, but don't let it go below 0
        if self.timer > 0:
            self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left, so reverse dt
            self.rotate(-dt)
            self.rotation = self.rotation % 360
        if keys[pygame.K_d]:
            # Rotate right, so use dt directly
            self.rotate(dt)
            self.rotation = self.rotation % 360
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        print("Player shoot called")
        if self.timer <= 0:
            # Create a new shot at the player's position
            new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
    
            # Set the velocity of the shot
            direction = pygame.Vector2(0, 1)  # Start with "up"
            direction = direction.rotate(self.rotation)  # Rotate it to match the player's angle
            new_shot.velocity = direction * PLAYER_SHOOT_SPEED  # Scale it by the shot speed
    
            # Add the shot to your shots group
            self.shots.add(new_shot)

            self.timer = PLAYER_SHOOT_COOLDOWN