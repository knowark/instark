
class DeviceChannel:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.device_id = attributes['device_id']
        self.channel_id = attributes['channel_id']
