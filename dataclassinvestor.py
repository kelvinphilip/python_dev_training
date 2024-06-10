from dataclasses import dataclass, field

@dataclass(order=True)
class Investor:
    cash : int 
    name: str
    accredited : bool = field(repr=False)
    
    # sort_index: int = field(init=False, repr=False)
    

    def __repr__(self):
        return f"Depositor Name: {self.name}, Accredited Investor: {self.accredited}, Amount deposited: {self.cash}"
    
    # def __post_init__(self):
        # self.sort_index = self.cash

i1 = Investor(cash=50000 , name="Kelvin", accredited=True)
i3 = Investor(cash=4500 , name="Kash", accredited=True)

print(i1 > i3)
print(i1 < i3)
