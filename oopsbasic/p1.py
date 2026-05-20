class Car:
    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    
    def accelerate(self,increment):
        self.speed += increment
    
    def brake(self,decrement):
        self.speed -= decrement

car = Car("BMW","M3",180)
print(f"Brand: {car.brand}")
print(f"Model: {car.model}")
print(f"Speed: {car.speed}")

car.accelerate(50)
print(f"Car's speed after accelerating {car.speed}")

car.brake(30)
print(f"Car's speed after braking {car.speed}")