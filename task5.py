attempt = 0

while attempt < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username.isalpha() and password.isdigit():
        print("Valid Input")
        print("Registration done")
        break
    else:
        print("Invalid Input")
        attempt += 1

if attempt == 3:
    print("Account Locked") 