import pygame

class System:
    """Singleton для управления игровыми ресурсами."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if getattr(self, "_initialized", False):
            return

    screen_width = 640
    screen_height = 480
    screen = None
    clock = None

    def initialize(self, config=None):
        pygame.init()

        if config is not None:
            config.validate()
            self.screen_width = config.screen_width
            self.screen_height = config.screen_height

        pygame.display.set_caption("Змейка")
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )
        self.clock = pygame.time.Clock()

    def set_screen_size(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Размеры экрана должны быть положительными.")
        
        System.screen_width = width
        System.screen_height = height

        if self.screen is not None:
            self.screen = pygame.display.set_mode((width, height))

