import os
# print(help("os")

path = "C:\\Users\\luise\\OneDrive\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is file!")
    elif os.path.isdir(path):
        print("That is directory")
else:
    print("That location doesn't exists!")