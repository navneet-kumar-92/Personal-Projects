
try:
    number = int(input("Enter a number: "))
    if number/0 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError as err: # When the type is weird
    print(err)
except ZeroDivisionError:
    print("Invalid Division")

# Best practice

