
class RenderProxy:
    """Заместитель, контролирующий отрисовку игрового объекта."""

    def __init__(self, game_object):
        self._game_object = game_object
        self.draw_calls = 0

    def draw(self, surface):
        x, y = self._game_object.position

        # Не отрисовываем объект за пределами игрового поля.
        if (
            x < 0
            or y < 0
            or x >= surface.get_width()
            or y >= surface.get_height()
        ):
            return

        self.draw_calls += 1
        self._game_object.draw(surface)

    def __getattr__(self, name):
        # Остальные атрибуты передаём исходному объекту.
        return getattr(self._game_object, name)
