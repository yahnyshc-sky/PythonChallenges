# Snake Game using Pygame
import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 600, 600
GAME_WIDTH, GAME_HEIGHT = 300, 300
OFFSET_X, OFFSET_Y = 150, 150
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Background Image
bg_image_path = os.path.join(os.path.dirname(__file__), 'images', 'canon.webp')
bg_image = pygame.image.load(bg_image_path)
bg_image = pygame.transform.scale(bg_image, (GAME_WIDTH, GAME_HEIGHT))

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

# # Sound Effects
# eat_sound_path = os.path.join(os.path.dirname(__file__), 'sounds', 'eat.wav')
# eat_sound = pygame.mixer.Sound(eat_sound_path)
# bg_sound_path = os.path.join(os.path.dirname(__file__), 'sounds', 'bg_music.wav')
# bg_sound = pygame.mixer.Sound(bg_sound_path)

# pygame.mixer.music.load(bg_sound_path)
# pygame.mixer.music.play(-1)

def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
        pygame.draw.rect(screen, BLACK, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE), 1)

def draw_food(food_position):
    pygame.draw.rect(screen, BLUE, pygame.Rect(food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE))

def show_score(score):
    score_surface = FONT.render(f'Score: {score}', True, BLACK)
    screen.blit(score_surface, (WIDTH // 2 - score_surface.get_width() // 2, 10))

def game_over(score): 
    while True:
        screen.fill(WHITE)
        # screen.blit(bg_image, (GAME_WIDTH, GAME_HEIGHT))
        game_over_surface = FONT.render('Game Over!', True, BLACK)
        screen.blit(game_over_surface, ((WIDTH - game_over_surface.get_width()) // 2, HEIGHT // 3))
        
        score_surface = FONT.render(f'Final Score: {score}', True, BLACK)
        screen.blit(score_surface, ((WIDTH - score_surface.get_width()) // 2, HEIGHT // 2))

        retry_surface = FONT.render('Press R to Retry or Q to Quit', True, BLACK)
        screen.blit(retry_surface, ((WIDTH - retry_surface.get_width()) // 2, HEIGHT // 1.5))

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
    snake_position = [300, 300]
    snake_body = [[300, 300], [290, 300], [280, 300]]
    food_position = [(random.randrange(1, (GAME_WIDTH // SNAKE_SIZE)) * SNAKE_SIZE)+OFFSET_X,
                     (random.randrange(1, (GAME_HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE)+OFFSET_Y]
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
            # eat_sound.play()
        else:
            snake_body.pop()

        if not food_spawn:
            food_position = [(random.randrange(1, (GAME_WIDTH // SNAKE_SIZE)) * SNAKE_SIZE)+OFFSET_X,
                             (random.randrange(1, (GAME_HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE)+OFFSET_Y]
        food_spawn = True

        screen.fill(WHITE)
        screen.blit(bg_image, (OFFSET_X, OFFSET_Y))

        border_radius=5
        pygame.draw.rect(screen, BLACK, pygame.Rect(OFFSET_X-5, OFFSET_Y-5, GAME_WIDTH+10, GAME_HEIGHT+10), border_radius)
        draw_snake(snake_body)
        draw_food(food_position)
        show_score(score)

        if (snake_position[0] < 0 or snake_position[0] >= GAME_WIDTH+OFFSET_X or snake_position[0] < GAME_WIDTH-OFFSET_X or
                snake_position[1] < 0 or snake_position[1] >= GAME_HEIGHT+OFFSET_Y or snake_position[1] < GAME_HEIGHT-OFFSET_Y):
            game_over(score)

        for block in snake_body[1:]:
            if snake_position == block:
                game_over(score)

        pygame.display.flip()
        clock.tick(SNAKE_SPEED)

if __name__ == '__main__':
    main()

