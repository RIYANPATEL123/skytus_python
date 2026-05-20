class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        print("Car starting")

class ElectricCar(Car):
    def start(self):
        print("Electric car starting")

v = Vehicle()
v.start()
c = Car()
c.start()
e = ElectricCar()
e.start()