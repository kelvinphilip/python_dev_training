# Define a class Vehicle
class Vehicle:
    # Initialize the Vehicle class with a default transmission type
    def __init__(self, transmisison="automatic") -> None:
        self.transmission = transmisison

# Define a class Car that inherits from Vehicle
class Car(Vehicle):
    # Initialize the Car class with brand, type, and wheels
    def __init__(self, brand, type, wheels)  -> None:
        # Call the parent class's __init__ method
        super().__init__()
        self.brand = brand
        self.type = type 
        self.wheels = wheels

# Define a class Cycle that inherits from Vehicle
class Cycle(Vehicle):
    # Initialize the Cycle class with a default transmission type
    def __init__(self, transmisison="manual") -> None:
        # Call the parent class's __init__ method with the transmission type
        super().__init__(transmisison = transmisison)

# Create an instance of the Car class
hondacrv = Car(brand="honda",type="car",wheels=4)

# Create an instance of the Cycle class
herocycle = Cycle()

# Print the Car instance
print(hondacrv)

# Print the brand of the Car instance
print(hondacrv.brand)

# Print the type of the Car instance
print(hondacrv.type)

# Print the number of wheels of the Car instance
print(hondacrv.wheels)

# Print the transmission type of the Car instance
print(hondacrv.transmission)

# Print the transmission type of the Cycle instance
print(herocycle.transmission)