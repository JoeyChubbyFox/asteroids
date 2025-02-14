# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # 1. Handle events first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # 2. Fill screen with black
        screen.fill((0, 0, 0))
    
        # 3. Flip display to show changes
        pygame.display.flip()

if __name__ == "__main__":
    main()