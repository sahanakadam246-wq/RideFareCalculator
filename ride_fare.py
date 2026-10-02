class Vehicle:
    def __init__(self, driver, base_fare):
        self.driver = driver
        self.__base_fare = base_fare

    # Setter - Encapsulation
    def set_base_fare(self, value):
        if value < 0:
            print("Base fare cannot be negative. Setting it to 0.")
            self.__base_fare = 0
        else:
            self.__base_fare = value

    # Getter
    def get_base_fare(self):
        return self.__base_fare

    # Method to be overridden
    def rate_per_km(self):
        return 0

    # Calculate total fare
    def fare(self, distance):
        return self.__base_fare + (distance * self.rate_per_km())

    # String representation
    def __str__(self):
        return f"{self.__class__.__name__} driven by {self.driver}"


# Child class: Bike
class Bike(Vehicle):
    def __init__(self, driver):
        super().__init__(driver, 10)

    def rate_per_km(self):
        return 5


# Child class: Sedan
class Sedan(Vehicle):
    def __init__(self, driver):
        super().__init__(driver, 50)

    def rate_per_km(self):
        return 15


# Child class: Auto
class Auto(Vehicle):
    def __init__(self, driver):
        super().__init__(driver, 25)

    def rate_per_km(self):
        return 9


# Create objects
bike = Bike("Ramesh")
sedan = Sedan("Priya")
auto = Auto("Suresh")

# Store objects in a list
vehicles = [bike, sedan, auto]

# Trip distance
distance = 8

# Display fares
print(f"Fares for a {distance} km trip:\n")

for vehicle in vehicles:
    print(f"{vehicle} -> ₹{vehicle.fare(distance)}")