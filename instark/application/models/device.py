from .entity import Entity


class Device(Entity):
    def __init__(self, **attributes) -> None:
        super().__init__(**attributes)
        self.name = attributes.get('name', '')
        self.locator = attributes['locator']
