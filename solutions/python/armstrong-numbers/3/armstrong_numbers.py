"""This modules checks if a number is a 
Armstrong number.
"""

def is_armstrong_number(number):
    """Checks if a number is Armstrong number.

    Args:
        number (int): The number to check.
    Returns:
        bool : This function returns True if the number
            matches the condition else return False.

    This function converts the number into a string then
    iterates over the char in that string to get the digits.
    If the sum of each digit each raised to the power of the
    number of digits is equal to the number itself then it's
    an Armstrong number. If this condition is matched then it
    return True else False.
    """
    digits = str(number)
    digits_num = len(digits)
    foo = 0
    for digit in digits:
        foo += int(digit)**digits_num
    return foo == number
