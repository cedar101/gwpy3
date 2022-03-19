"""
>>> 3 + moogah
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'moogah' is not defined
"""
import doctest
doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)