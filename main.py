import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Screen created")

    # Create groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Set containers before creating the player
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
                                    
    # Now create the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    print("Player created")

    # Create the asteroid field
    asteroid_field = AsteroidField()
    print("Asteroid field created")

    clock = pygame.time.Clock()
    dt = 0

    while True:
        #print("Game loop running")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill screen with black
        screen.fill((0, 0, 0))
        
        # Draw player - Make sure this line exists!
        for entity in drawable:
            entity.draw(screen)
        
        # Draw each shot in the shots group
        for shot in shots:
            shot.draw(screen)

        # Check collissions between shots and asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    shot.kill()
                    new_asteroids = asteroid.split()
                    # If new_asteroids is not None, add them to the asteroids list
                    if new_asteroids:
                         asteroids.add(*new_asteroids)  # The * unpacks the tuple into separate arguments
        
        # Update display
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

        # Update game objects
        print(f"updatable count: {len(updatable)}")
        updatable.update(dt)  # <- This ensures the player processes input each frame
        
        # Update each shot in the shots group
        shots.update(dt)

        # After the update section in your game loop
        for asteroid in asteroids:  # Assuming asteroids_group is your group of asteroids
            if player.collides_with(asteroid):  # Using the method you just created
                print("Game over!")
                sys.exit()  # Don't forget to import sys at the top of your file

if __name__ == "__main__":
    main() 