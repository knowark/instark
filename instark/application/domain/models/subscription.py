from modelark import Entity


class Subscription(Entity):
    def __init__(self, **attributes) -> None:
        super().__init__(**attributes)
        self.device_id = attributes['device_id']
        self.channel_id = attributes['channel_id']
