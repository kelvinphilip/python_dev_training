# Define a tuple of fruits
fruit = ("mango","grape","banana")

# Print the fruits in the tuple
print(f'Fruits in the tuple are {fruit}')

# Try to append a new fruit to the tuple
try:
    fruit.append('berry')
# Catch the exception if any occurs
except Exception as e:
    # Print the exception message
    print(f'This is a tuple which is immutable :: {e}')
    raise NotImplementedError(f'This functionality is not implemented by python')