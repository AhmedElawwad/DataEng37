class Car:

    def __init__(self, make, model, top_speed):
        self._make = make
        self._model = model
        self._top_speed = top_speed
        self._speed = 0

    def accelerate(self, speed_add):
        self._speed = min(self._speed + speed_add, self._top_speed)

    def brake(self, reduce_speed):
        self._speed = max(self._speed - reduce_speed, 0)

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_speed(self):
        return self._speed


ahmeds_car = Car('Vauxhall', 'insignia', 120)

ahmeds_car.accelerate(120)
ahmeds_car.brake(50)
print(ahmeds_car.get_model())
print(ahmeds_car.get_model())
print(ahmeds_car.get_speed())
ahmeds_car.brake(20)
print(ahmeds_car.get_speed())
