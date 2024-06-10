class Investor:
    """
    This class represents an Investor.
    """
    listOfInvestors = []  # List to store the names of the investors
    listofCapital = []  # List to store the capital of the investors
    numberOfInvestors = 20  # Number of investors
    
    # If there are investors, ask for their name and capital
    if numberOfInvestors > 0:
        inp = input("Please enter your name: ")  # Get the name of the investor
        numberOfInvestors -=1  # Decrease the number of investors
        listOfInvestors.append(inp)  # Add the investor to the list
        inp = input("Please enter the amount of money you want to deposit: ")  # Get the capital of the investor
        listofCapital.append(inp)  # Add the capital to the list
      
    @property
    def getInvestors(self) -> str:
        """
        This method returns the list of investors.
        """
        index = 0  # Initialize index
        for l in self.listOfInvestors:  # Loop through the list of investors
            f"investor {index} : {l[index]}"  # Format the output
            index += 1  # Increase the index
            return  # Return the list of investors
    
# Create an instance of the Investor class
inv = Investor()
# Get the list of investors
inv.getInvestors