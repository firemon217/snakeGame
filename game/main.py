from random import randint
import pygame

from config.game_config_builder import GameConfigBuilder
from config.game_conifg_director import GameConfigDirector
from main_menu import MainMenu
from game_system import System
from game import Game

# Инициализация PyGame:
pygame.init()
pygame.display.set_caption('Змейка')

if __name__ == '__main__':
    """
    Главный игровой цикл:
    - Создаёт экземпляры змейки и яблока.
    - Обрабатывает ввод с клавиатуры.
    - Обновляет положение змейки.
    - Проверяет, съела ли змейка яблоко.
    - Перерисовывает экран.
    """
    builder = GameConfigBuilder()
    director = GameConfigDirector(builder)

    # Выбираем конфигурацию игры.
    config = director.create_normal_config()

    system = System()

    system.initialize()

    MainMenu = MainMenu()
    Game = Game()
    MainMenu.show_menu()
    Game.update()

    
