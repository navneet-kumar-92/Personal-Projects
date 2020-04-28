# Dictionary - Lookup file kind of :

# How to convert a month short form into long form
# Jan -> January
# Mar -> March

month_Convert = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(month_Convert)
print(month_Convert["Jan"])
print(month_Convert.get("Mar"))
print(month_Convert.get("Apr", "Not a valid key"))
print(month_Convert.get("Jan", "Not a valid key"))


month_Convert2 = {
    1: "January",
    2: "February",
    3: "March",
}

print(month_Convert2)
print(month_Convert2[1])
print(month_Convert2.get(2))
print(month_Convert2.get(6, "Not a valid key"))
print(month_Convert2.get(2, "Not a valid key"))