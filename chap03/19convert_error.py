"""
>>> convert_to_celsius(212)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'convert_to_celsius' is not defined
"""
import doctest
doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)
