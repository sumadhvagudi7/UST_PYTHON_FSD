from abc import ABC, abstractmethod
import logging


# Logging Setup

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# Abstract Class

class Notification(ABC):
    """Abstract base class defining the notification interface."""

    @abstractmethod
    def notify_user(self, message: str):
        """Send notification with a given message."""
        pass


# Concrete Classes

class EmailNotification(Notification):
    """Handles email-based notifications."""

    def notify_user(self, message: str):
        print(f"Sending EMAIL: {message}")


class SMSNotification(Notification):
    """Handles SMS-based notifications."""

    def notify_user(self, message: str):
        print(f"Sending SMS: {message}")


class PushNotification(Notification):
    """Handles push-based notifications."""

    def notify_user(self, message: str):
        print(f"Sending PUSH Notification: {message}")


# Extendable New Type
class SlackNotification(Notification):
    """Handles Slack-based notifications."""

    def notify_user(self, message: str):
        print(f"Sending SLACK message: {message}")



# Factory Class

class NotificationFactory:
    """Factory class to create appropriate Notification objects."""

    @staticmethod
    def get_notification(channel_type: str) -> Notification:
        """Return an instance of the requested notification type."""
        channel_type = channel_type.lower()
        notification_classes = {
            "email": EmailNotification,
            "sms": SMSNotification,
            "push": PushNotification,
            "slack": SlackNotification,  
        }

        if channel_type not in notification_classes:
            raise ValueError(f"Unknown notification type: {channel_type}")

        selected_class = notification_classes[channel_type]
        logging.info(f"Factory created instance of {selected_class.__name__}")
        return selected_class()



#  Main Function

def main():
    """Simulate user input and send notification."""
    preferred_channel = input("Enter your preferred channel (Email/SMS/Push/Slack): ").strip()
    message = input("Enter your message: ").strip()

    try:
        # Use Factory to get the notification instance
        notification = NotificationFactory.get_notification(preferred_channel)
        # Send notification
        notification.notify_user(message)
    except ValueError as err:
        logging.error(err)


if __name__ == "__main__":
    main()
