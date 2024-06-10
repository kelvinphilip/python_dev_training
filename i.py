class Investor:
    listOfInvestors = []
    listofCapital = []
    numberOfInvestors = 20
    
    if numberOfInvestors > 0:
        inp = input("Please enter your name: ")
        numberOfInvestors -=1 
        listOfInvestors.append(inp)
        inp = input("Please enter the amount of money you want to deposit: ")
        listofCapital.append(inp)
      
    @property
    def getInvestors(self) -> str:
        index = 0 
        for l in self.listOfInvestors:
            f"investor {index} : {l[index]}"
            index += 1
            return
    
inv = Investor()
inv.getInvestors




