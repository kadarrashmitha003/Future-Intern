import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Display size
WIDTH, HEIGHT = 600, 400
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock to control the speed of the game
CLOCK = pygame.time.Clock()
SNAKE_SIZE = 10
SNAKE_SPEED = 15

def message(msg, color):
    """Display messages to the screen."""
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, color)
    DISPLAY.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0

    while not game_over:

        while game_close:
            DISPLAY.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_SIZE
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        DISPLAY.fill(BLACK)
        pygame.draw.rect(DISPLAY, GREEN, [foodx, foody, SNAKE_SIZE, SNAKE_SIZE])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for segment in snake_List:
            pygame.draw.rect(DISPLAY, WHITE, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])
        
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0
            Length_of_snake += 1

        CLOCK.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()
