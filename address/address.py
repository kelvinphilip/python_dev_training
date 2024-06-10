# Import the datetime class from the datetime module
from datetime import datetime
# Import the DistanceCalculator class from the distancecalculator module
from distancecalculator import DistanceCalculator
# Import the Country class from the country module in the current package
from .country import Country

# Define the Address class
class Address:
    # Initialize the Address class with house number, street, city, postal code, and country
    def __init__(self, housenumber:int , street:str, city:str, postalcode:str, country:Country=Country.CANADA):
        self.house = housenumber  # The house number of the address
        self.street = street  # The street of the address
        self.city = city  # The city of the address
        self.postal = postalcode  # The postal code of the address
        self.country = country  # The country of the address, default is Canada
        self.created = datetime.now()  # The date and time when the address was created

    # Define the string representation of the Address class
    def __str__(self):
        # Return a string that includes the house number, street, city, postal code, and country name of the address
        return f"{self.house} {self.street} {self.city} {self.postal} {self.country.name}"

    # Define a method to calculate the distance from the address to an origin
    def distance(self, origin) -> int:
        # Create a DistanceCalculator with the origin and destination
        d = DistanceCalculator(origin = origin, destination= self.__str__())
        # Return the distance from the origin to the destination
        return d.get_distance()