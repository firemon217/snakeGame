import pygame

class System:

    screen_width = 640
    screen_height = 480
    screen = None
    clock = None

    @staticmethod
    def initialize():
        pygame.init()
        pygame.display.set_caption('Змейка')
        System.screen = pygame.display.set_mode(
            (System.screen_width, System.screen_height)
        )
        System.clock = pygame.time.Clock()

    @staticmethod
    def setScreenSize(width, height):
        System.screen_width = width
        System.screen_height = height
        System.screen = pygame.display.set_mode((System.screen_width, System.screen_height), 0, 32)

