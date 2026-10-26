
import pygame

from game_system import System
from snake import GRID_SIZE, Snake
from apple import Apple
from factory.apple_factory import AppleCreator
from game_composite import GameGroup
from input_adapter import InputAdapter

from factory.snake_segment_factory import SnakeSegmentFactory

BOARD_BACKGROUND_COLOR = (0,0,0)

class GameFacade:
    """Упрощённый интерфейс для основных игровых подсистем."""

    def __init__(self, config=None, renderer=None):
        self.config = config
        self.renderer = renderer
        self.system = System()

        self.snake = Snake(renderer)
        self.apple = Apple(renderer)

        self.input_adapter = InputAdapter(self.snake)

    def handle_event(self, event):
        """Передаёт управление клавишами змейке."""
        if event.type != pygame.KEYDOWN:
            return

        self.input_adapter.handle_event(event)
        
    def update(self):
        """Обновляет состояние игровых объектов."""
        self.snake.move()

        # Проверка, съела ли змейка яблоко
        if self.snake.get_head_position() == self.apple.position:
            self.snake.length += 1

            # Создаём новое яблоко клонированием предыдущего.
            self.apple = self.apple.clone()
            self.apple.randomize_position()

            # Не размещаем яблоко внутри змейки.
            while self.apple.position in [segment.position for segment in self.snake.segments]:
                self.score += self.apple.points
                self.apple.randomize_position()

        # Отрисовка игрового экрана
        self.system.screen.fill(BOARD_BACKGROUND_COLOR)
        snake_group = GameGroup()

        for segment in self.snake.segments:
            snake_group.add(segment)

        flyweight = SnakeSegmentFactory.get_flyweight(
            self.system.screen,
            self.snake.body_color,
            GRID_SIZE,
            self.snake.renderer
        )

        snake_group.draw(flyweight)
        self.apple.draw(self.system.screen)

        pygame.display.update()
