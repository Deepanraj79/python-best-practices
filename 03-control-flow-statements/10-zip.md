# Using `zip()` in Python

Python’s zip() function is defined as zip(*iterables). The function takes in iterables as arguments and returns an
iterator. This iterator generates a series of tuples containing elements from each iterable. zip() can accept any type
of iterable, such as `files, lists, tuples, dictionaries, sets,` and so on.

## Passing No Arguments

```python
>>> zipped = zip()
>>> zipped
<zip object at 0x7f196294a488>
>>> list(zipped)
[]
```

## Passing One Argument

```python
>>> a = [1, 2, 3]
>>> zipped = zip(a)
>>> list(zipped)
[(1,), (2,), (3,)]
```

## Passing n Arguments

```python
>>> numbers = [1, 2, 3]
>>> letters = ['a', 'b', 'c']
>>> zipped = zip(numbers, letters)
>>> zipped  # Holds an iterator object
<zip object at 0x7fa4831153c8>
>>> type(zipped)
<class 'zip'>
>>> list(zipped)
[(1, 'a'), (2, 'b'), (3, 'c')]
```

## Passing Arguments of Unequal Length

In these cases, the number of elements that zip() puts out will be equal to the length of the shortest iterable.
The remaining elements in any longer iterables will be totally ignored by zip(), as you can see here:

```python
>>> list(zip(range(5), range(100)))
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
```

If trailing or unmatched values are important to you, then you can use itertools.zip_longest() instead of zip(). With
this function, the missing values will be replaced with whatever you pass to the fillvalue argument (defaults to None).

```python
>>> from itertools import zip_longest
>>> numbers = [1, 2, 3]
>>> letters = ['a', 'b', 'c']
>>> longest = range(5)
>>> zipped = zip_longest(numbers, letters, longest, fillvalue='?')
>>> list(zipped)
[(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]
```

## Traversing Lists in Parallel
```python
>>> letters = ['a', 'b', 'c']
>>> numbers = [0, 1, 2]
>>> for l, n in zip(letters, numbers):
...     print(f'Letter: {l}')
...     print(f'Number: {n}')
```

```python
>>> letters = ['a', 'b', 'c']
>>> numbers = [0, 1, 2]
>>> operators = ['*', '/', '+']
>>> for l, n, o in zip(letters, numbers, operators):
...     print(f'Letter: {l}')
...     print(f'Number: {n}')
...     print(f'Operator: {o}')
```

## Traversing Dictionaries in Parallel

```python
>>> dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
>>> dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
>>> for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
...     print(k1, '->', v1)
...     print(k2, '->', v2)
```

## Unzipping a Sequence

```python
>>> pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
>>> numbers, letters = zip(*pairs)
>>> numbers
(1, 2, 3, 4)
>>> letters
('a', 'b', 'c', 'd')
```

## Sorting in Parallel
```python
>>> letters = ['b', 'a', 'd', 'c']
>>> numbers = [2, 4, 3, 1]
>>> data = sorted(zip(letters, numbers))  # Sort by letters
>>> data
[('a', 4), ('b', 2), ('c', 1), ('d', 3)]
```

## Building Dictionaries

```python
>>> fields = ['name', 'last_name', 'age', 'job']
>>> values = ['John', 'Doe', '45', 'Python Developer']
>>> a_dict = dict(zip(fields, values))
>>> a_dict
{'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Developer'}
```

```python
>>> new_job = ['Python Consultant']
>>> field = ['job']
>>> a_dict.update(zip(field, new_job))
>>> a_dict
{'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Consultant'}
```