
from dataclasses import dataclass

@dataclass
class GameConfig:
    """Конфигурация игры «Змейка»."""

    screen_width: int = 640
    screen_height: int = 480
    grid_size: int = 20
    speed: int = 20

    background_color: tuple[int, int, int] = (0, 0, 0)
    snake_color: tuple[int, int, int] = (0, 255, 125)
    apple_color: tuple[int, int, int] = (255, 125, 0)

    def validate(self) -> None:
        """Проверяет корректность настроек."""

        if self.screen_width <= 0 or self.screen_height <= 0:
            raise ValueError("Размеры экрана должны быть положительными.")

        if self.grid_size <= 0:
            raise ValueError("Размер клетки должен быть положительным.")

        if (
            self.screen_width % self.grid_size != 0
            or self.screen_height % self.grid_size != 0
        ):
            raise ValueError(
                "Размеры экрана должны делиться на размер клетки без остатка."
            )

        if self.speed <= 0:
            raise ValueError("Скорость игры должна быть положительной.")

        for color in (
            self.background_color,
            self.snake_color,
            self.apple_color,
        ):
            if (
                len(color) != 3
                or any(not isinstance(c, int) or not 0 <= c <= 255
                       for c in color)
            ):
                raise ValueError(
                    "Цвет должен состоять из трёх целых чисел от 0 до 255."
                )
