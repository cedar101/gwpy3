# from typing import List

def average(L: list[float]) -> float:
    """L 내 값의 평균을 반환한다.

    >>> average([1.4, 1.6, 1.8, 2.0])
    1.7
    """
    return sum(L) / len(L)


if __name__ == '__main__':
    import doctest
    doctest.testmod()