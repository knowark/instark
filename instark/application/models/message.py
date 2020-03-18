from .entity import Entity


class Message(Entity):
    def __init__(self, **attributes) -> None:
        super().__init__(**attributes)
        self.recipient_id = attributes['recipient_id']
        self.kind = attributes.get('kind', 'direct')
        self.backend_id = attributes.get('backend_id', '')
        self.title = attributes.get('title')
        self.content = attributes['content']
