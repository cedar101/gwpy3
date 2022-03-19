"""
>>> ph = float(input('pH 농도를 입력하세요: ')) 
pH 농도를 입력하세요: 
>>> if ph < 7.0:
...     ph = 8.0
...
>>> if ph > 7.0:
...      print(ph, "은(는) 염기성입니다.") 
...
8.0 은(는) 산성입니다. 
>>> ph = float(input('pH 농도를 입력하세요: ')) 
pH 농도를 입력하세요: 
>>> if ph < 7.0:
...     ph = 8.0
... elif ph > 7.0:
...      print(ph, "은(는) 염기성입니다.") 
...
>>>
"""
import sys
import io
import doctest

sys.stdin = io.StringIO('6.0\n6.0')
doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)