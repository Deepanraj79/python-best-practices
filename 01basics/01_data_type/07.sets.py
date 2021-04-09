'''Python Sets

References

https://realpython.com/python-sets/
'''

# Defining Set

my_set = set()

my_set1 = {'bmw', 'toyota', 'volvo', 'chrysler'}

my_set2 = set(['bmw', 'toyota', 'volvo'])

# Set methods

# .discard()

'''
Docstring:
Remove an element from a set if it is a member.

If the element is not a member, do nothing.
Type:      builtin_function_or_method

'''

# .remove()

'''
Docstring:
Remove an element from a set; it must be a member.

If the element is not a member, raise a KeyError.
Type:      builtin_function_or_method
'''

# .pop()

'''
Docstring:
Remove and return an arbitrary set element.
Raises KeyError if the set is empty.
Type:      builtin_function_or_method

'''

# Mutable objects can not be a element in Set

'''
Don’t forget that set elements must be immutable. For example, a tuple may be included in a set:

>>> x = {42, 'foo', (1, 2, 3), 3.14159}
>>> x
{42, 'foo', 3.14159, (1, 2, 3)}

>>> my_set = {[1, 2, 3]}
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    {a}
TypeError: unhashable type: 'list'

>>> my_set = {{'a': 1, 'b': 2}}
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    {d}
TypeError: unhashable type: 'dict'

'''


# Frozen Set

'''
Python provides another built-in type called a frozenset, which is in all respects exactly like a set, except
that a frozenset is immutable. You can perform non-modifying operations on a frozenset:

>>> x = frozenset(['foo', 'bar', 'baz'])
>>> x
frozenset({'foo', 'baz', 'bar'})

>>> len(x)
3
'''

# We can not perform non modifying operation on the frozenset

'''
>>> x = frozenset(['foo', 'bar', 'baz'])

>>> x.add('qux')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    x.add('qux')
AttributeError: 'frozenset' object has no attribute 'add'

>>> x.pop()
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    x.pop()
AttributeError: 'frozenset' object has no attribute 'pop'
'''

