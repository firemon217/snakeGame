
from abc import ABC, abstractmethod


class GameComponent(ABC):
    """Общий интерфейс отдельного объекта и группы объектов."""

    @abstractmethod
    def draw(self, surface):
        pass

class GameGroup(GameComponent):
    """Группа игровых компонентов."""

    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def draw(self, flyweight):
        for component in self.children:
            flyweight.draw(component)
