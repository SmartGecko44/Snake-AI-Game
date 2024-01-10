# Snake class
import pygame

from SnakeAIGame.constants import CELL_SIZE, GREEN


class Snake:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (1, 0)  # Initial direction (right)

    def move(self):
        head = (self.body[0][0] + self.direction[0] * CELL_SIZE, self.body[0][1] + self.direction[1] * CELL_SIZE)
        self.body.insert(0, head)
        self.body.pop()

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:  # Avoid moving backward
            self.direction = new_direction

    def grow(self):
        tail_direction = (self.body[-1][0] - self.body[-2][0], self.body[-1][1] - self.body[-2][1])
        new_tail = (self.body[-1][0] + tail_direction[0], self.body[-1][1] + tail_direction[1])
        self.body.append(new_tail)

    def check_collision(self):
        return (
            self.body[0][0] < 0
            or self.body[0][0] >= self.width
            or self.body[0][1] < 0
            or self.body[0][1] >= self.height
            or self.body[0] in self.body[1:]
        )

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

