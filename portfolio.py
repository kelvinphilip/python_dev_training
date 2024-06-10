# Import the Address class from the address module
from address import Address
# Import the Investor class from the classinvestor module in the current package
from .classinvestor import Investor

# Define the Portfolio class that inherits from the Investor class
class Portfolio(Investor):
    # Initialize the Portfolio class with name, accreditation status, deposit amount, and address
    def __init__(self, name: str, accredited: bool, deposit: float, address: Address):
        # Call the initializer of the Investor class with the name, accreditation status, deposit amount, and address
        super().__init__(name, accredited, deposit, address)