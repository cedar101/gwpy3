"""
>>> ph = float(input('pH 농도를 입력하세요: ')) 
pH 농도를 입력하세요: 
>>> if ph < 7.0:
...     print(ph, "은(는) 산성입니다.") 
... print("조심히 다루세요!") 
Traceback (most recent call last):
  File "<stdin>", line 3 
    print("조심히 다루세요!")
        ^
SyntaxError: invalid syntax
"""
import sys
import io
import doctest

sys.stdin = io.StringIO('8.0')
doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)