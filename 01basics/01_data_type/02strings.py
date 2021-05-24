"""
Ref: https://realpython.com/python-strings/
"""

# String Formatting

name = 'John'
print('Hello, %s' % name)

# 1 “Old Style” String Formatting (% Operator)

'''
>>> 'Hello, %s' % FirstName
"Hello, Bob"

>>> 'Hello, %s %s' % ('FirstName', 'LastName')
"Hello, Bob"

'''

# 2 “New Style” String Formatting (str.format)
'''
Python 3 introduced a new way to do string formatting that was also later back-ported to Python 2.7. 

>>> 'Hello, {}'.format(name)
'Hello, Bob'

>>> 'Hello, {} {}'.format('FirstName', 'LastName')
'Hello, FirstName LastName'

>>> 'Hello, {0} {1}'.format('FirstName', 'LastName')
'Hello, FirstName LastName'

>>> 'Hello, {1} {0}'.format('FirstName', 'LastName')
'Hello, LastName FirstName'

>>> 'Hello, {first_name} {last_name}'.format(first_name='FirstName', last_name='LastName')
'Hello, FirstName LastName'

>>> 'Hello, {first_name} {last_name}'.format_map({'first_name': 'FirstName', 'last_name': 'LastName'})
'Hello, FirstName LastName'
'''

# 3 String Interpolation / f-Strings (Python 3.6+)

'''
Python 3.6 added a new string formatting approach called formatted string literals or “f-strings”.

>>> name = 'Bob'
>>> f'Hello, {name}!'
'Hello, Bob!'

>>> a = 5
>>> b = 10
>>> f'Five plus ten is {a + b} and not {2 * (a + b)}.'
'Five plus ten is 15 and not 30.'
'''

# 4 Template Strings (Standard Library)

'''
Here’s one more tool for string formatting in Python: template strings. It’s a simpler and less powerful
mechanism, but in some cases this might be exactly what you’re looking for.

>>> from string import Template
>>> t = Template('Hey, $name!')
>>> t.substitute(name=name)
'Hey, Bob!'

>>> temp_string = 'Hey $name, there is a $error error!'
>>> Template(temp_string).substitute(
...     name=name, $error=25)
'Hey Bob, there is a 25 error!'
'''

# Note, Don't use the operator + to concatenate the string


# Multi line strings

'''
>>> print("""
    b
    c""")
a
b
c
'''

# List of the Methods of String object

'''
>>> my_str = 'my_string'
>>> dir(my_str)
'''

'''
s.count(<sub>[, <start>[, <end>]])
Counts occurrences of a substring in the target string.


>>> 'foo goo moo'.count('oo')
3
>>> 'foo goo moo'.count('oo', 0, 8)
2

s.endswith(<suffix>[, <start>[, <end>]])
Determines whether the target string ends with a given substring.

>>> 'foobar'.endswith('bar')
True
>>> 'foobar'.endswith('baz')
False

>>> 'foobar'.endswith('oob', 0, 4)
True
>>> 'foobar'.endswith('oob', 2, 4)
False


s.startswith(<prefix>[, <start>[, <end>]])
Determines whether the target string starts with a given substring.

>>> 'foobar'.startswith('foo')
True
>>> 'foobar'.startswith('bar')
False

>>> 'foobar'.startswith('bar', 3)
True
>>> 'foobar'.startswith('bar', 3, 2)
False

s.replace(<old>, <new>[, <count>])
Replaces occurrences of a substring within a string.

>>> 'foo bar foo baz foo qux'.replace('foo', 'grault')
'grault bar grault baz grault qux'

>>> 'foo bar foo baz foo qux'.replace('foo', 'grault', 2)
'grault bar grault baz foo qux'


s.rstrip([<chars>])
Trims trailing characters from a string.

>>> '   foo bar baz   '.rstrip()
'   foo bar baz'

>>> 'foo.$$$;'.rstrip(';$.')
'foo'

s.strip([<chars>])
Strips characters from the left and right ends of a string.

>>> 'www.realpython.com'.strip('w.moc')
'realpython'

'''


# Converting Between Strings and Lists

'''
s.join(<iterable>)
Concatenates strings from an iterable.

>>> ', '.join(['foo', 'bar', 'baz', 'qux'])
'foo, bar, baz, qux'

>>> list('corge')
['c', 'o', 'r', 'g', 'e']

>>> ':'.join('corge')
'c:o:r:g:e'

>>> '---'.join(['foo', 23, 'bar'])
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    '---'.join(['foo', 23, 'bar'])
TypeError: sequence item 1: expected str instance, int found


s.partition(<sep>)
Divides a string based on a separator.

>>> 'foo.bar'.partition('.')
('foo', '.', 'bar')
>>> 'foo@@bar@@baz'.partition('@@')
('foo', '@@', 'bar@@baz')

>>> 'foo.bar'.partition('@@')
('foo.bar', '', '')

s.split(sep=None, maxsplit=-1)
Splits a string into a list of substrings.

>>> 'www.realpython.com'.split('.', maxsplit=1)
['www', 'realpython.com']
>>> 'www.realpython.com'.rsplit('.', maxsplit=1)
['www.realpython', 'com']


'''

