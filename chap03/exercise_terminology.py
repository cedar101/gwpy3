def square(num):
    """ (number) -> number
    
    Return the square of num.

    >>> square(3)
    9
    """
    return num * num


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)