"""
>>> ph = float(input('pH 농도를 입력하세요: ')) 
pH 농도를 입력하세요: 
>>> if ph < 7.0:
...     print(ph, "은(는) 산성입니다.") 
... elif ph > 7.0:
...     print(ph, "은(는) 염기성입니다.") 
...
8.5 은(는) 염기성입니다.
>>>
"""
import sys
import io
import doctest

sys.stdin = io.StringIO('8.5')
doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)