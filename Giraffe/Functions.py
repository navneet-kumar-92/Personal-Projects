print("Welcome to functions")


def say_hi(name, age):
    print("Hello " + name + str(age))

say_hi("Mike",28)
say_hi("Navneet",13)


# -- Using a return statement

def calc_exponential(num,power):
    out = pow(num,power)
    return out

a = calc_exponential(2,4)
print(a)

print("  - - - - - - - - Using Classes and Objects - - - - - - - - ")

from Classes_and_Objects import Student

student1=Student("Navneet", "Data Science", 4.0, False)
student2=Student("Pam", "Artifical Intelligence", 3, False)
print(student1.name)
print(type(student1.gpa))
print(student2.gpa)

print(student1.on_honor_roll())

