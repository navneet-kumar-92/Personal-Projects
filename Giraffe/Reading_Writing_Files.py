family_file = open("Family.txt", "r")
# Change the mode types as r(ead), w(rite), a(ppend),r+ (read/write)

# How to get information from the file

print(family_file.readable())
# Above one asks the question - Yes we can read!
# print(family_file.read())
# print(family_file.readline())
# print(family_file.readline())


# print(family_file.readlines())
# print(family_file.readlines()[2])

for member in family_file.readlines():
    print(member)

family_file.close()

family_file = open("Family.txt", "a")
family_file.write("\nSrishti 20")
family_file.close()

# If you use write mode, it would overwrite everything

family_file2 = open("Family2.txt", "r+")
family_file2.write("\nSrishti 20")
print(family_file2.read())
family_file2.close()

webpage = open("index.html", "w")
webpage.write("<p> This is the landing page </p>")
webpage.close()