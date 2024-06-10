# from enum import Enum
# from datetime import datetime
from distancecalculator import DistanceCalculator
from address import Address, Country


class Investor:
    def __init__(self, name:str, accredited:bool, balance:float, address:Address):
        self.name = name
        self.accredited = accredited
        self.balance= balance
        self.address = address
    
    def __str__(self):
        return f"Depositor Name: {self.name}\nAccredited Investor: {self.accredited}\nCurrent Balance: {self.balance}\nAddress: {self.address}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def distance(self, origin) -> int:
        d = DistanceCalculator(origin = origin, destination= self.address)
        return d.get_distance()
    
if __name__ == "__main__":
    address1 = Address(housenumber=3460, street="Redmond drive", city="Mississauga", postalcode="L5B-4C5")
    address2 = Address(housenumber=3455, street="blue drive", city="Mississauga", postalcode="L5B-5V3", country=Country.USA)
    investor1 = Investor(name='Kashyap', accredited='false', balance=50000, address=address1)
    investor2 = Investor(name='Kelvin', accredited='true', balance=500, address=address2)

    # investor3 = Investor('Kelvin', 'true', 20000)

    investor1.distance(origin="45 cyxtera avenue")
    print(investor1)
    print()
    investor2.distance(origin="1 commerce valley")
    print(investor2)




