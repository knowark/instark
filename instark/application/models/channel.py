
class Channel:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.name = attributes.get('name', '')
        self.code = attributes['code']
