# For loop with else

`for` loops also have an `else` clause which most of us are unfamiliar with. The else clause executes after the loop
completes normally. This means that the loop did not encounter a break statement.

```python
for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything..
    not_found_in_container()
```

# Iterate keys from dictionary

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)
```

