
import pygame
from enum import Enum
from game_system import System


class MenuItems(Enum):
    START_GAME = 0
    OPTIONS = 1
    EXIT = 2


class MainMenu:
    def __init__(self):
        font = pygame.font.SysFont('Arial', 42, bold=True)
        button_font = pygame.font.SysFont('Arial', 28)

        self.title = font.render('ЗМЕЙКА', True, (0, 255, 125))

        self.start_text = button_font.render(
            'НАЧАТЬ ИГРУ', True, (255, 255, 255)
        )
        self.option_text = button_font.render(
            'НАСТРОЙКИ', True, (255, 255, 255)
        )
        self.exit_text = button_font.render(
            'ВЫХОД', True, (255, 255, 255)
        )

        self.start_button = pygame.Rect(170, 200, 300, 50)
        self.option_button = pygame.Rect(170, 270, 300, 50)
        self.exit_button = pygame.Rect(170, 340, 300, 50)

        self.menu_items = [
            MenuItems.START_GAME,
            MenuItems.OPTIONS,
            MenuItems.EXIT
        ]

        self.button_colors = {
            MenuItems.START_GAME: (0, 100, 50),
            MenuItems.OPTIONS: (100, 50, 50),
            MenuItems.EXIT: (100, 50, 0)
        }

        self.buttons = {
            MenuItems.START_GAME: self.start_button,
            MenuItems.OPTIONS: self.option_button,
            MenuItems.EXIT: self.exit_button
        }

        self.selected_index = 0

    def show_menu(self):
        """Отображает главное меню и обрабатывает ввод."""

        while True:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        raise SystemExit

                    elif event.key in (pygame.K_UP, pygame.K_w):
                        self.navigate("up")

                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self.navigate("down")

                    elif event.key in (
                        pygame.K_RETURN,
                        pygame.K_KP_ENTER,
                        pygame.K_SPACE
                    ):
                        if self.select_item():
                            return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for index, item in enumerate(self.menu_items):
                            if self.buttons[item].collidepoint(event.pos):
                                self.selected_index = index

                                if self.select_item():
                                    return

            mouse_pos = pygame.mouse.get_pos()

            for index, item in enumerate(self.menu_items):
                if self.buttons[item].collidepoint(mouse_pos):
                    self.selected_index = index

            # Отрисовка меню
            System.screen.fill((0, 0, 0))

            System.screen.blit(
                self.title,
                self.title.get_rect(
                    center=(System.screen_width // 2, 120)
                )
            )

            for index, item in enumerate(self.menu_items):
                button = self.buttons[item]
                color = self.button_colors[item]

                # Подсветка выбранного пункта
                if index == self.selected_index:
                    color = self.adjust_color(color, 40)
                    pygame.draw.rect(
                        System.screen,
                        (0, 255, 125),
                        button.inflate(6, 6),
                        2
                    )

                pygame.draw.rect(System.screen, color, button)

                text = {
                    MenuItems.START_GAME: self.start_text,
                    MenuItems.OPTIONS: self.option_text,
                    MenuItems.EXIT: self.exit_text
                }[item]

                System.screen.blit(
                    text,
                    text.get_rect(center=button.center)
                )

            pygame.display.flip()
            System.clock.tick(30)

    def navigate(self, direction):
        """Переключает выбранный пункт меню."""

        if direction == "up":
            self.selected_index = (
                self.selected_index - 1
            ) % len(self.menu_items)

        elif direction == "down":
            self.selected_index = (
                self.selected_index + 1
            ) % len(self.menu_items)

    @staticmethod
    def adjust_color(color, amount):
        """Изменяет яркость цвета, не выходя за диапазон 0–255."""

        return tuple(
            max(0, min(255, channel + amount))
            for channel in color
        )

    def select_item(self):
        """Активирует выбранный пункт меню."""

        selected_item = self.menu_items[self.selected_index]

        if selected_item == MenuItems.START_GAME:
            return True

        elif selected_item == MenuItems.OPTIONS:
            # Здесь можно открыть настройки игры.
            print("Настройки пока не реализованы.")
            return False

        elif selected_item == MenuItems.EXIT:
            pygame.quit()
            raise SystemExit

        return False
