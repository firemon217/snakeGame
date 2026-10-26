from apple import Apple
from .game_object_factory import GameObjectCreator

class AppleCreator(GameObjectCreator):
    """Создатель обычных яблок."""

    def factory_method(self, renderer=None):
        return Apple(renderer)