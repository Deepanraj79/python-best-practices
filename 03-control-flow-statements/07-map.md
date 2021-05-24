## Basic Example
```python
>>> str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

>>> int_nums = map(int, str_nums)
>>> int_nums
<map object at 0x7fb2c7e34c70>

>>> list(int_nums)
[4, 8, 6, 5, 3, 2, 8, 9, 2, 5]

>>> str_nums
["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
```

## Using map() With Different Kinds of Functions

```python
>>> numbers = [-2, -1, 0, 1, 2]

>>> abs_values = list(map(abs, numbers))
>>> abs_values
[2, 1, 0, 1, 2]

>>> list(map(float, numbers))
[-2.0, -1.0, 0.0, 1.0, 2.0]

>>> words = ["Welcome", "to", "Real", "Python"]

>>> list(map(len, words))
[7, 2, 4, 6]
```

# Processing Multiple Input Iterables With map()
If you supply multiple iterables to map(), then the transformation function must take as many arguments as iterables you
pass in. Each iteration of map() will pass one value from each iterable as an argument to function. The iteration stops
at the end of the shortest iterable.

```python
>>> first_it = [1, 2, 3]
>>> second_it = [4, 5, 6, 7]

>>> list(map(pow, first_it, second_it))
[1, 32, 729]
```

```python
>>> list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5]))
[1, 1, 1]

>>> list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8]))
[10, 15]
```

## Transforming Iterables of Strings With Python’s map()

```python
>>> string_it = ["processing", "strings", "with", "map"]
>>> list(map(str.capitalize, string_it))
['Processing', 'Strings', 'With', 'Map']

>>> list(map(str.upper, string_it))
['PROCESSING', 'STRINGS', 'WITH', 'MAP']

>>> list(map(str.lower, string_it))
['processing', 'strings', 'with', 'map']
```

## Combining map() With Other Functional Tools
```python
>>> import math

>>> def is_positive(num):
...     return num >= 0
...

>>> def sanitized_sqrt(numbers):
...     cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
...     return list(cleaned_iter)
...

>>> sanitized_sqrt([25, 9, 81, -16, 0])
[5.0, 3.0, 9.0, 0.0]
```

