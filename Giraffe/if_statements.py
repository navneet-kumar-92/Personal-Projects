is_male = False
is_tall = True

if is_male and is_tall:
    print("You are male")
elif is_male and not is_tall:
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and you are not tall")


# --- Comparisons

def max_num(a, b, c):
    """

    :type a: Number
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(" - - - - Welcome to the maximum number finder - - - - ")
a=float(input("Enter number 1: "))
b=float(input("Enter number 2: "))
c=float(input("Enter number 3: "))
print(max_num(a, b, c))
