
# For Loops
for letter in "Giraffe Academy":
    print(letter)

# This loops through every character

friends = ["Jim", "Steve", "Sarah", "Sidd"]
for friend in friends:
    print(friend)
# This loops through every individual

for index in range(3,5):
    print(index)

i = 10

for index in range(i):
    print(index)

for index in range(len(friends)):
    print(str(index) + " : " + friends[index])

# Exponent Function :


def raise_to_power(base,power):
    result = 1
    for index in range(power):
        result = result * base
    return result

print(raise_to_power(3,6))