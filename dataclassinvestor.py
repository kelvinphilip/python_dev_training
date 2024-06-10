# Import necessary classes from the dataclasses module
from dataclasses import dataclass, field

# Define the Investor class as a dataclass
@dataclass(order=True)
class Investor:
    # Define the properties of the Investor class
    cash : int  # The amount of cash the investor has
    name: str  # The name of the investor
    accredited : bool = field(repr=False)  # Whether the investor is accredited, not included in the string representation of the class
    
    # Define the string representation of the Investor class
    def __repr__(self):
        # Return a string that includes the name, accreditation status, and cash of the investor
        return f"Depositor Name: {self.name}, Accredited Investor: {self.accredited}, Amount deposited: {self.cash}"

# Create two instances of the Investor class
i1 = Investor(cash=50000 , name="Kelvin", accredited=True)  # An investor named Kelvin who is accredited and has 50000 cash
i3 = Investor(cash=4500 , name="Kash", accredited=True)  # An investor named Kash who is accredited and has 4500 cash

# Print whether Kelvin has more cash than Kash
print(i1 > i3)  # True if Kelvin has more cash than Kash, False otherwise

# Print whether Kelvin has less cash than Kash
print(i1 < i3)  # True if Kelvin has less cash than Kash, False otherwise