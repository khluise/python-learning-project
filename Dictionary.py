# Dictionary = a collection of {key: value} pairs
#             ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow",
            "Bangladesh": "Dhaka"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("India"))

# if capitals.get("Japan"):
#     print("That capital exits"):
# else:
#     print("That capital doesn't exit")

# capitals.update({"Germany": "Berlin"})
# print(capitals)

# capitals.pop("Bangladesh")
# capitals.popitem()
# capitals.clear()
# print(capitals)

# keys = capitals.keys()
# for key in capitals.keys():
#     print(key, end=" ")
# print()
# values = capitals.values()
# for value in values:
#     print(value, end=", ")

# items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
