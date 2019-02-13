
class Locator:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.medium = attributes['medium']
        self.type = attributes['type']
        self.reference_id = attributes['reference_id']
