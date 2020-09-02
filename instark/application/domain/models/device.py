import time
from typing import List
from modelark import Entity


class Device(Entity):
    def __init__(self, **attributes) -> None:
        super().__init__(**attributes)
        self.name = attributes.get('name', '')
        self.locator = attributes.get('locator', '')
