"""Python list"""

# Del statement
'''

>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
'''

# Looping Technique

# enumerate()

'''
When looping through dictionaries, the key and corresponding value can be retrieved at the same time
using the items() method.

>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe

'''

# zip()

'''
To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
'''

# reversed()

'''
To loop over a sequence in reverse,

>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
'''

# sorted()

'''
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
'''

# List Comprehensions

'''
List comprehensions provide a concise way to create lists. 

>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


squares = [x**2 for x in range(10)]


>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

'''

# Nested List Comprehensions

'''
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

'''

# List methods

# .pop()

'''
In [29]: li.pop??
Signature: li.pop(index=-1, /)
Docstring:
Remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range.
Type:      builtin_function_or_method
'''

# .sort()

'''
cities = ['Mumbai', 'London', 'Paris', 'New York']
cities.sort(key=len)

cities = ['Mumbai', 'London', 'Paris', 'New York']
cities.sort(key=str.lower)

cities = ['Mumbai', 'London', 'Paris', 'New York']
cities.sort(key=min, reverse=True)

'''

# sorted()

'''
Another difference is that the list.sort() method is only defined for lists. In contrast, the sorted() function
accepts any iterable.


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
'''

'''
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)   # sort by age
'''