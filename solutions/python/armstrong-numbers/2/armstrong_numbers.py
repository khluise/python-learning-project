"""This modules checks if a number is a 
Armstrong number.
"""

def is_armstrong_number(number):
    digits = str(number)
    digits_num = len(digits)
    foo = 0
    for digit in digits:
        foo += int(digit)**digits_num
    return foo == number
