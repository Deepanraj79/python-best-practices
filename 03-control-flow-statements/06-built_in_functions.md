## dir

The dir function can be used for two things:

* Seeing a list of all your local variables
* Seeing a list of all attributes on a particular object

Here we can see that our local variables, right after starting a new Python shell and then after creating a new variable x:

```python
>>> dir()
['__annotations__', '__doc__', '__name__', '__package__']
>>> x = [1, 2, 3, 4]
>>> dir()
['__annotations__', '__doc__', '__name__', '__package__', 'x']

```

If we pass that x list into dir we can see all the attributes it has:

```python
>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

## property
The property function is a `decorator` and a descriptor (only click those weird terms if you’re extra curious) and it’ll likely seem somewhat magical when you first learn about it.

This decorator allows us to create an attribute which will always seem to contain the return value of a particular function call. It’s easiest to understand with an example.

Here’s a class that uses `property`:

```python
class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

```

```python
>>> circle = Circle()
>>> circle.diameter
2
>>> circle.radius = 5
>>> circle.diameter
10
```

## hasattr()

This function return True, if the defined object has the mentioned attribute, else it will return False.

```python
class Student:
  name = "Ann"
  age = 28
  country = "USA"

x = hasattr(Student, 'age')

print(x)

# output = True
```

## getattr

### Bad

```python
import module

if method == Constants.POST:
    external_response = post(url, path, params=params, json=json, headers=headers)
elif method == Constants.GET:
    external_response = get(url, path, params=params, json=json, headers=headers)
elif method == Constants.PUT:
    external_response = put(url, path, params=params, json=json, headers=headers)
elif method == Constants.DELETE:
    external_response = delete(url, path, params=params, json=json, headers=headers)
```

### Good

```python
import module

try:
    http_request = getattr(module, request.http_method)
    http_request(url, path, params=params, json=json, headers=headers)
except AttributeError:
    log.error('The module does contains the implementation for http method')
```

