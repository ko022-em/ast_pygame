# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()

    #importing the GUI screen mode
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #setting up an infinite loop for game updates
    num = 0
    while num == 0:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            return
    pygame.surface.fill(255,255,255)
    pygame.display.flip()

if __name__ == "__main__":
   
    main()

