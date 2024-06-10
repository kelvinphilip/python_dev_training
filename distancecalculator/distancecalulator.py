# Define the DistanceCalculator class
class DistanceCalculator:
    # Initialize the DistanceCalculator class with origin and destination
    def __init__(self, origin:str, destination:str):
        self.origin = origin  # The starting point for the distance calculation
        self.destination = destination  # The ending point for the distance calculation
        self.__distance = 0  # The distance between the origin and destination, initialized to 0

    # Define a method to get the distance between the origin and destination
    def get_distance(self) -> int:
        self.__distance = 50  # Set the distance to 50 for the purpose of this example
        # Print the origin, destination, and distance
        print(f"origin = {self.origin}\ndestination = {self.destination}\ndistance between origin and destination = {self.__distance}")
        return self.__distance  # Return the distance