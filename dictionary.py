# Define a dictionary with various key-value pairs
thisdict = {
    "brand": "Ford",  # The brand of the car
    "type" : "car",  # The type of vehicle
    "wheels" : 4,  # The number of wheels on the car
    "sold" : False,  # Whether the car has been sold
    "owners" : ["Kelvin", "Kashyap"],  # The owners of the car
    "metadata" : {  # Additional information about the car
        "color" : "red",  # The color of the car
        "transmission" : "auto",  # The type of transmission in the car
        "engine_cc" : 500  # The engine displacement of the car
        }
}

# Iterate over the items in the dictionary
for key,value in thisdict.items():
    # If the value is a dictionary
    if isinstance(value, dict):
        # Iterate over the items in the dictionary
        for k,v in value.items():
            # Print the parent key, child key, and child value
            print(f'parent_key = {key} and child_key = {k}, child_value = {v}')
    # If the value is a list
    elif isinstance(value, list):
        # Iterate over the items in the list
        for v in value:
            # Print the key and child value
             print(f'key = {key} , child_value = {v}')
    # If the value is neither a dictionary nor a list
    else:
        # Print the key and value
        print(f'key = {key} , value = {value}')