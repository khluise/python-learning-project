# *args       = allows you to pass multiple non-key arguments
# **kwargs    = allows you to pass multiple keyword-arguments
#               * unpacking operator
#               1. positional 2. default 3.keyword 4.ARBITARY

# def add(*nums):
#     total = 0
#     # print(type(args))
#     for num in nums:
#         total += num
#     return  total
# print(add(1,2,3, 5))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
# display_name("Spongebob", "Squarepants")
# print()
# display_name("Dr.", "Spongebob", "Squarepants")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_address(street="123 Fake st.",
#               city="Detroit",
#               state="MI",
#               zip="54321")

def shipping_lable(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
shipping_lable("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake st.",
               apt="#100",
               city="Detroit",
               state="MI",
               zip="54321")