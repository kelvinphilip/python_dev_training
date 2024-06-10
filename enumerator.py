from enum import Enum

class CarManufacturer(Enum):
    HONDA = 1
    TOYOTA = 2 
    LAMBORGHINI = 3

print(type(CarManufacturer.HONDA))
print(f'name is {CarManufacturer.HONDA.name} and value is {CarManufacturer.HONDA.value}')
print(f'name is {type(CarManufacturer.HONDA.name)} and value is {type(CarManufacturer.HONDA.value)}')


carmanufacturer = {
    "HONDA": 1,
    "TOYOTA" : 2,
    "LAMBORGHINI" : 3,
}
print(carmanufacturer)
print(f'name is {"HONDA"} and value is {carmanufacturer["HONDA"]}')