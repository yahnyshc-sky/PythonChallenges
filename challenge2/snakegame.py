# Snake Game using Pygame

import pygame
import random
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Colours 
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Snake settings
SNAKE_SIZE = 10
SNAKE_SPEED = 15
FONT = pygame.font.SysFont('arial', 25)

def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
        pygame.draw.rect(screen, BLACK, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE), 1)

def draw_food(food_position):
    pygame.draw.rect(screen, RED, pygame.Rect(food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE))

def show_score(score):
    score_surface = FONT.render(f'Score: {score}', True, WHITE)
    screen.blit(score_surface, (10, 10))

def game_over(score): 
    while True:
        screen.fill(BLACK)
        game_over_surface = FONT.render(f'Game Over! Your Score: {score}', True, WHITE)
        screen.blit(game_over_surface, (WIDTH // 6, HEIGHT // 3))
        
        retry_surface = FONT.render('Press R to Retry or Q to Quit', True, WHITE)
        screen.blit(retry_surface, (WIDTH // 6, HEIGHT // 2))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()  # Restart the game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()  


def main():
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    food_position = [random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                     random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
    food_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        direction = change_to

        if direction == 'UP':
            snake_position[1] -= SNAKE_SIZE
        elif direction == 'DOWN':
            snake_position[1] += SNAKE_SIZE
        elif direction == 'LEFT':
            snake_position[0] -= SNAKE_SIZE
        elif direction == 'RIGHT':
            snake_position[0] += SNAKE_SIZE

        snake_body.insert(0, list(snake_position))
        if snake_position == food_position:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_position = [random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                             random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
        food_spawn = True

        screen.fill(BLACK)
        draw_snake(snake_body)
        draw_food(food_position)
        show_score(score)

        if (snake_position[0] < 0 or snake_position[0] >= WIDTH or
                snake_position[1] < 0 or snake_position[1] >= HEIGHT):
            game_over(score)

        for block in snake_body[1:]:
            if snake_position == block:
                game_over(score)

        pygame.display.flip()
        clock.tick(SNAKE_SPEED)

if __name__ == '__main__':
    main()

