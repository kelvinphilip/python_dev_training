# Import necessary classes from other modules
from distancecalculator import DistanceCalculator
from address import Address, Country

# Define the Investor class
class Investor:
    # Initialize the Investor class with name, accreditation status, balance, and address
    def __init__(self, name:str, accredited:bool, balance:float, address:Address):
        self.name = name
        self.accredited = accredited
        self.balance= balance
        self.address = address

    # Define the string representation of the Investor class
    def __str__(self):
        return f"Depositor Name: {self.name}\nAccredited Investor: {self.accredited}\nCurrent Balance: {self.balance}\nAddress: {self.address}"

    # Define the equality of two Investor instances
    def __eq__(self, other):
        return self.name == other.name

    # Define a method to calculate the distance from the investor to an origin
    def distance(self, origin) -> int:
        d = DistanceCalculator(origin = origin, destination= self.address)
        return d.get_distance()

# If this script is run as the main program
if __name__ == "__main__":
    # Define two addresses
    address1 = Address(housenumber=3460, street="Redmond drive", city="Mississauga", postalcode="L5B-4C5")
    address2 = Address(housenumber=3455, street="blue drive", city="Mississauga", postalcode="L5B-5V3", country=Country.USA)
    # Define two investors
    investor1 = Investor(name='Kashyap', accredited='false', balance=50000, address=address1)
    investor2 = Investor(name='Kelvin', accredited='true', balance=500, address=address2)
    # Calculate the distance from the investors to an origin
    investor1.distance(origin="45 cyxtera avenue")
    investor2.distance(origin="1 commerce valley")
    # Print the investors
    print(investor1)
    print()
    print(investor2)