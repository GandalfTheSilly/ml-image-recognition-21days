print("""
      -----------------------------
      
      Welcome to Calculator CLI!
      
      -----------------------------
      """)


def get_number():
    try:
        a = float(input("Please enter your first number: "))
        b = float(input("Please enter your second number: "))

        nmbr_validation = input(
            f"The number you've entered: First one is {a} and Second one is {b}. Are you certain ? (y/n) "
        )

        if nmbr_validation == "y":
            return a, b
        else:
            print("""You've enter unknow answer.
System reloading...""")
            return get_number()

    except ValueError:
        print("""You've entered something besides a number.
Please try again.
System reloading...
              """)
        return get_number()


def get_operation():
    op = input("What operation would like to do ? (+,-,*,/) ")

    if op == "+" or op == "-" or op == "*" or op == "/":
        return op
    else:
        print("""You've enter unknow operation.
System reloading...""")
        return get_operation()


def calculate(a, b, op):
    try:
        match op:
            case "+":
                result = a + b
            case "-":
                result = a - b
            case "*":
                result = a * b
            case "/":
                result = a / b

        print(f"Result is {result}")

    except ZeroDivisionError:
        print('You cannot divide something with "0"')
        


a, b = get_number()
op = get_operation()
calculate(a, b, op)

c = input("Do you want another calculation? (y/n) ")
while c == "y":
    a, b = get_number()
    op = get_operation()
    calculate(a, b, op)
    c = input("Do you want another calculation? (y/n) ")
else:
    print("Well done! Thanks for using the calculator. Goodbye!")
