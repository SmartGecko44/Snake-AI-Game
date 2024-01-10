# Apple class
import random

import pygame

from SnakeAIGame.constants import CELL_SIZE, RED


class Apple:
    def __init__(self, width, height):
        self.position = (random.randint(0, (width - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (height - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (*self.position, CELL_SIZE, CELL_SIZE))
