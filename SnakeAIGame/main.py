# Main function
import sys

import pygame

from SnakeAIGame.apple import Apple
from SnakeAIGame.constants import FPS, BLACK
from SnakeAIGame.snake import Snake


def handle_events(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            handle_keydown_event(event.key, snake)


def handle_keydown_event(key, snake):
    directions = {
        pygame.K_w: (0, -1),
        pygame.K_s: (0, 1),
        pygame.K_a: (-1, 0),
        pygame.K_d: (1, 0)
    }

    if key in directions:
        snake.change_direction(directions[key])


def check_collision_and_update(snake, apples, width, height):
    for apple in apples:
        if snake.body[0] == apple.position:
            snake.grow()
            apples.remove(apple)
            apples.append(Apple(width, height))

    if snake.check_collision():
        print("Game Over!")
        pygame.quit()
        sys.exit()


def draw_objects(screen, snake, apples):
    screen.fill(BLACK)
    snake.draw(screen)
    for apple in apples:
        apple.draw(screen)


def main_loop():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    width, height = screen.get_size()
    snake = Snake(width, height)
    apples = [Apple(width, height) for _ in range(3)]  # Spawn 3 apples initially

    while True:
        handle_events(snake)
        snake.move()
        check_collision_and_update(snake, apples, width, height)
        draw_objects(screen, snake, apples)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main_loop()
