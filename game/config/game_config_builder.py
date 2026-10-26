

from .game_config import GameConfig

class GameConfigBuilder:
    """Пошагово создаёт конфигурацию игры."""

    def __init__(self):
        self.reset()

    def reset(self):
        """Создаёт новую конфигурацию для сборки."""
        self._config = GameConfig()
        return self

    def set_screen_size(self, width: int, height: int):
        self._config.screen_width = width
        self._config.screen_height = height
        return self

    def set_grid_size(self, size: int):
        self._config.grid_size = size
        return self

    def set_speed(self, speed: int):
        self._config.speed = speed
        return self

    def set_background_color(self, color: tuple[int, int, int]):
        self._config.background_color = color
        return self

    def set_snake_color(self, color: tuple[int, int, int]):
        self._config.snake_color = color
        return self

    def set_apple_color(self, color: tuple[int, int, int]):
        self._config.apple_color = color
        return self

    def build(self) -> GameConfig:
        """Проверяет и возвращает готовую конфигурацию."""
        self._config.validate()
        result = self._config
        self.reset()
        return result
