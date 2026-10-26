from snake import SnakeSegmentFlyweight

class SnakeSegmentFactory:
    """Создаёт и повторно использует общие данные сегментов."""

    _flyweights = {}

    @classmethod
    def get_flyweight(cls, surface, color, grid_size, renderer):
        # Ключ учитывает визуальные параметры сегмента и тип отрисовщика.
        key = (color, grid_size, type(renderer))

        if key not in cls._flyweights:
            cls._flyweights[key] = SnakeSegmentFlyweight(
                surface,
                color,
                grid_size,
                renderer
            )

        return cls._flyweights[key]