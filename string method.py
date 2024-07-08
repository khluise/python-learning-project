# # name = input("Enter your full name: ")
# phone_number = input("Enter your full number: ")
#
# #result = len(name)
# #result = name.find(" ")
# # result = name.rfind("a")
# # result = name.capitalize()
# # result = name.upper()
# # result = name.isdigit()
# # result = name.isalpha()
# # result = phone_number.count("-")
# result = phone_number.replace("-","")
# print(result)

# valid user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

user_name = input("Enter your username: ")
length = len(user_name)
if(length<=12) and (user_name.find(" ")) and (user_name.isalpha()):
    print("User name is valid")
else:
    print("unvalid")