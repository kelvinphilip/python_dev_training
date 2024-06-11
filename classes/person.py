class Person:
    def __init__(self, first_name, last_name, age, sin=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sin = sin

    def __str__(self) -> str:
        return f'Person :: First Name={self.first_name} :: Last Name={self.last_name} :: Age={self.age} :: SIN=XXXX-XX-{self.sin[-4:]}'

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def greet(self):
        print(f'Hello, {self.first_name}!')

# Create an instance of the Person class
john_doe = Person(first_name='John', last_name='Doe', age=30, sin='1234-34-7755' )
dave_smith = Person(first_name='Dave', last_name='Smith', age=25)

# Print the full name of the Person instance
john_doe_full_name = john_doe.get_full_name()
print(john_doe_full_name)  # 'John Doe'

print(john_doe)