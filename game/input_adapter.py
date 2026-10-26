import pygame


class InputAdapter:
    """Адаптирует события Pygame к командам управления."""

    def __init__(self, snake):
        self.snake = snake

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        directions = {
            pygame.K_UP: (0, -1),
            pygame.K_DOWN: (0, 1),
            pygame.K_LEFT: (-1, 0),
            pygame.K_RIGHT: (1, 0),
        }

        direction = directions.get(event.key)

        if direction is not None:
            self.snake.update_direction(direction)