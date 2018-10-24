
class Message:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.recipient_id = attributes['recipient_id']
        self.kind = attributes['kind']
        self.backend_id = attributes.get('backend_id', '')
        self.content = attributes['content']
