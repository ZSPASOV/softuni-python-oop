class Car:
    pass


class BMW(Car):
    pass


class Mercedes(Car):
    pass



def simple_car_factory(brand):
    cars = {
        'bmw': BMW,
        'mercedes': Mercedes,
    }
    return cars[brand]()

print(simple_car_factory('mercedes'))