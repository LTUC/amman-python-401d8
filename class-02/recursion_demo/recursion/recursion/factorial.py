
def fact(value):
    """
        return value! (as it's sometimes written)
        e.g. factorial(3) = 3 * 2 * 1 = 6
        Note: Normally wouldn't name a package or module this way
        but wanted to be really clear about which was which
        Bonus: hover your mouse over the function name when importing
    """
    if type(value) == str:
        return "Please provide a positive integer"
    if value<=1:
        return 1
    return value * fact(value-1)