import pygame

from apple import Apple
from game_system import System
from snake import Snake
import snake

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

SPEED = 20

BOARD_BACKGROUND_COLOR = (0,0,0)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0
        self.game_over = False

    def handle_keys(self) -> None:
        """
        Обрабатывает нажатия клавиш для управления змейкой.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.update_direction(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.update_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.update_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.update_direction(RIGHT)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise SystemExit

    def update(self):
        while True:
            System.clock.tick(SPEED)
    
            self.handle_keys()
            self.snake.move()
    
            # Проверка, съела ли змейка яблоко
            if self.snake.get_head_position() == self.apple.position:
                self.snake.length += 1  # Увеличение длины змейки
                self.apple.randomize_position()
                print(f'Новое яблоко на позиции: {self.apple.position}')
                
                # Гарантия, что яблоко не появится внутри змейки
                while self.apple.position in self.snake.positions:
                    self.apple.randomize_position()
    
            # Отрисовка игрового экрана
            System.screen.fill(BOARD_BACKGROUND_COLOR)
            self.snake.draw(System.screen)
            self.apple.draw(System.screen)
    
            pygame.display.update()