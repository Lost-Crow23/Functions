# from oop basics
#  FizzBuzz question

# A for loop is used to include the variable, and prints out within a range using the range function.
for fizzbuzz in range(1, 100):
    # this gives a insight if it is either modulus by 3 or 5, it'll still print out fizzbuzz
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    # if modulus by 3, every multiple of 3, fizz will be printed out
    elif fizzbuzz % 3 == 0:
        print("fizz")
    # if modulus by 5, every multiple of 5, buzz will be printed out
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

