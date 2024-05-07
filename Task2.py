num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print("The arithmetic operations are:")
print("1:Addition")
print("2:Subtraction")
print("3:Multipication")
print("4:Division")
while True:
    ans=input("Want to perform arithmetic operations(yes/no)?:")
    if ans=="yes":
        operation=int(input("Enter the option no:"))
        if operation==1:
            add=num1+num2
            print("The addition of the numbers is",add)
        elif operation==2:
            subtract=num1-num2
            print("The subtraction of the numbers is",subtract)
        elif operation==3:
            multiply=num1*num2
            print("The multiplication of the numbers is",multiply)
        elif operation==4:
            divide=num1/num2
            print("The division of the numbers is",divide)
        else:
            print("Invalid operation")
    else:
        break


