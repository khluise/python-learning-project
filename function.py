# def greetings(name):
#     print(f"Hello {name}!")
#
# greetings("Luise")

# def greetings(name, age):
#     print(f"Hello {name}!")
#     print(f"You are {age} years old.")
# greetings("Luise", 24)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount} is due: {due_date}")
# display_invoice("abir", 25, "10/7")

# def add(x, y):
#     z = x+ y
#     return z
# def subtract(x,y):
#     z = x-y
#     return z
# def multiply(x,y):
#     z= x*y
#     return z
# def divide(x,y):
#     z = x/y
#     return z
# print(add(1,2))
# print(divide(1,2))

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)
# print(net_price(500))
# print(net_price(500,0.03,0.06))

# import time
# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")
# count(30, 15 )


# keyword arguments = an argument preceded by identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3.keyword 4.arbitrary
# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")
# hello("Hello", last="Squarepants", title="Mr.", first="Spongbob")

def get_phone(country, operator, first, last):
    return f"{country}-{operator}-{first}-{last}"
phone_num = get_phone(country=88, operator="013", first=1518, last=8626)
print(phone_num)
