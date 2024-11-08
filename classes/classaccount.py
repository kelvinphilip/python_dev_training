# Import necessary classes from other modules
from classinvestment import Portfolio, Investment, MarketFund, InvestmentType
from classinvestor import Investor
from address import Address,Country

# Define some MarketFund instances
NVIDIA = MarketFund(name="NVIDIA", value=380, type=InvestmentType.STOCK)
AMD = MarketFund(name="AMD", value=300, type=InvestmentType.STOCK)
HOUSE = MarketFund(name="BEACHHOUSE", value=450000, type=InvestmentType.REALESTATE)
BITCOIN = MarketFund(name="BITCOIN", value=23000, type=InvestmentType.CRYPTO)
GIC = MarketFund(name="GIC", value=100, type=InvestmentType.BONDS)


# Define the Account class
class Account:
    # Declare private variables for investor and portfolio
    __investor: Investor
    __portfolio: Portfolio

    # Initialize the Account class with an investor and a portfolio
    def __init__(self, investor:Investor, portfolio:Portfolio) -> None:
        self.__investor = investor
        self.__portfolio = portfolio

    # Define the string representation of the Account class
    def __str__(self) -> str:
        return self.__investor.__str__() + self.__portfolio.__str__()

    # Define a method to make an investment
    def makeInvestment(self, investment:Investment):
        newbalance = self.__portfolio.addinvestment(investment=investment, currentbalance=self.__investor.balance)
        self.__investor.balance = newbalance


# Define the address, investor, portfolio, and account for investor 1
INVESTOR1_ADDRESS = Address(housenumber=340, street="Red Maple Drive", city="Mississauga", postalcode="L5A-1C5")
INVESTOR1 = Investor(name='INVESTOR1', accredited='false', balance=50000, address=INVESTOR1_ADDRESS) 
INVESTOR1_PORTFOLIO = Portfolio()
INVESTOR1_ACCOUNT = Account(investor=INVESTOR1, portfolio=INVESTOR1_PORTFOLIO)   

# Make an investment for investor 1
AMD_INVESTMENT = Investment(fund=AMD, quantity= 2)
INVESTOR1_ACCOUNT.makeInvestment(investment=AMD_INVESTMENT)

# Define the address, investor, portfolio, and account for investor 2
INVESTOR2_ADDRESS = Address(housenumber=345, street="Lincoln Drive", city="Washington", postalcode="55601", country=Country.USA)
INVESTOR2 = Investor(name='INVESTOR2', accredited='true', balance=500, address=INVESTOR2_ADDRESS)
INVESTOR2_PORTFOLIO = Portfolio()
INVESTOR2_ACCOUNT = Account(investor=INVESTOR2,portfolio=INVESTOR2_PORTFOLIO)

# Print the account details for investor 1
print(INVESTOR1_ACCOUNT)

# Print the account details for investor 2
print(INVESTOR2_ACCOUNT)