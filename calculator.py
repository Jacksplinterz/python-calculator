print("This is my first time actually building something real using python lol.")
print("So, this is gonna be a calculator and an indication of my current practical knowledge of the python language and application of if/else statements.")
print("It's gonna be purely text-based so it wont look fancy or anything yet but it's gonna work fs.")
print("As I make progress in the python course, I'll update this file or begin more projects so it accurately reflects my current skill level. ")
print("------------------------------------------------------------------------------------------------")
print("Welcome to my calculator!")
op1 = float(input("Please type your first operand: "))
op2 = float(input("Please type your 2nd operand: "))

operation = input("Which operation would you like to perform? (+, -, * or /) ")
if (operation == "+"):
    result = op1 + op2
    print(f"{op1} + {op2} = {result}")
elif (operation == "-"):
    result = op1 - op2
    if (op1 >= op2):
        print(f"{op1} - {op2} = {result}")
    elif (op1 < op2):
        userchoice = input("This is gonna result in a negative value. Do you wanna proceed? Y/N ").upper()
        if userchoice == "Y":
            print(f"{op1} - {op2} = {result}")
        elif userchoice == "N":
            print("Noted. Please restart the program.")
        else:
            print("Invalid Option. Please restart the program.")
  
elif (operation == "*"):
    result = op1 * op2
    print(f"{op1} * {op2} = {result}")

elif (operation == "/"):
    if op2 == 0:
        print("Sorry, You cannot divide a number by 0.")
    else:
        result = op1/op2
        print(f"{op1} / {op2} = {result}")

else: 
    print("You have entered an invalid operation. Please try again.") 

