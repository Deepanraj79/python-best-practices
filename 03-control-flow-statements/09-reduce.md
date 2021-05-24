## reduce()

The first argument to Python’s reduce() is a two-argument function conveniently called function. This function will be applied to the items in an iterable to cumulatively compute a final value.

Even though the official documentation refers to the first argument of reduce() as “a function of two arguments,” you can pass any Python callable to reduce() as long as the callable accepts two arguments.


## Import it from standard module functools

```python
from functools import reduce
```

## Addition of numbers

```python
>>> def my_add(a, b):
...     result = a + b
...     print(f"{a} + {b} = {result}")
...     return result

>>> from functools import reduce

>>> numbers = [0, 1, 2, 3, 4]

>>> reduce(my_add, numbers)
0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10
```

## The Optional Argument: initializer

The third argument to Python’s reduce(), called initializer, is optional. If you supply a value to initializer, then reduce() will feed it to the first call of function as its first argument.

This means that the first call to function will use the value of initializer and the first item of iterable to perform its first partial computation. After this, reduce() continues working with the subsequent items of iterable.

```python
>>> from functools import reduce

>>> numbers = [0, 1, 2, 3, 4]

>>> reduce(my_add, numbers, 100)
100 + 0 = 100
100 + 1 = 101
101 + 2 = 103
103 + 3 = 106
106 + 4 = 110
110
```

## Addition of numbers in iterable With lambda

```python
>>> from functools import reduce

>>> numbers = [1, 2, 3, 4]

>>> reduce(lambda a, b: a + b, numbers)
10
```

## With add function from operator standard module

```python
>>> from operator import add
>>> from functools import reduce

>>> add(1, 2)
3

>>> numbers = [1, 2, 3, 4]

>>> reduce(add, numbers)
10
```

## Finding min and max with lambda

```python
>>> from functools import reduce

>>> numbers = [3, 5, 2, 4, 7, 1]

>>> # Minimum
>>> reduce(lambda a, b: a if a < b else b, numbers)
1

>>> # Maximum
>>> reduce(lambda a, b: a if a > b else b, numbers)
7
```

## Considering Performance and Readability

Python’s reduce() can have remarkably bad performance because it works by calling functions multiple times.
This can make your code slow and inefficient. Using reduce() can also compromise the readability of your code when you
use it with complex user-defined functions or lambda functions.

* Use a dedicated function to solve use cases for Python’s reduce() whenever possible. Functions such as `sum(), all(),
  any(), max(), min(), len(), math.prod()`, and so on will make your code faster and more readable, maintainable,
  and Pythonic.

* Avoid complex user-defined functions when using reduce(). These kinds of functions can make your code difficult to
  read and understand. You can use an explicit and readable for loop instead.

* Avoid complex lambda functions when using reduce(). They can also make your code unreadable and confusing.

