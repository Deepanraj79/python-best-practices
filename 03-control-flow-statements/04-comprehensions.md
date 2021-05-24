List comprehensions provides a powerful, concise way to work with lists.

Generator expressions follows almost the same syntax as list comprehensions but return a generator instead of a list.

Creating a new list requires more work and uses more memory. If you are just going to loop through the new list, prefer
using an iterator instead.

### Bad
```python
# needlessly allocates a list of all (gpa, name) entires in memory
valedictorian = max([(student.gpa, student.name) for student in graduates])
```

### Good
```python
valedictorian = max((student.gpa, student.name) for student in graduates)
```

Use list comprehensions when you really need to create a second list, for example if you need to use the result multiple
times.

If your logic is too complicated for a short list comprehension or generator expression, consider using a generator
function instead of returning a list.

# Never remove items from a list while you are iterating through it.

##Filter elements greater than 4

### Bad
```python
a = [3, 4, 5]
x = 4
for i in a:
    if i > 4:
        a.remove(i)
```

## Good
```python
a = [3, 4, 5]
x = 4
# comprehensions create a new list object
filtered_values = [value for value in a if value != x]

# generators don't create another list
filtered_values = (value for value in a if value != x)
```

# Modifying the values in a list
## Add three to all list members.

## Bad
```python
a = [3, 4, 5]
b = a                     # a and b refer to the same list object
for i in range(len(a)):
    a[i] += 3             # b[i] also changes
```

### Good
```python
a = [3, 4, 5]
b = a

# assign the variable "a" to a new list without changing "b"
a = [i + 3 for i in a]
```

# Comprehension for nested for loops

```python
results = []
for i in range(10):
    for j in range(i):
        results.append((i, j))
```

```python
results = [(i, j)
           for i in range(10)
           for j in range(i)]
```

# Invoke function in Comprehension expression

```python
result = [do_something_with(item) for item in item_list]
```
