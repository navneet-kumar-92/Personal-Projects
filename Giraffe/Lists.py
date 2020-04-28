friends = ["Abhinav", "Harshal", "Kisna", "Toshu", "Swadesh"]

print(friends[2:])
print(friends[2:10])

friends[3] = "Isha"

print(friends)

# --- Using functions with Python

lucky_nums = [4, 8, 15, 16, 0, 23, 42]
friends = ["Abhinav", "Harshal", "Kisna", "Toshu", "Swadesh"]
print(friends)
print(lucky_nums)

# -- Extend function

friends.extend(lucky_nums)
print(friends)

# -- Append Function

friends.append("Creed")
print(friends)

# -- Insert function

friends.insert(1, "Kelly")
print(friends)

# -- Remove function

# -- clear function

# -- pop : Pops the last item off the list
print(friends)
a=friends.pop()
print(friends)
print(a)

# -- index : find whether an item is avalable or not

print(friends.index("Kisna"))

# -- Count the number of items
friends.append("Kisna")
friends.insert(2,"Kisna")
print(friends.count("Kisna"))
print(friends.index("Kisna"))

# sort
friends = ["Abhinav", "Harshal", "Kisna", "Toshu", "Swadesh"]
friends.sort()
print(friends)

friends.reverse()
print(friends)

# copy
friends2=friends.copy()
print(friends2)

# -- Tuples
# Immutable Lists - Anything that doesn't need to be changed

coordinates = (4,5)
print(coordinates)
print(coordinates[0])

# List of tuples
coordinates = [(4,5),(2,3)]
print(coordinates)
print(coordinates[0][1])


# 2D lists
numbers_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10]
]

print(numbers_grid)
print(numbers_grid[0])
print(numbers_grid[0][2])

