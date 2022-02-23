from unicodedata import name


days_per_week = 7

# variable : data
# function : code


# name is called parameter
def say_hello(name): 
    print('hello')
    print(f'My name is {name}')
    print('Have a good day')

say_hello('Jermaine')
say_hello('Tony')
say_hello('Jaxen')


def times_two(num):
    print(num + 2)

times_two(3)
times_two(5.0)

def multiply(a,b):
    print(a + b)

multiply(5,4)
multiply(6.0, 100)