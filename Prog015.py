num1 = float(input("Enter your first number "))
num2 = float(input("Enter your second number "))

if num2 != 0:
    remainder = num1 % num2
    print("The remainder is: ", remainder)
else:
    print("Please, enter a valid value")