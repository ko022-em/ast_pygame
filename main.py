# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

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
    #creating groups to place objects within
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #making those groups containers for the classes
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    #setting up the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #setting up the asteroid field
    asteroid_field = AsteroidField()
    #setting up an infinite loop for game updates
    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            screen.fill("black")
            for d in drawable:
                d.draw(screen)
            player.update(dt, shots)
            for obj in updateable:
                if obj != player:
                    obj.update(dt)
            for a in asteroids:
                if a.collision(player):
                    raise Exception("Game over!")
            shots.update(dt)
            for shot in shots:
                shot.draw(screen)
            for a in asteroids:
                for shot in shots:
                    if a.collision(shot):
                        a.split()
                        shot.kill()
            pygame.display.flip()

            # limit the framerate to 60 FPS
            dt = clock.tick(60) / 1000

if __name__ == "__main__":
   
    main()

