from .delivery_service import DeliveryService


class MemoryDeliveryService(DeliveryService):
    """Memory Delivery Service"""

    def __init__(self, response=''):
        self.response = response
        self.code = None
        self.locator = None

    def send(self, locator: str, content: str) -> str:
        self.locator = locator
        return self.response

    def broadcast(self, code: str, content: str) -> str:
        self.code = code
        return self.response

    def subscribe(self, code: str, locator: str) -> bool:
        self.code = code
        self.locator = locator
        return True
