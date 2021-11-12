# v1
class SIMCardReaderMixin:
    def make_call_through_sim(self):
        pass


class DisplayMixin:
    def show_on_display(self):
        pass


class Tablet(DisplayMixin):
    def make_call_through_sim(self):
        pass


class SmartPhone(DisplayMixin, SIMCardReaderMixin):
    pass

# v2
# Jambazov ne e mnogo fen na na4ina gore, po dobre da se polzva composition vmesto mix-ins po sledniq na4in:

class Device:
    pass


class Tablet(Device):
    def __init__(self):
        self.display = Display()


class SmartPhone(Device):
    def __init__(self):
        self.display = Display()
        self.sim_card = SIMCardReader()


