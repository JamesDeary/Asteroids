# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from functions import *


def main():
    print("Starting asteroids!")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    large_font = pygame.font.SysFont(None, 80) # larger for game over

    bg_image = pygame.image.load('asteroids_bg.png')
    bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Player Triangle Test")

    player = Player(x= SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, radius = PLAYER_RADIUS)
    asteroidfield = AsteroidField()

    GameOver = False
    GameStart = False

    ## while loop for start screen
    while GameStart == False:
        #screen.fill("black") # can use ("colour") or ((0,0,0)) black
        screen.blit(bg_image, (0,0))

        game_start_text = large_font.render("PRESS RETURN TO START ASTEROIDS", True, "white")
        game_start_rect = game_start_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
        screen.blit(game_start_text, game_start_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # exits if window is closed
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    GameStart = True
    

    ## while loop for game loop
    while not GameOver and GameStart:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # exits if window is closed
                return
            
        screen.fill((0,0,0))
        #screen.blit(bg_image, (0,0))
        display_score(screen, score)

        for thing in updateable:
            thing.update(dt)

        for thing in asteroids:
            if thing.collisions(player):
                print("Game over!")
                print(f"Your score was: {score}")
                GameOver = True
                
            for shot in shots:
                if shot.collisions(thing):
                    shot.kill()
                    score = thing.split(score)
        

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

        if GameOver:
            GameOver = game_over_display(screen, score)
            if not GameOver:
                player, asteroidfield, updateable, drawable, asteroids, shots, score, GameOver = reset_game(player, asteroidfield, updateable, drawable, asteroids, shots, score, GameOver)
            else:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
    