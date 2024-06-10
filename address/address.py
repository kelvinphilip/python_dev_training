from datetime import datetime
from distancecalculator import DistanceCalculator
from .country import Country

class Address:
    def __init__(self, housenumber:int , street:str, city:str, postalcode:str, country:Country=Country.CANADA):
        self.house = housenumber
        self.street = street
        self.city = city 
        self.postal = postalcode
        self.country = country
        self.created = datetime.now()
    
    def __str__(self):
        return f"{self.house} {self.street} {self.city} {self.postal} {self.country.name}"
    
    def distance(self, origin) -> int:
        d = DistanceCalculator(origin = origin, destination= self.__str__())
        return d.get_distance()