# Calculator using mathematical operators and functions

# defining operators

def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    return x / y

first_number = float(input("Type First number: "))
second_number = float(input("Type Second number: "))

while True:
    operation = input("what operator do you require: addition , subtraction, multiplication, division: ")
    operation = operation.lower()

    if operation in ("addition", "subtraction", "multiplication", "division: "):
        if operation == "addition":
            result = (addition(first_number, second_number))
            print(f"{first_number} + {second_number} = {result}")

        elif operation == "subtraction":
            result = (subtract(first_number, second_number))
            print(f"{first_number} + {second_number} = {result}")

        elif operation == "multiplication":
            result = (multiply(first_number, second_number))
            print(f"{first_number} + {second_number} = {result}")

        elif operation == "division":
            if second_number == 0:
                print("Error, cannot divide by zero")
            else:
                result = (division(first_number, second_number))
                print(f"{first_number} + {second_number} = {result}")

    next_calc = input("Do you require another operator: yes / no ")
    if next_calc == "no":
        print("The process has ended")
        break
    elif next_calc != "yes":
        print("invalid input")
        break
    else:
        first_number = float(input("Type First number: "))
        second_number = float(input("Type Second number: "))




