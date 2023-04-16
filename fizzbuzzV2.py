def fizzbuzz(number):
    # using the modulus operator to factor in the multiples of 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        return fizzbuzz
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)

# defining fizzbuzz with an argument n which is an empty variable
def print_fizzbuzz(n):
    # using range to and adding one to it to the desired amount of number entered in line 18
    for num in range(1, n+1):
        print(fizzbuzz(num))
# print the maximum number to which fizzbuzz will go up too
print_fizzbuzz(300)

