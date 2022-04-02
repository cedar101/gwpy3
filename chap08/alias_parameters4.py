"""
>>> celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> remove_last_item(celegans_markers)
>>> celegans_markers
['Emb', 'Him', 'Unc', 'Lon', 'Dpy']
"""

from typing import Any

def remove_last_item(L: list[Any]) -> None:
    """마지막 항목을 삭제한 리스트 L을 반환한다.

    전제 조건: len(L) >= 0

    >>> remove_last_item([1, 3, 2, 4])
    """
    del L[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()