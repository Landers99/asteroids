# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        updatable.update(dt)

        for obj in asteroid:
            for shot in shots:
                if obj.check_for_collision(shot):
                    obj.kill()
                    shot.kill()

            player_collision = obj.check_for_collision(player)
            if player_collision:
                print("Game over!")
                sys.exit()

        for obj in drawable:
            obj.draw(screen)

        dt = clock.tick(60) / 1000
        # call last
        pygame.display.flip()

if __name__ == "__main__":
    main()
