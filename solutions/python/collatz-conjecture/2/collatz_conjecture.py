"""Collatz Conjecture"""


def is_even(number):
    """This function checks is a number is even and return true."""
    return number % 2 == 0
    

def collatz_function(number):
    """This function """
    if number < 1 :
        raise ValueError("Only positive integers are allowed")
    if is_even(number):
        return number / 2
        
    return (number * 3) + 1


def steps(number):
    """This function returns the steps requires to reach 1 according
    to the rules of the Collatz Conjecture.
    """
    step_count = 0

    while number != 1:
        number = collatz_function(number)
        step_count += 1
    
    return step_count
