import pygame
from game_composite import GameComponent
from game_object import GameObject
from typing import Optional, Tuple, List

# Константы экрана и сетки
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480  # Размеры окна
GRID_SIZE = 20  # Размер одной клетки
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE  # Количество клеток по горизонтали
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE  # Количество клеток по вертикали
SNAKE_COLOR = (0, 255, 125)  # Цвет змейки



class SnakeSegment(GameComponent):
    """Один сегмент тела змейки."""

    def __init__(self, game_object, position):
        self.game_object = game_object
        self.position = position

    def draw(self, surface):
        self.game_object.draw_cell(
            surface,
            self.position,
            self.game_object.body_color
        )
    
class Snake(GameObject):
    """
    Класс, представляющий змейку в игре.
    """

    def __init__(self, renderer=None) -> None:
        """
        Инициализирует змейку в центре экрана.
        """
        super().__init__((GRID_WIDTH // 2 * GRID_SIZE, GRID_HEIGHT // 2 * GRID_SIZE), SNAKE_COLOR, renderer)
        self.length: int = 1
        self.segments: List[SnakeSegment] = [SnakeSegment(self, self.position)]
        self.direction: Tuple[int, int] = (1, 0)
        self.next_direction: Optional[Tuple[int, int]] = None

    def update_direction(self, new_direction: Tuple[int, int]) -> None:
        """
        Обновляет направление движения змейки, если оно не противоположное текущему.
        """
        if new_direction != (-self.direction[0], -self.direction[1]):
            self.next_direction = new_direction

    def move(self) -> None:
        """
        Перемещает змейку на одну клетку в текущем направлении.
        Если змейка сталкивается с собой, игра сбрасывается.
        """
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

        cur_head = self.segments[0]  # Текущая голова змейки
        x, y = self.direction
        
        # Рассчитываем новую позицию головы с учётом границ экрана
        new_head = ((cur_head.position[0] + x * GRID_SIZE) % SCREEN_WIDTH,
                    (cur_head.position[1] + y * GRID_SIZE) % SCREEN_HEIGHT)

        # Проверяем столкновение с телом
        if len(self.segments) > 2 and new_head in [segment.position for segment in self.segments[2:]]:
            self.reset()
        else:
            self.segments.insert(0, SnakeSegment(self, new_head))  # Добавляем новую голову
            if len(self.segments) > self.length:
                self.segments.pop()  # Удаляем последний сегмент, если змейка не растёт

    def get_head_position(self) -> Tuple[int, int]:
        """
        Возвращает текущие координаты головы змейки.
        
        :return: Кортеж с координатами (x, y).
        """
        return self.segments[0].position

    def reset(self) -> None:
        """
        Сбрасывает змейку в начальное состояние после столкновения с собой.
        """
        self.length = 1
        self.segments = [SnakeSegment(self, (GRID_WIDTH // 2 * GRID_SIZE, GRID_HEIGHT // 2 * GRID_SIZE))]
        self.direction = (1, 0)
        self.next_direction = None

    def draw(self, surface: pygame.Surface) -> None:
        """
        Отображает змейку на игровом поле.
        Голова выделяется отдельным цветом.
        
        :param surface: Поверхность Pygame, на которой рисуется змейка.
        """
        pass