# from typing import List

def remove_neg(num_list: list[float]) -> None: 
    """리스트 num_list에서 음수를 삭제한다.
    
    >>> numbers = [-5, 1, -3, 2]
    >>> remove_neg(numbers)
    >>> numbers
    [1, 2]
    >>> numbers2 = [1, 2, 3, -3, -1, 3, 1]
    >>> remove_neg(numbers2)
    >>> numbers2
    [1, 2, 3, 3, 1]
    """ 
    
    for item in reversed(num_list): 
        if item < 0: 
            num_list.remove(item)
            
if __name__ == '__main__':
    import doctest
    doctest.testmod()