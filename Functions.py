# functions
# allow you to use DRY (Do not repeat yourself)

def print_something():
    print("something has been printed")
print_something()

def print_something(print_string):
    print(print_string)
#
print_something("my name is tom")
print_something(("my surname is spurn"))
#
def greeting(name):
    print("Hello, my name is " + name)

greeting("tom")

# return statement
def addition(int1, int2):
    return int1 + int2

print(addition(2, 3))

# default arguments

def addition(int1=2, int2=2):
    return int1 + int2

print(addition(10, 2))

# multiple arguments, * makes a tuple mutiargs = argument which can't be changed.
def multi_args(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)

multi_args(1, 2, 2, 3, 4, 5, 6)

# Type hints

def greeting(name: str):
    print("Hello, my name is " + name)

def division(denum: int, num: int) -> float:
    return denum / num
print(division(12, 5))

#  this function subtracts two numbers, -> = output
def subtraction(int1: int = 5, int2 =2) -> int:
    return int1 - int2

print(type(subtraction()))

# functions best practices

# 1. Name your methods using lowercase and underscores
# 2. all arguments should be clear in their need and where possible and their expected type
# 3. remember the return statement or your function will return none in most cases
# 4. Keep your functions small as possible, and keep them readable
# 5. Use comments within your methods to help with instructions on how to use them.
# 6. Consider using Type Hints to avoid errors earlier

