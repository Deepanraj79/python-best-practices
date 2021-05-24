## Unpacking the list of elements into two variables

```python
>>> numbers = [3, 5, 2, 4, 7, 1]

>>> min_value, *rest = numbers
>>> min_value
3
>>> rest
[5, 2, 4, 7, 1]
```
