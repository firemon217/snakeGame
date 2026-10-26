import pygame

from game_system import System

from renderers import NeonRenderer
from game_facade import GameFacade

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

SPEED = 20

class Game:
    def __init__(self, config=None):
        self.system = System()
        self.config = config
        self.facade = GameFacade(config, NeonRenderer())

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit

            self.facade.handle_event(event)
            
    def update(self):
        while True:
            self.system.clock.tick(SPEED)
    
            self.handle_keys()
            self.facade.update()