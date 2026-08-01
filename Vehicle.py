class Vehicle:
    def __init__(self, max_speed, engine_type, car_type, model):
        self.max_speed=max_speed
        self.engine_type=engine_type
        self.car_type=car_type
        self.model=model
    def show_traits(self):
        print("max speed:", self.max_speed)
        print("engine type):", self.engine_type)
        print("car type):", self.car_type)
        print("model):", self.model)
class Car(Vehicle):
    def __init__(self, max_speed, engine_type, car_type, model):
        super().__init__(max_speed, engine_type, car_type, model)
    def show_traits(self):
        super().show_traits()
child = Car("161.093 KMPH", "Permanent Magnet Synchronous Motor (PMSM)", "SUV", " EQA 250+")
child.show_traits()
print("Is Kid a subclass of Vehicle?", issubclass(Car, Vehicle))
