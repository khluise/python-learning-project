"""Determines the nature of triangle"""


def not_triangle(sides):
    """Checks for a invalid triangle returns boolean"""
    sorted_sides = sorted(sides)
    return sorted_sides[0] + sorted_sides[1] <= sorted_sides[2] \
        or len(sides) > 3  or sorted_sides[0] <= 0


def equilateral(sides):
    """Checks if the triangle have three equal sides returns boolean."""
    if not_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """Checks if the triangle have at least two equal sides returns boolean."""
    if not_triangle(sides):
        return False
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]


def scalene(sides):
    """Checks if the triangle have no equal sides returns boolean."""
    if not_triangle(sides):
        return False
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]