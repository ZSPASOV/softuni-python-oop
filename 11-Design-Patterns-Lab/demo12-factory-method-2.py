from abc import ABC, abstractmethod


class Car:
    pass


class BMW(Car):
    pass


class Mercedes(Car):
    pass


class CarFactory:
    def make_bmw(self):
        return BMW()

    def make_mercedes(self):
        return Mercedes()


    @staticmethod
    def make_car_by_brand(brand):
        cars = {
            'bmw': BMW,
            'mercedes': Mercedes,
        }
        return cars[brand]()

print(CarFactory.make_car_by_brand('mercedes')) # <__main__.Mercedes object at 0x000000000060D430>