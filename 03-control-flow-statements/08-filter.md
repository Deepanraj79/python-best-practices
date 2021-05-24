The Python built-in filter() function can be used to create a new iterator from an existing iterable
(like a list or dictionary) that will efficiently filter out elements using a function that we provide.

## Using filter() with a Function(Lambda)

```python
creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']
print(list(filter(lambda x: x[0].lower() in 'aeiou', creature_names)))

# Output
['Ashley', 'Olly']
```

```python
myList = [10, 25, 17, 9, 30, -5]
# Returns the elements which are multiples of 5
myList2 = list(filter(lambda n : n%5 == 0, myList))
print(myList2)
```

## Using a pre-defined function
```python
# Returns the elements which are multiples of 5
def multiple_of_five(n):
  if n % 5 == 0:
    return n

myList = [10, 25, 17, 9, 30, -5]
myList2 = list(filter(multiple_of_five, myList))

print(myList2)
```

## Using `None` with filter()

We can pass None as the first argument to filter() to have the returned iterator filter out any value that Python
considers “falsy”. Generally, Python considers anything with a length of 0 (such as an empty list or empty string) or
numerically equivalent to 0 as false, thus the use of the term “falsy.”

```python
aquarium_tanks = [11, False, 18, 21, "", 12, 34, 0, [], {}]
filtered_tanks = filter(None, aquarium_tanks)
print(list(filtered_tanks))

# Output
[11, 25, 18, 21, 12, 34]
```


