<h1>Basic Calculator</h1>
<h2>Using Maths Operators</h2>

<h5>Defining Functions</h5>

<strong>Using define function to give the desirable outcome using basic operators.
</strong>.

    def addition (x, y):
    return x + y

    def subtract (x, y):
    return x - y

    def multiply (x, y):
    return x * y

    def division (x, y):
    return x / y

<strong>Asks the user to input the numbers as a float or an integer to be used within the chosen operators</strong>.

    first_number = float(input("Type First number: "))

    second_number = float(input("Type Second number: "))

<strong>Using a While Loop indicates the loops run until it breaks</strong>.
<strong>Prompts the user to enter the desirable operator, whilst being in lower.case</strong>.
    
    while True:

        operation = input("what operator do you require: addition , subtraction, multiplication, division: ")
    
        operation = operation.lower()

<strong>if statement is used to classify each operator, using the result variable, thus a "f" string to concatenante the variables and print the result </strong>.

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

<strong>Since no modulus has been used we define division not be divided by 0, since it will give no value</strong>.

        elif operation == "division":
            if second_number == 0:
                print("Error, cannot divide by zero")
            else:
                result = (division(first_number, second_number))
                print(f"{first_number} + {second_number} = {result}")

<strong>The loop is broken by "break", and if new set of numbers are used, asks the user to input numbers again</strong>.

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