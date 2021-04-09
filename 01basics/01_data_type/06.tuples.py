'''Python Tuples'''

# Defining tuple

'''
You can use commas to define tuple
>>> tuple1 = 1,2,3,4
>>> tuple1
(1, 2, 3, 4)

Second method is to use parenthesis

>>> tuple2 = (5,6,7,8)
>>> tuple2
(5, 6, 7, 8)

While defining singleton tuple, comma is required

>>> singleton = ('element1',)
>>> type(singleton)
<class 'tuple'>

>>> singleton = ('element1')
>>> type(singleton)
str
'''


# Tuple methods

# .count()

'''
Signature: my_tuple.count(value, /)
Docstring: Return number of occurrences of value.
Type:      builtin_function_or_method


>>> my_tuple = (1, 'hello')

>>> my_tuple.count(1)
1

>>> my_tuple.count(4)
0
'''

# .index()

'''
Signature: my_tuple.index(value, start=0, stop=9223372036854775807, /)
Docstring:
Return first index of value.

Raises ValueError if the value is not present.
Type:      builtin_function_or_method

>>> my_tuple = (1, 'hello')
>>> my_tuple.index(4)

ValueError: tuple.index(x): x not in tuple
'''

# Note

'''
Don't use a mutable objects in a tuple.

When you define a tuple with a list or dictionary as its member then it loses its mutability and hashable
behavior also. Because list and dictionaries are the mutable objects and using them in a tuple makes tuple
modifiable.

>>> mutable_tuple = (1,2,3,[4,5],{'travel':'blog'} )
>>> mutable_tuple[3][1]=9
>>> mutable_tuple
(1, 2, 3, [4, 9], {'travel': 'blog'})
>>> mutable_tuple[4]['travel']='expense'
>>> mutable_tuple
(1, 2, 3, [4, 9], {'travel': 'expense'})

In above, tuple got modified. In such cases, it does not make any sense of using a tuple because it just not
only modifies the behavior but also affects the benefits of hashing.
'''
