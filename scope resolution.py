# variable scope      = where a variable is visible and accessible
# scope resolution    = (LEGB) Local -> Enclosed -> Global -> Built-in

# # Variables defined within a function have a local scope
# def func1():
#     x = 1
#     print(x)
# def func2():
#     x = 2
#     print(x)
# func1()
# func2()

# # If variable is not found in local scope then it will search in enclosed scope
# def func1():
#     x = 1
#     def func2():
#         print(x)
#     func2()
# func1()

# # Then check the global scope
# def func1():
#     print(x)
#     def func2():
#         print(x)
#     func2()
# x = 3
# func1()

# Built-in
from math import e
def func1():
    print(e)
func1()