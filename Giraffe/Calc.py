# Building Basic Calculator
print(" ------------ WELCOME TO BASIC ADDITION, SUBSTRACTION CALCULATOR ------------ ")
a = input("Enter first number : ")
b = input("Enter second number : ")
operator = input("Enter the operation you want to conduct (+ OR -) : ")
# if operator.find("+") != -1:
#     print("The result is : " + str((float(a) + float(b))))
# elif operator.find("-") != -1:
#     print("The result is : " + str((float(a) - float(b))))
# else:
#     print("Entered a bad operator!")

if operator == '+':
    print("The result is : " + str((float(a) + float(b))))
elif operator == '-':
    print("The result is : " + str((float(a) - float(b))))
else:
    print("Entered a bad operator!")
