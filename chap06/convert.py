def convert_to_celsius(fahrenheit: float) -> float:
    """화씨온도와 동일한 섭씨온도를 반환합니다.

    >>> convert_to_celsius(75)
    23.88888888888889
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0

if __name__ == '__main__':
    import doctest
    doctest.testmod()