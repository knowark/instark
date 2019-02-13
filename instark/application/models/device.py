from .locator import Locator


class Device:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.name = attributes.get('name', '')
        self.locator_id = attributes['locator_id']
