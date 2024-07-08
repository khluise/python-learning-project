# fruits =        ["apple", "orange", "banana", "coconut"]
# vegetables =    ["celery", "carrots", "potatoes"]
# meats =         ["chiken", "fish", "turkey"]
#
# # 2D list
# groceries = [fruits, vegetables, meats]
#
# # print(groceries[0][3])
#
# for collection in groceries:
#     for food in collection:
#         print(food, end = " ")
#     print()

num_pad =((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()