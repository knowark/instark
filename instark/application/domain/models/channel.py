from modelark import Entity


class Channel(Entity):
    def __init__(self, **attributes) -> None:
        super().__init__(**attributes)
        self.name = attributes.get('name', '')
        self.code = attributes.get('code', '')
