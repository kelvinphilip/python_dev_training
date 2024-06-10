class Vehicle:
    def __init__(self, transmisison="automatic") -> None:
        self.transmission = transmisison

class Car(Vehicle):
    def __init__(self, brand, type, wheels)  -> None:
        super().__init__()
        self.brand = brand
        self.type = type 
        self.wheels = wheels

class Cycle(Vehicle):
    def __init__(self, transmisison="manual") -> None:
        super().__init__(transmisison = transmisison)


hondacrv = Car(brand="honda",type="car",wheels=4)
herocycle = Cycle()

print(hondacrv)
print(hondacrv.brand)
print(hondacrv.type)
print(hondacrv.wheels)
print(hondacrv.transmission)
print(herocycle.transmission)