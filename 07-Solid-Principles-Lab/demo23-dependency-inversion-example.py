class Email:
    def send_email(self):
        pass

# Notification depends on Email
class Notification:
    def __init__(self):
        self._email = Email()

    def promotional_notification(self):
        self._email.send_email()


# Example: Constructor Injection
class IMessageService:
    def send_message(self):
        pass

class Email(IMessageService):
    def send_message(self):
        pass

class Notification:
    def __init__(self, service: IMessageService):
        self._service = service

    def promotional_notification(self):
        self._service.send_message()
