# Base Class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclasses
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying through the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing on the water 🚤"

# Function using polymorphism
def travel(vehicle: Vehicle):
    print(vehicle.move())

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    travel(v)
