"""
>>> 12 = x
Traceback (most recent call last):
  File "<stdin>", line 1
SyntaxError: can't assign to literal
"""
import doctest
doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)