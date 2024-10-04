class Vehicle:
    numOfWheels = 4
    def __init__(self):
        pass

class Truck(Vehicle):
    def __init__(self):
        pass

ford = Truck()
print(ford.numOfWheels)