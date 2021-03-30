"""
x Create a class named Vehicle, use the __init__() function to assign values for make, model, color, year, velocity and no_of_wheels.
x Velocity should always be set to 0.
x Let no_of_wheels be optional when creating an object by setting the default value 4 for the appropriate __init__() parameter.
x Create a couple of vehicles and print out their properties.

x Add the max_speed property to the Vehicle class.
x Create the methods accelerate() and decelerate() that both take a change parameter and increases / decreases the velocity.
x Check the parameter. The new speed can’t be lower than 0 or higher than the max speed.
x Create a class named Car and let it inherit from Vehicle. The max_speed should always be 160.
x Create a class named Truck and let it inherit from Vehicle.
x The max_speed should always be 80.
x Add the property load_capacity.
x Create a couple of cars and trucks and print out their properties.
x Create the method print() that prints out the properties for the vehicle.
Create the class Motorcycle that inherits from Vehicle. Max speed is 200.
"""


class Vehicle:
    def __init__(self, make, model, color, year, max_speed=100, no_of_wheels=4):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.velocity = 0
        self.no_of_wheels = no_of_wheels
        self.max_speed = max_speed

    def accelerate(self, speed_change):
        if self.velocity + speed_change > self.max_speed:
            self.velocity = self.max_speed
        else:
            self.velocity += speed_change

    def decelerate(self, speed_change):
        if self.velocity - speed_change < 0:
            self.velocity = 0
        else:
            self.velocity -= speed_change

    def print(self):
        print("make:", self.make)
        print("model:", self.model)
        print("color:", self.color)
        print("year:", self.year)
        print("velocity:", self.velocity)
        print("max_speed:", self.max_speed)
        print("no_of_wheels:", self.no_of_wheels)


class Car(Vehicle):
    def __init__(self, make, model, color, year, no_of_wheels=4):
        max_speed = 160
        super().__init__(make, model, color, year, max_speed, no_of_wheels)


class Motorcycle(Vehicle):
    def __init__(self, make, model, color, year, no_of_wheels=2):
        max_speed = 200
        super().__init__(make, model, color, year, max_speed, no_of_wheels)


class Truck(Vehicle):
    def __init__(self, make, model, color, year, load_capacity=2, no_of_wheels=6):
        max_speed = 80
        super().__init__(make, model, color, year, max_speed, no_of_wheels)
        self.load_capacity = load_capacity

    def print(self):
        super().print()
        print("load_capacity:", self.load_capacity)


car1 = Car("Volvo", "V70", "red", 2020)

car1.print()

truck1 = Truck("Scania", "some model", "blue", 2018, 6, 8)

truck1.print()

mc1 = Motorcycle("Triumph", "Trophy", "green", 1995)

mc1.print()


"""
car1.accelerate(95)
print(car1.velocity)

car1.accelerate(10)
print(car1.velocity)

car1.decelerate(15)
print(car1.velocity)

car1.decelerate(100)
print(car1.velocity)
"""
