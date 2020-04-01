from abc import ABC, abstractmethod


class DeliveryService(ABC):
    @abstractmethod
    def send(self, locator: str, title: str, content: str) -> str:
        "Send method to be implemented."

    @abstractmethod
    def broadcast(self, code: str, title: str, content: str) -> str:
        "Broadcast to channel method to be implemented."

    @abstractmethod
    def subscribe(self, code: str, locator: str) -> bool:
        "Subscribe device to channel method to be implemented."
