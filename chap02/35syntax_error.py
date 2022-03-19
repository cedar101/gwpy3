"""
>>> 2 +
Traceback (most recent call last):
  File "<stdin>", line 1
    2 +
      ^
SyntaxError: invalid syntax
"""
import doctest
doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)