from random import randint
import pygame

from main_menu import MainMenu
from game_system import System
from apple import Apple
from snake import Snake
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
    System.initialize()


    MainMenu = MainMenu()
    Game = Game()
    MainMenu.show_menu()
    Game.update()

    
