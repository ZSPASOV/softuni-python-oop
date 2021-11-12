from typing import ClassVar # mnogo dobri primeri ot lekciq posledna instanciq sept 2020 Yavor Lulchev

class Time:
    hours: int
    minutes: int
    seconds: int

    max_hours: ClassVar[int] = 23
    max_minutes: ClassVar[int] = 59
    max_seconds: ClassVar[int] = 59

    def __init__(self, hs: int, ms: int, ss: int):
        self.hours = hs
        self.minutes = ms
        self.seconds = ss

    def get_time(self) -> str:
        hh = str(self.hours).zfill(2)
        mm = str(self.minutes).zfill(2)
        ss = str(self.seconds).zfill(2)
        return f'{hh}:{mm}:{ss}'

    def set_time(self, hs, ms, ss) -> None:
        self.hours = hs
        self.minutes = ms
        self.seconds = ss

    def next_second(self) -> str:
        self.seconds = (self.seconds + 1) % (self.max_seconds + 1)
        self.minutes = (self.minutes + int(self.seconds == 0)) % (self.max_minutes + 1) # int(self.seconds == 0)) shte vrushta int ot bool izraz, toest 0 ili 1
        self.hours = (self.hours + int(self.minutes == 0 and self.seconds == 0)) % (self.max_hours + 1)

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
