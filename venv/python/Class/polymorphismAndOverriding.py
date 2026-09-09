from classAndObject import Car
# Create a parent class Vehicle with __init__(self, make, model) and a method describe(self).
# Create a child class Car that inherits from it, using super() in its own __init__ to add a doors attribute.

class Child_Car(Car):
    def __init__(self, make, model, doorModel, doorColor, doorQETest):
        super().__init__(make, model)
        self.doorModel = doorModel
        self.doorColor = doorColor
        self.doorQETest = doorQETest

    def describe(self, speed=None): #Use speed = None, becuse another describe want speed but this not need, so have to assign None
        print(f'{self.model} {self.make} {self.year} car\'s door {self.doorModel} {self.doorColor} color is {self.doorQETest} in QE test')

car_details = Child_Car("M1", "BMW", "Carbon_Fiber_02", "Shinning_Balck", "PASS")
car_details.describe()

# Create a Motorcycle child class too, and give both Car and Motorcycle their own overridden describe(self) method
# that includes their specific extra attribute.
class Motorcycle(Child_Car):
    def __init__(self, make, model):
        Car.__init__(self, make, model)

    def describe(self, speed=None):
        print(f'This {self.make} {self.model} motor bike top speed is {speed}')

motor_bike = Motorcycle("Triumph", "Speed 400 T4")
DF_car_details = Child_Car("Land Rover", "Defender", "Carbon_Fiber_003", "Grey", "PASS")
motor_bike.describe("165 km/hr")

list1 = [motor_bike, DF_car_details]

for list in list1:
    list.describe("166 km/hr")