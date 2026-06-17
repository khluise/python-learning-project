def square(number):
    """Returns the number of grains on a given square.

    The number of grains doubles on each square so it can be calculated
    mathematically as 2 ** (number - 1).
    
    Args:
        number (int): The position of the square in the chessboard.

    returns:
        int : The number of grains in that square.
        
     Raises:
        ValueError: If the square number is not between 1 and 64 meaning
            the if the square is not in a chess board.
    """
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
    
    return 2 ** (number - 1)

def total():
    """Calculates the total number grains.

    returns:
        int : The total number of grains on the chessboard.
    """
    total_grains = 0
    current_square = 1

    while current_square <= 64:
        total_grains += square(current_square)
        current_square += 1

    return total_grains
