def login(user, passwrd):
    chances = 3
    while chances > 0:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == user and password == passwrd:
            print("Login successful")
            break
        else:
            print("Please try again")
            chances = chances - 1

    if chances == 0:
        print("No more login attempts")


def validation(name, email, phone, address, password):
    if name.isalpha():
        if email.islower() and email.count("@") == 1:
            if email.endswith(".com") or email.endswith(".in"):
                if phone.isdigit():
                    uppercase_count = 0
                    lowercase_count = 0
                    length = 0
                    special_character = True

                    for character in password:
                        length = length + 1

                        if character.isupper():
                            uppercase_count = uppercase_count + 1

                        if character.islower():
                            lowercase_count = lowercase_count + 1

                        if character.isalnum() == False:
                            if character != "_" and character != "#" and character != "@":
                                special_character = False

                    if length >= 8 and uppercase_count >= 1 and lowercase_count >= 1 and special_character == True:
                        username = email.split("@")[0]
                        print("Your username is", username)
                        login(username, password)
                    else:
                        print("Invalid password")
                else:
                    print("Enter only digits for phone number")
            else:
                print("Enter a valid email ID")
        else:
            print("Enter a valid email ID")
    else:
        print("Name should have only alphabets")


def registration():

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    ph = input("Enter your phone no: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")
    retype = input("Enter your password again: ")

    if password == retype:
        validation(name, email, ph, address, password)
    else:
        print("Passwords do not match")
registration()