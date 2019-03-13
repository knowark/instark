
class Message:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.recipient_id = attributes['recipient_id']
        self.kind = attributes.get('kind', 'Direct')
        self.backend_id = attributes.get('backend_id', '')
        self.subject = attributes.get('subject', '')
        self.content = attributes['content']
        self.payload = attributes.get('payload', {})
