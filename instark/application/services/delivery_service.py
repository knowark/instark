from abc import ABC, abstractmethod


class DeliveryService(ABC):
    @abstractmethod
    def send(self, locator: str, content: str) -> str:
        "Send method to be implemented."


class MemoryDeliveryService(DeliveryService):
    """Memory Delivery Service"""

    def __init__(self, response=''):
        self.response = response

    def send(self, locator: str, content: str) -> str:
        return self.response
