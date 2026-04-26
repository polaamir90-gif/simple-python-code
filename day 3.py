"""degree = int(input("Enter your degree: "))
name = input("Enter your name: ")
if degree >= 85:
    print(f"{name} passed with Excellent")
elif degree >= 65:
    print(f"{name} passed with Good")
else:
    print(f"{name} failed") """
#####################################################################
''''name = input("Enter your name: ")
degree = int(input("Enter your degree: "))

if degree >= 50:
    if degree >= 85:
        print(f"{name} passed with Excellent")
    elif degree >= 65:
        print(f"{name} passed with Good")
    else:
        print(f"{name} passed")
else:
    print(f"{name} failed")'''''
#####################################################################
"""Username = input("Enter your Username: ")
Password = input("Enter your Password: ")

if Username == "pola":
    if Password == "5000":
        print(f"Hello {Username}, Login successful")
    else:
        print("Wrong password")

elif Username == "marco":
    if Password == "6000":
        print(f"Hello {Username}, Login successful")
    else:
        print("Wrong password")

else:
    print("User not found") """""
#####################################################################
number = int(input("Enter the number: "))
if number % 2 == 0:
    print(f"{number} → Even")
else:
    print(f"{number} → Odd")