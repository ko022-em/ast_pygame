# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import *
from circleshape import *

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    #importing the GUI screen mode
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #creating a game clock for FPS and tick updates
    clock = pygame.time.Clock()
    dt = 0
    # setting up the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #setting up an infinite loop for game updates
    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            screen.fill("black")
            player.draw(screen)
            player.update(dt)
            pygame.display.flip()

            # limit the framerate to 60 FPS
            dt = clock.tick(60) / 1000

if __name__ == "__main__":
   
    main()

