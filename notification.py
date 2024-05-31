from abc import ABC, abstractmethod

class NotificationStrategy(ABC):
    @abstractmethod
    def envoyer(self, notification):
        pass


class EmailNotificationStrategy(NotificationStrategy):
    def envoyer(self, notification):
        # Implémentation pour envoyer un email
        print(f"Email envoyé: {notification}")


class SMSNotificationStrategy(NotificationStrategy):
    def envoyer(self, notification):
        # Implémentation pour envoyer un SMS
        print(f"SMS envoyé: {notification}")
