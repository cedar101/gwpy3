"""
>>> compound = input('분자를 입력하세요: ') 
분자를 입력하세요: 
>>> if compound == "H2O":
...     print("물") 
... elif compound == "NH3":
...     print("암모니아")
... elif compound == "CH4":
...     print("메탄")
... else:
...     print("알려지지 않은 분자") 
...
알려지지 않은 분자 
>>>
"""
import sys
import io
import doctest

sys.stdin = io.StringIO('H2SO4')
doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)