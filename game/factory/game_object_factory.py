from abc import ABC, abstractmethod

class GameObjectCreator(ABC):
    """Базовый создатель игровых объектов."""

    @abstractmethod
    def factory_method(self, config=None):
        """Создаёт игровой объект."""
        pass

    def create(self, config=None):
        """Общий метод создания объекта."""
        return self.factory_method(config)
