def convert_to_celsius(fahrenheit: float) -> float:
    """화씨와 동일한 섭씨를 반환합니다. 

    >>> convert_to_celsius(75)
    23.88888888888889
    """

    return (fahrenheit - 32.0) * 5.0 / 9.0

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print('80, 78.8, and 10.4 degrees Fahrenheit are equal to ', end='')
    print(convert_to_celsius(80), end=', \n')
    print(convert_to_celsius(78.8), end=', and ')
    print(convert_to_celsius(10.4), end=' Celsius.\n')
