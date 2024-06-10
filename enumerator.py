# Import the Enum class from the enum module
from enum import Enum

# Define the CarManufacturer class as an enumeration
class CarManufacturer(Enum):
    HONDA = 1  # Honda is represented by the number 1
    TOYOTA = 2  # Toyota is represented by the number 2
    LAMBORGHINI = 3  # Lamborghini is represented by the number 3

# Print the type of CarManufacturer.HONDA
print(type(CarManufacturer.HONDA))  # This will print <enum 'CarManufacturer'>

# Print the name and value of CarManufacturer.HONDA
print(f'name is {CarManufacturer.HONDA.name} and value is {CarManufacturer.HONDA.value}')  # This will print "name is HONDA and value is 1"

# Print the types of the name and value of CarManufacturer.HONDA
print(f'name is {type(CarManufacturer.HONDA.name)} and value is {type(CarManufacturer.HONDA.value)}')  # This will print "name is <class 'str'> and value is <class 'int'>"

# Define a dictionary that represents car manufacturers
carmanufacturer = {
    "HONDA": 1,  # Honda is represented by the number 1
    "TOYOTA" : 2,  # Toyota is represented by the number 2
    "LAMBORGHINI" : 3,  # Lamborghini is represented by the number 3
}

# Print the dictionary
print(carmanufacturer)  # This will print {'HONDA': 1, 'TOYOTA': 2, 'LAMBORGHINI': 3}

# Print the name and value of "HONDA"
print(f'name is {"HONDA"} and value is {carmanufacturer["HONDA"]}')  # This will print "name is HONDA and value is 1"