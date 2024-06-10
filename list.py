# Define a list of fruits
fruits = ["apple", "mango", "banana", "grapes"]

# Calculate the number of fruits in the list
count = len(fruits)

# Get the last fruit in the list
last_fruit = fruits[-1]

# Get the first fruit in the list
first_fruit = fruits[0]

# Print the number of fruits in the list
print("The number of fruits in the list is" , count)

# Print the last fruit in the list
print("The last fruit in the list is", last_fruit)

# Print the first fruit in the list
print("The first fruit in the list is", first_fruit)

# Print the first three fruits in the list
print(fruits[0:3])

# Print all fruits in the list except the last one
print(fruits[:-1])

# Print each fruit in the list along with its index
for index,fruit in enumerate(fruits):
    print(f'Fruit at {index} = {fruit}')

# Another way to print each fruit in the list along with its index
index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1

# Define a list of binary numbers
binary_list = [0,1,0,1,1,0,1,0] #0x5A

# Count the number of 1s in the list
count_of_one = binary_list.count(1)

# Count the number of 0s in the list
count_of_zero = binary_list.count(0)

# Check if there is at least one 1 in the list
any_true = any(binary_list)

# Check if all numbers in the list are 1
all_true = all(binary_list)

# Print the number of 1s in the list
print(f'The total count of 1s in the list is {count_of_one}')

# Print the number of 0s in the list
print(f'The total count of 0s in the list is {count_of_zero}')

# Print whether there is at least one 1 in the list
print(f'One present in the list =  {any_true}')

# Print whether all numbers in the list are 1
print(f'All one present in the list =  {all_true}')