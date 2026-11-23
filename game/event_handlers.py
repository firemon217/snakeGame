
import pygame
from abc import ABC, abstractmethod

from input_adapter import InputAdapter


class EventHandler(ABC):
    """Базовый класс обработчика цепочки событий."""

    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        """Устанавливает следующего обработчика в цепочке."""
        self._next_handler = handler
        return handler

    def handle(self, event):
        """Обрабатывает событие или передаёт его дальше."""

        if self.can_handle(event):
            return self.process(event)

        if self._next_handler is not None:
            return self._next_handler.handle(event)

        return False

    @abstractmethod
    def can_handle(self, event):
        """Проверяет, может ли обработчик принять событие."""
        pass

    @abstractmethod
    def process(self, event):
        """Обрабатывает принятое событие."""
        pass


class QuitEventHandler(EventHandler):
    """Обрабатывает закрытие игрового окна."""

    def can_handle(self, event):
        return event.type == pygame.QUIT

    def process(self, event):
        pygame.quit()
        raise SystemExit


class EscapeEventHandler(EventHandler):
    """Обрабатывает нажатие клавиши Escape."""

    def can_handle(self, event):
        return (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE
        )

    def process(self, event):
        pygame.quit()
        raise SystemExit


class MovementEventHandler(EventHandler):
    """Обрабатывает управление движением змейки."""

    def __init__(self, snake):
        super().__init__()
        self.input_adapter = InputAdapter(snake)

    def can_handle(self, event):
        return (
            event.type == pygame.KEYDOWN
            and event.key in (
                pygame.K_UP,
                pygame.K_DOWN,
                pygame.K_LEFT,
                pygame.K_RIGHT
            )
        )

    def process(self, event):
        self.input_adapter.handle_event(event)
        return True


def create_game_event_chain(snake):
    """Создаёт цепочку обработки игровых событий."""

    quit_handler = QuitEventHandler()
    escape_handler = EscapeEventHandler()
    movement_handler = MovementEventHandler(snake)

    quit_handler.set_next(escape_handler).set_next(movement_handler)

    return quit_handler
