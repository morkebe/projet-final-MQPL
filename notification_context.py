class NotificationContext:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def notifier(self, message, destinataire):
        notification = f"Notification à {destinataire}: {message}"
        self.strategy.envoyer(notification)
