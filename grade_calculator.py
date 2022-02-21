maths = input("Welcome to Grade Calculator \n Please enter your maths mark: ")
chemistry = input("Please enter your chemistry mark: ")
physics = input("Please enter your physics mark: ")

total_mark = int(maths) + int(chemistry) + int(physics)
percentage = (total_mark / 300) * 100

print("Your percentage score is " + str(percentage))

if percentage >= 70: 
    print("You scored a grade of A")
elif percentage >= 60: 
    print("You scored a grade of B")
elif percentage >= 50: 
    print("You scored a grade of C")
elif percentage >= 40: 
    print("You scored a grade of D")
else:
    print("You failed")

# example of additional functionality

#while True:
    # ask user for input
#    user_input = input("> ")
    # check user input is valid
#    input_is_valid = test_user_input(user_input)
#    if not input_is_valid:
#        continue; # go back and ask user again
    # I now have valid input
#    break;