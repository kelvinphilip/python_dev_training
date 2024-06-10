class DistanceCalculator:
    def __init__(self, origin:str, destination:str):
        self.origin = origin
        self.destination = destination
        self.__distance = 0 # acts like a private variable
    
    def get_distance(self) -> int:
        self.__distance = 50
        print(f"origin = {self.origin}\ndestination = {self.destination}\ndistance between origin and destination = {self.__distance}")
        return self.__distance
        
        