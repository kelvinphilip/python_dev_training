class Investment:
    # ...

    # Define a property for profit and loss
    @property
    def pnl(self) -> int:
        # Calculate the profit and loss
        self.__pnls = (self.fund.value - self.baseprice) * self.quantity
        # Return the profit and loss
        return self.__pnls
    
    # Define a property for the value of the investment
    @property
    def value(self) -> int:
        # Calculate the value of the investment
        self.__value = self.fund.value * self.quantity
        # Return the value of the investment
        return self.__value

class Portfolio:
    # Define some class variables
    investStr = ""
    investments = []
    __totalAssetValue = 0 
    __totalPnlValue = 0 

    # Define the string representation of the Portfolio class
    def __str__(self):
        # If there are investments in the portfolio
        if len(self.investments):
            # Add some information to the string
            self.investStr += f"\nThis is the Portfolio\n"
            self.investStr += f"---------------------\n"
            # For each investment in the portfolio
            for index,investment in enumerate(self.investments):
                # Add the investment to the string
                self.investStr += (f"Investment {index+1}\n{investment}\n")
            # Add the total value and profit and loss of the portfolio to the string
            self.investStr += f"Total value of the portfolio {self.totalValue}\n"
            self.investStr += f"Total pnl value of the portfolio {self.totalPnl}\n"
        # If there are no investments in the portfolio
        else:
            # Add a message to the string
            self.investStr += f"\nEmpty Portfolio, Please add Investments"
        # Return the string
        return self.investStr
    
    # Define a method to add an investment to the portfolio
    def addinvestment(self, investment:Investment, currentbalance:int) -> int:
        # Calculate the new balance
        newbalance = currentbalance - investment.value
        # Add the investment to the portfolio
        self.investments.append(investment)
        # Return the new balance
        return newbalance

    # Define a method to remove an investment from the portfolio
    def removeinvestment(self, investment:Investment) -> int:
        # Remove the investment from the portfolio
        self.investments.remove(investment)
        # Return the investments in the portfolio
        return self.investments
    
    # Define a property for the total value of the portfolio
    @property
    def totalValue(self) -> int:
        # For each investment in the portfolio
        for investment in self.investments:
            # Add the value of the investment to the total value
            self.__totalAssetValue += investment.value
        # Return the total value
        return self.__totalAssetValue
    
    # Define a property for the total profit and loss of the portfolio
    @property
    def totalPnl(self) -> int:
        # For each investment in the portfolio
        for investment in self.investments:
            # Add the profit and loss of the investment to the total profit and loss
            self.__totalPnlValue += investment.pnl
        # Return the total profit and loss
        return self.__totalPnlValue