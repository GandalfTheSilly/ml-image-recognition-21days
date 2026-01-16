def get_username():
    usr_name = input("Enter your name, please: ")
    
    while usr_name.isspace() == True or usr_name == "":
        print("You have to enter a name")
        usr_name = input("Enter your name, please: ")
    
    return usr_name
    

def get_valid_age():
    age = input("Enter your age, please: ")

    while age == "" or age.isspace() == True or age.isdigit() == False:
        age = input(f"{age} is not a valid. Please enter valid age: ")

    age = int(age)

    while age <= 0:
        age = input(f"{age} is not a valid. Please enter valid age: ")

        while age == "" or age.isspace() == True or age.isdigit() == False:
            age = input(f"{age} is not a valid. Please enter valid age: ")

        age = int(age)

    return age

name = get_username()
age = get_valid_age()

if age >= 18:
    print(f"Thanks {name}, you are classified as: adult!")
else:
    print(f"Thanks {name}, you are classified as: minor")