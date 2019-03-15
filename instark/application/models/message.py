
class Message:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.recipient_id = attributes['recipient_id']
        self.kind = attributes.get('kind', 'Direct')
        self.backend_id = attributes.get('backend_id', '')
        self.title = attributes.get('title')
        self.content = attributes['content']
