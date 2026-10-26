from apple import Apple, GoldenApple
from .game_object_factory import GameObjectCreator


class GoldenAppleCreator(GameObjectCreator):
    """Создатель золотых яблок."""

    def factory_method(self, config=None):
        return GoldenApple(config)

class AppleCreator(GameObjectCreator):
    """Создатель обычных яблок."""

    def factory_method(self, config=None):
        return Apple(config)