from abc import ABC, abstractmethod


class DeliveryService(ABC):
    @abstractmethod
    def send(self, locator: str, content: str) -> bool:
        "Send method to be implemented."


class MemoryDeliveryService(DeliveryService):
    """Memory Delivery Service"""

    def __init__(self, sent=True):
        self.sent = sent

    def send(self, locator: str, content: str) -> bool:
        return self.sent
