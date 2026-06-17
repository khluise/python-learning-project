def leap_year(year):
    """This function checks if a year is a leap year 
    and return boolean."""
    if year % 400 == 0: return True
    if year % 100 == 0: return False
    if year % 4 == 0: return True
    return False
