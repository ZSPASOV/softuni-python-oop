# vmesto mixins moje da se polzva kompoziciq
class SIMCardReader:
    def send_signal(self):
        pass

    def receive_signal(self):
        pass


class Display:
    def show_on_display(self):
        pass


class Smartphone:
    def __init__(self):
        self.sim_reader = SIMCardReader()
        self.display = Display()


class Tablet(DisplayMixin):
    def __init__(self):
        self.display = Display()