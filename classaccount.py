from classinvestment import Portfolio, Investment, MarketFund, InvestmentType
from classinvestor import Investor
from address import Address,Country


NVIDIA = MarketFund(name="NVIDIA", value=380, type=InvestmentType.STOCK)
AMD = MarketFund(name="AMD", value=300, type=InvestmentType.STOCK)
HOUSE = MarketFund(name="HOUSE", value=450000, type=InvestmentType.REALESTATE)
BITCOIN = MarketFund(name="BITCOIN", value=23000, type=InvestmentType.CRYPTO)
GIC = MarketFund(name="GIC", value=100, type=InvestmentType.BONDS)

class Account:
    __investor: Investor
    __portfolio: Portfolio

    def __init__(self, investor:Investor, portfolio:Portfolio) -> None:
        self.__investor = investor
        self.__portfolio = portfolio

    def __str__(self) -> str:
        return self.__investor.__str__() + self.__portfolio.__str__()
    
    def makeInvestment(self, investment:Investment):
        newbalance = self.__portfolio.addinvestment(investment=investment, currentbalance=self.__investor.balance)
        self.__investor.balance = newbalance

KASHYAP_ADDRESS = Address(housenumber=3460, street="Redmond drive", city="Mississauga", postalcode="L5B-4C5")
KASHYAP = Investor(name='Kashyap', accredited='false', balance=50000, address=KASHYAP_ADDRESS) 
KASHYAP_PORTFOLIO = Portfolio()
KASHYAP_ACCOUNT = Account(investor=KASHYAP, portfolio=KASHYAP_PORTFOLIO)   

AMD_INVESTMENT = Investment(fund=AMD, quantity= 2)
KASHYAP_ACCOUNT.makeInvestment(investment=AMD_INVESTMENT)

KELVIN_ADDRESS = Address(housenumber=3455, street="blue drive", city="Mississauga", postalcode="L5B-5V3", country=Country.USA)
KELVIN = Investor(name='Kelvin', accredited='true', balance=500, address=KELVIN_ADDRESS)
KELVIN_PORTFOLIO = Portfolio()
KELVIN_ACCOUNT = Account(investor=KELVIN,portfolio=KELVIN_PORTFOLIO)

print(KASHYAP_ACCOUNT)

