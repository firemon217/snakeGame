import pygame
from abc import ABC, abstractmethod

class Renderer(ABC):
    """Интерфейс реализации отрисовки."""

    @abstractmethod
    def draw_cell(self, surface, position, color, grid_size):
        pass


class PygameRenderer(Renderer):
    """Стандартная отрисовка клеток."""

    def draw_cell(self, surface, position, color, grid_size):
        rect = pygame.Rect(
            position[0], position[1], grid_size, grid_size
        )
        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, (0, 0, 0), rect, 1)


class NeonRenderer(Renderer):
    """Альтернативная отрисовка с неоновой рамкой."""

    def draw_cell(self, surface, position, color, grid_size):
        rect = pygame.Rect(
            position[0], position[1], grid_size, grid_size
        )
        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, (0, 255, 255), rect, 2)