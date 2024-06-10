fruit = ("mango","grape","banana")
print(f'Fruits in the tuple are {fruit}')
try:
    fruit.append('berry')
except Exception as e:
    print(f'This is a tuple which is immutable:: {e}')

