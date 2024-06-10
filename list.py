fruits = ["apple", "mango", "banana", "grapes"]
count = len(fruits)
last_fruit = fruits[-1]
first_fruit = fruits[0]
print("The number of furits in the list is" , count)
print("The last fruit in the list is", last_fruit)
print("The first fruit in the list is", first_fruit)
print(fruits[0:3]) #same thing as the code below
print(fruits[:-1])

for index,fruit in enumerate(fruits):
    print(f'Fruit at {index} = {fruit}')

index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1

binary_list = [0,1,0,1,1,0,1,0] #0x5A
count_of_one = binary_list.count(1)
count_of_zero = binary_list.count(0)
any_true = any(binary_list)
all_true = all(binary_list)
print(f'The total count of 1s in the list is {count_of_one}')
print(f'The total count of 0s in the list is {count_of_zero}')
print(f'One present in the list =  {any_true}')
print(f'All one present in the list =  {all_true}')







