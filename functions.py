import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

## function to display the score constantly on the screen
def display_score(screen, score):
    font = pygame.font.SysFont(None, 100) # creates font object
    score_text = f"SCORE: {score}"
    rendered_text = font.render(score_text, True, "white") # renders font object
    text_rect = rendered_text.get_rect(topright=(SCREEN_WIDTH - 10, 10)) # simple rectangle around text
    screen.blit(rendered_text, text_rect) # draws font objects


def game_over_display(screen, score):
    clock = pygame.time.Clock()
    flash_timer = 0
    show_message = True
    waiting = True
    font = pygame.font.SysFont(None, 50) # creates font object
    large_font = pygame.font.SysFont(None, 100) # larger for game over
    
    while waiting:

        screen.fill("black") # can use ("colour") or ((0,0,0)) black

        dt = clock.tick(60) / 1000 # convert delta time into seconds
        flash_timer += dt

        if flash_timer > FLASH_INTERVAL / 1000: # remember conversions!
            flash_timer = 0
            show_message = not show_message

        if show_message:
            game_over_text = large_font.render("GAME OVER", True, "red")
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
            screen.blit(game_over_text, game_over_rect)

            quit_text = f"PRESS ESC TO QUIT"
            rendered_text = font.render(quit_text, True, "white")
            quit_rect = rendered_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200))
            screen.blit(rendered_text, quit_rect)

            retry_text = f"PRESS ENTER TO RETRY"
            rendered_retry = font.render(retry_text, True, "White")
            retry_rect = rendered_retry.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 250))
            screen.blit(rendered_retry, retry_rect)
        
        score_text = f"FINAL SCORE: {score}"
        rendered_score = font.render(score_text, True, "white")
        score_rect = rendered_score.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
        screen.blit(rendered_score, score_rect)
  
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # exits if window is closed
                return True
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_ESCAPE:  # Exits on esc key press
                    return True
                if event.key == pygame.K_RETURN:
                    return False
                


def reset_game(player, asteroidfield, updateable, drawable, asteroids, shots, score, GameOver):
    # reset score
    score = 0

    # clear the sprite groups
    updateable.empty()
    drawable.empty()
    asteroids.empty()
    shots.empty()

    # reinitialise player and asteroid field
    player = Player(x= SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, radius = PLAYER_RADIUS)
    asteroidfield = AsteroidField()

    # reset GameOver status
    GameOver = False

    print("Game has been reset.")

    # return everything 
    return player, asteroidfield, updateable, drawable, asteroids, shots, score, GameOver
