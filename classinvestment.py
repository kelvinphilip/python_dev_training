from enum import Enum
from datetime import datetime
import random

class InvestmentType(Enum):
    CRYPTO = "crypto"
    STOCK = "stock"
    BONDS = "bonds"
    REALESTATE = "real estate" 

class MarketFund:
    name:str 
    value:int 
    type:InvestmentType

    def __init__(self, name:str, value:int, type:InvestmentType) -> None:
        self.name = name
        self.value = value 
        self.type = type

class Market:
    open:bool = False
    marketStr = ""
    funds:list = []
    
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        self.simulateMarket()
        self.marketStr += f"\nWelcome to the Market\n"
        self.marketStr += f"---------------------\n"
        for index,fund in enumerate(self.funds):
            self.marketStr += (f"\nFund {index+1}\nName {fund.name}\nValue {fund.value}\n")
        return self.marketStr

    @property
    def isOpen(self) -> bool:
        currentDatetime = datetime.now()
        today9am = currentDatetime.replace(hour=9, minute=0, second=0, microsecond=0)
        today5pm = currentDatetime.replace(hour=17, minute=0, second=0, microsecond=0)
        self.open = today9am < currentDatetime < today5pm
        return self.open
    
    
    def addFund(self, fund:MarketFund) -> int:
        self.funds.append(fund)
        return self.funds
    
    def removeFund(self, fund:MarketFund) -> int:
        self.funds.remove(fund)
        return self.funds
    
    def modifyFund(self, fund:MarketFund, newvalue:int):
        for f in self.funds:
            if f.name == fund.name:
                f.value = int(newvalue)
                break
    
    def simulateMarket(self):
        if self.isOpen:
            for fund in self.funds:
                multiplier = random.randint(0,200)
                self.modifyFund(fund=fund, newvalue = fund.value * (multiplier / 100))
    
   
class Investment:
    __pnls = 0 # private variable in python
    __value = 0

    def __init__(self, fund:MarketFund, quantity:int = 0) -> None:
       self.fund = fund
       self.type = self.fund.type
       self.baseprice = self.fund.value
       self.quantity = quantity
       self.purchasedate = datetime.now()

    def __str__(self):
        return f"Investment type: {self.type}\nbase price of the investment: {self.baseprice}\nNumber of quantities purchased: {self.quantity}\nDate and time of purchase: {self.purchasedate}\nvalue of this investment {self.value}\n"

    @property
    def pnl(self) -> int:
        self.__pnls = (self.fund.value - self.baseprice) * self.quantity
        return self.__pnls
    
    @property
    def value(self) -> int:
        self.__value = self.fund.value * self.quantity
        return self.__value

   
class Portfolio:
    investStr = ""
    investments = []
    __totalAssetValue = 0 
    __totalPnlValue = 0 


    def __str__(self):
        if len(self.investments):
            self.investStr += f"\nThis is the Portfolio\n"
            self.investStr += f"---------------------\n"
            for index,investment in enumerate(self.investments):
                self.investStr += (f"Investment {index+1}\n{investment}\n")
            self.investStr += f"Total value of the portfolio {self.totalValue}\n"
            self.investStr += f"Total pnl value of the portfolio {self.totalPnl}\n"

        else:
            self.investStr += f"\nEmpty Portfolio, Please add Investments"
        return self.investStr
    
 
    def addinvestment(self, investment:Investment, currentbalance:int) -> int:
        newbalance = currentbalance - investment.value
        self.investments.append(investment)
        return newbalance

    def removeinvestment(self, investment:Investment) -> int:
        self.investments.remove(investment)
        return self.investments
    
    @property
    def totalValue(self) -> int:
        for investment in self.investments:
            self.__totalAssetValue += investment.value
        return self.__totalAssetValue
    
    @property
    def totalPnl(self) -> int:
        for investment in self.investments:
            self.__totalPnlValue += investment.pnl
        return self.__totalPnlValue



if __name__ == "__main__":
    firstCryptoInvestment = Investment(type=InvestmentType.CRYPTO , fund=BITCOIN, quantity=2)
    firstStockInvestment = Investment(type=InvestmentType.STOCK, fund=AMD, quantity= 1)
    firstRealEstateInvestment = Investment(type=InvestmentType.REALESTATE, fund=HOUSE, quantity = 1)
    # pnls = firstCryptoInvestment.profitorloss(currentprice=600)
    # print(pnls)
    # print(firstCryptoInvestment.__pnls)
    # pnls = 0
    # print(pnls)
    # print(firstCryptoInvestment.__pnls)

    port = Portfolio()
    market = Market()
    port.addinvestment(investment=firstCryptoInvestment)
    port.addinvestment(investment=firstStockInvestment)
    port.addinvestment(investment=firstRealEstateInvestment)

    port.removeinvestment(investment=firstRealEstateInvestment)


    market.addFund(fund = AMD)
    market.addFund(fund = BITCOIN)

    print(port)
    print(f"The Market is open: {market.isOpen}\n")
    print(market)
    print(port)
