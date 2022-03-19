"""
>>> ph = float(input('pH 농도를 입력하세요: ')) 
pH 농도를 입력하세요: 
>>> if ph < 7.0:
... print(ph, "은(는) 산성입니다.")
Traceback (most recent call last):
    ...
  File "<...>", line 2
    print(ph, "은(는) 산성입니다.")
        ^
IndentationError: expected an indented block
"""
import sys
import io
import doctest

sys.stdin = io.StringIO('6')
doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)