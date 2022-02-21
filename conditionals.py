num = 11

if num > 0:
    if num < 11:
        print("Number is between 1-10") 
    else:
        print("Number is out of range")


name = "Ollie"

if name in ("root", "admin"):
    print("This is not a valid username!")
else:
    print(f"Welcome, {name}!")


password = "super"

if password in ("password", "0000", "1234", "root", "admin"):
    print("This is a rubbish password, pick a different one")
else:
    print("password accepted")