from address import Address
from .classinvestor import Investor

class Portfolio(Investor):

    def __init__(self, name: str, accredited: bool, deposit: float, address: Address , ):
        super().__init__(name, accredited, deposit, address)
