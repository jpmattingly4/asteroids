# this allows us to use code from
# the open-source pygame library
# throughtout this file
import pygame
from constants import *

def main():
    pygame.init() # initializes all imported pygame modules
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # sets GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # functionality for windows close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()
        
if __name__ == "__main__":
    main()