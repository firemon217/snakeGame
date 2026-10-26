
from apple import Apple

class AppleDecorator(Apple):
    """Базовый декоратор для яблока."""

    def __init__(self, apple):
        self._apple = apple

    @property
    def position(self):
        return self._apple.position

    @position.setter
    def position(self, value):
        self._apple.position = value

    @property
    def body_color(self):
        return self._apple.body_color

    @body_color.setter
    def body_color(self, value):
        self._apple.body_color = value

    @property
    def renderer(self):
        return self._apple.renderer

    @renderer.setter
    def renderer(self, value):
        self._apple.renderer = value

    @property
    def points(self):
        return self._apple.points

    def draw(self, surface):
        self._apple.draw(surface)

    def randomize_position(self):
        self._apple.randomize_position()


class GoldenAppleDecorator(AppleDecorator):
    """Золотое яблоко с дополнительными очками."""

    @property
    def points(self):
        return self._apple.points + 4

    def draw(self, surface):
        self._apple.draw(surface)

        # Дополнительная золотая рамка вокруг яблока
        import pygame

        x, y = self.position
        rect = pygame.Rect(x, y, 20, 20)
        pygame.draw.rect(surface, (255, 215, 0), rect, 3)
