class SIMCardReaderMixin:
    def send_signal(self):
        pass

    def receive_signal(self):
        pass


class DisplayMixin:
    def show_on_display(self):
        pass


class Smartphone(DisplayMixin, SIMCardReaderMixin):
    pass


class Tablet(DisplayMixin):
    pass