import doctest


def convert_to_celsius(fahrenheit: float) -> float:
    """화씨와 동일한 섭씨를 반환한다.

    >>> convert_to_celsius(75)
    23.88888888888889
    """

    return (fahrenheit - 32.0) * 5.0 / 9.0

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    
    print(convert_to_celsius(80))
    print(convert_to_celsius(78.8))
    print(convert_to_celsius(10.4))
