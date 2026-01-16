print('Day 1 Done!')

usr_name = input("Enter a username, please: ")
age = input("Enter your age, please: ")

while age.isdigit() == False:
    print(f"""{age} is not a valid age.
          Enter a valid one: """)
    age = input("Enter your age, please: ")
else:
    age = int(age)
    if age >= 18:
        print(f"{usr_name} is an adult!")
    else:
        print(f"{usr_name} is a minor!")
