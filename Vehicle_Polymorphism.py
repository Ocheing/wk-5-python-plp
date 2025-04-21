# Base class - Vehicle
class Vehicle:
    def move(self):
        pass

# Car class
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Bike class
class Bike(Vehicle):
    def move(self):
        print("Cycling 🚲")

# Create objects
car = Car()
plane = Plane()
bike = Bike()

# Demonstrate polymorphism
vehicles = [car, plane, bike]

for vehicle in vehicles:
    vehicle.move()  
