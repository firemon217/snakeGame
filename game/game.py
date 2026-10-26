import pygame

from apple import Apple
from factory.apple_factory import AppleCreator
from game_system import System
from snake import Snake

from input_adapter import InputAdapter
from renderers import NeonRenderer
from apple_decorator import GoldenAppleDecorator
from game_composite import GameGroup

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

SPEED = 20

BOARD_BACKGROUND_COLOR = (0,0,0)

class Game:
    def __init__(self):
        self.system = System()
        self.snake = Snake(renderer=NeonRenderer())
        self.input_adapter = InputAdapter(self.snake)
        self.apple_factory = AppleCreator()
        self.apple = self.apple_factory.create(renderer=NeonRenderer())
        self.apple = GoldenAppleDecorator(self.apple)
        self.score = 0
        self.game_over = False

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise SystemExit

            self.input_adapter.handle_event(event)

    def update(self):
        while True:
            self.system.clock.tick(SPEED)
    
            self.handle_keys()
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

            snake_group.draw(self.system.screen)
            self.apple.draw(self.system.screen)
    
            pygame.display.update()