
from .game_config import GameConfig
from .game_config_builder import GameConfigBuilder


class GameConfigDirector:
    """Создаёт готовые конфигурации игровых режимов."""

    def __init__(self, builder: GameConfigBuilder):
        self._builder = builder

    def create_easy_config(self) -> GameConfig:
        """Лёгкий режим: медленная змейка."""
        return (
            self._builder
            .set_screen_size(640, 480)
            .set_grid_size(20)
            .set_speed(10)
            .set_background_color((0, 0, 0))
            .set_snake_color((0, 255, 125))
            .set_apple_color((255, 125, 0))
            .build()
        )

    def create_normal_config(self) -> GameConfig:
        """Обычный режим: стандартные настройки."""
        return (
            self._builder
            .set_screen_size(640, 480)
            .set_grid_size(20)
            .set_speed(20)
            .set_background_color((0, 0, 0))
            .set_snake_color((0, 255, 125))
            .set_apple_color((255, 125, 0))
            .build()
        )

    def create_hard_config(self) -> GameConfig:
        """Сложный режим: высокая скорость."""
        return (
            self._builder
            .set_screen_size(800, 600)
            .set_grid_size(20)
            .set_speed(30)
            .set_background_color((20, 20, 30))
            .set_snake_color((255, 80, 80))
            .set_apple_color((255, 200, 0))
            .build()
        )
