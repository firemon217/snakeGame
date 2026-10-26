import pygame
from typing import Optional, Tuple
from copy import deepcopy
from renderers import Renderer, PygameRenderer

GRID_SIZE = 20
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BORDER_COLOR = (0, 0, 0)


class GameObject:
    """Базовый игровой объект с отделённой отрисовкой."""

    def __init__(
        self,
        position: Optional[Tuple[int, int]] = None,
        body_color: Optional[Tuple[int, int, int]] = None,
        renderer: Optional[Renderer] = None,
    ) -> None:
        self.position = (
            position
            if position is not None
            else (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        )
        self.body_color = (
            body_color if body_color is not None else (255, 255, 255)
        )
        self.renderer = renderer or PygameRenderer()

    def draw(self, surface: pygame.Surface) -> None:
        pass

    def draw_cell(
        self,
        surface: pygame.Surface,
        position: Tuple[int, int],
        color: Optional[Tuple[int, int, int]] = None,
    ) -> None:
        self.renderer.draw_cell(
            surface,
            position,
            color if color is not None else self.body_color,
            GRID_SIZE,
        )

    def clone(self):
        """Создаёт независимую копию игрового объекта."""
        return deepcopy(self)