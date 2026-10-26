from abc import ABC, abstractmethod

class GameObjectCreator(ABC):
    """Базовый создатель игровых объектов."""

    @abstractmethod
    def factory_method(self, renderer=None):
        """Создаёт игровой объект."""
        pass

    def create(self, renderer=None):
        """Общий метод создания объекта."""
        return self.factory_method(renderer)
