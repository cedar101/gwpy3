def total_occurrences(s1: str, s2: str, ch: str) -> int: 
    """전제 조건: len(ch) == 1 
    
    s1과 s2에서 ch가 나온 횟수를 반환한다.
    
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    return s1.count(ch) + s2.count(ch)

if __name__ == '__main__':
    import doctest
    doctest.testmod()