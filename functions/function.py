def greet(name):
    print(f'Hello, {name}!')

def get_full_name(*, first_name, last_name, middle_name='UNKNOWN'):
    fullname = first_name + ' ' + middle_name + ' ' + last_name
    print(fullname)
    return fullname

fullname = get_full_name(last_name='Doe', first_name='John')  # 'John Doe'
greet(fullname)

fullname = get_full_name(last_name='Smith', first_name='Dave', middle_name='Christopher') # 'Dave Christopher Smith'
greet(fullname)