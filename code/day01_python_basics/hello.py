print('Day 1 Done!')

usr_name = input("Enter a username, please: ")
age = input("Enter your age, please: ")

if age.isdigit() == False:
    print(f"""{age} is not a valid name.
          Enter a vallid one: """)
    age = input("Enter your age, please: ")
else:
    age = int(age)
    if age >= 18:
        print(f"{usr_name} is an adult!")
    else:
        print(f"{usr_name} is a minor!")
