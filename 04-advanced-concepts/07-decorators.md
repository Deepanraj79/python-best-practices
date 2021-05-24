## Decorators
By definition, a decorator is a function that takes another function and extends the behavior of the latter function
without explicitly modifying it.

## Simple Decorator
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
```

## Reusing Decorators

```python
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

from decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")
```

```python
>>> say_whee()
Whee!
Whee!
```

## Identity of the function after we decorate it

```python
>>> say_whee
<function do_twice.<locals>.wrapper_do_twice at 0x7f43700e52f0>

>>> say_whee.__name__
'wrapper_do_twice'

>>> help(say_whee)
Help on function wrapper_do_twice in module decorators:

wrapper_do_twice()
```

However, after being decorated, `say_whee()` has gotten very confused about its identity. It now reports being the wrapper_do_twice() inner function inside the do_twice() decorator. Although technically true, this is not very useful information.

To fix this, decorators should use the `@functools.wraps` decorator, which will preserve information about the original function. Update decorators.py again:

```python
import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```

```python
>>> say_whee
<function say_whee at 0x7ff79a60f2f0>

>>> say_whee.__name__
'say_whee'

>>> help(say_whee)
Help on function say_whee in module whee:

say_whee()
```

## Example - Timer

```python
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
```

```python
>>> waste_some_time(1)
Finished 'waste_some_time' in 0.0010 secs

>>> waste_some_time(999)
Finished 'waste_some_time' in 0.3260 secs
```

## Example - Slowing Down Code

```python
import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
```

```python
>>> countdown(3)
3
2
1
Liftoff!
```

## Registering Plugins

Decorators don’t have to wrap the function they’re decorating. They can also simply register that a function exists and return it unwrapped. This can be used, for instance, to create a light-weight plug-in architecture:

```python
import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
```

```python
>>> PLUGINS
{'say_hello': <function say_hello at 0x7f768eae6730>,
 'be_awesome': <function be_awesome at 0x7f768eae67b8>}

>>> randomly_greet("Alice")
Using 'say_hello'
'Hello Alice'
```

## Is the User Logged In?
The final example before moving on to some fancier decorators is commonly used when working with a web framework. In this example, we are using Flask to set up a /secret web page that should only be visible to users that are logged in or otherwise authenticated:

```python
from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    ...
```

## Decorating Classes

There are two different ways you can use decorators on classes. The first one is very close to what you have already done with functions: you can decorate the methods of a class. This was one of the motivations for introducing decorators back in the day.

Some commonly used decorators that are even built-ins in Python are `@classmethod, @staticmethod, and @property`. The @classmethod and @staticmethod decorators are used to define methods inside a class namespace that are not connected to a particular instance of that class. The @property decorator is used to customize getters and setters for class attributes. Expand the box below for an example using these decorators.

### Decorating methods

```python
from decorators import debug, timer

class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
```

```python
>>> tw = TimeWaster(1000)
Calling __init__(<time_waster.TimeWaster object at 0x7efccce03908>, 1000)
'__init__' returned None

>>> tw.waste_time(999)
Finished 'waste_time' in 0.3376 secs
```

### Decorating class

```python
from decorators import timer

@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
```

```python
>>> tw = TimeWaster(1000)
Finished 'TimeWaster' in 0.0000 secs

>>> tw.waste_time(999)
>>>
```

## Nesting Decorators

```python
from decorators import debug, do_twice

@debug
@do_twice
def greet(name):
    print(f"Hello {name}")
```

```python
>>> greet("Eva")
Calling greet('Eva')
Hello Eva
Hello Eva
'greet' returned None
```

## Decorators With Arguments

```python
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat
```

```python
@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")
```

## Stateful Decorators
Sometimes, it’s useful to have a decorator that can keep track of state. As a simple example, we will create a decorator that counts the number of times a function is called.

```python
import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")
```

```python
>>> say_whee()
Call 1 of 'say_whee'
Whee!

>>> say_whee()
Call 2 of 'say_whee'
Whee!

>>> say_whee.num_calls
2
```

## Classes as Decorators

```python
class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")
```
The .__call__() method is executed each time you try to call an instance of the class:

```python
>>> counter = Counter()
>>> counter()
Current count is 1

>>> counter()
Current count is 2

>>> counter.count
2
```

Therefore, a typical implementation of a decorator class needs to implement .__init__() and .__call__():

```python
import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")
```

```python
>>> say_whee()
Call 1 of 'say_whee'
Whee!

>>> say_whee()
Call 2 of 'say_whee'
Whee!

>>> say_whee.num_calls
2
```

## Creating Singletons

A singleton is a class with only one instance. There are several singletons in Python that you use frequently, including None, True, and False. It is the fact that None is a singleton that allows you to compare for None using the is keyword, like you saw in the Both Please section:

```python
if _func is None:
    return decorator_name
else:
    return decorator_name(_func)
```

The following `@singleton decorator` turns a class into a singleton by storing the first instance of the class as an attribute. Later attempts at creating an instance simply return the stored instance:

```python
import functools

def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass
```

```python
>>> first_one = TheOne()
>>> another_one = TheOne()

>>> id(first_one)
140094218762280

>>> id(another_one)
140094218762280

>>> first_one is another_one
True
```

## Validating JSON

```python
from flask import Flask, request, abort
import functools
app = Flask(__name__)

def validate_json(*expected_args):                  # 1
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:      # 2
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper_validate_json
    return decorator_validate_json
```

```python
@app.route("/grade", methods=["POST"])
@validate_json("student_id")
def update_grade():
    json_data = request.get_json()
    # Update database.
    return "success!"
```
