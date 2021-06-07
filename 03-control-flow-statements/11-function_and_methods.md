# Functions
Functions are extremely useful because they allow a piece of code to be written
nce and then invoked in a single line wherever needed throughout your code.
You then only need to make improvements to one place in your code and if the 
function is well named then whoever reads through your code can easily infer
what the function does by looking at its name and arguments instead of reading
multiple lines of code.

## Simple function

```python
def add(a, b):
    result = a + b
    return result

sum = add(5, 7)
print(sum)
# 12
```

## Function with parameter

```python
def highest_number(numbers):
    highest = 0
    for n in numbers:
        if n > highest:
            highest = number

    return highest

scores = [21, 14, 72, 148, 54]
top_score = highest_number(scores)

print(top_score)
# 148
```

## Parameters & arguments

`Parameters` are specified in parenthesis when you're defining a function,
`arguments` are the data that you pass into the function's parameters when you
call the function.

In the case with the code above, `a` and `b` are the `parameters` for the 
`add()` function, whereas `5` and `7` are the `arguments` that are passed 
into the function when it is called


### Keyword arguments
Keyword arguments are liked named parameters, this is how you can define and use them:

```python
def greet(greeting, name=None):
    if name:
        print(greeting + " " + name)
    else:
        print(greeting + " there")

# Call function with keyword argument
greet('Hello', name='Alex')
# Hello Alex

# Call function without keyword argument
greet('Hello')
# Hello there
```
### *args

At some point, you may come across a function definition that has a strange looking parameter with an `*` prefix, like this:

```python
def throw_party(host, *args):
    print(host, 'is throwing a party!')
    for guest in guests:
        print(guest, 'has arrived.')
```

Basically, the `*` operator is used to handle an unknown number of arguments. You'd use this when you may have a situation where you could have a variable number of arguments that you'd want to handle. For example, now we can use this function with any number of guests:

```python
throw_party('Anika', 'Jethrow', 'Roxanne', 'Sadiyah', 'Andrei')

Anika is throwing a party!
Jethrow has arrived.
Roxanne has arrived.
Sadiyah has arrived.
Andrei has arrived.
```

You don't have to name this parameter as `*args`, it's just a typical convention that is used. You could just as well use `*guests` and your code would continue to work just the same.

### **kwargs

Similarly, you might see a function that makes use of a `**kwargs` parameter like this:

```python
def scoreboard(game, **kwargs):
    print(game, "scores:")
    for key, value in kwargs.items():
        print(key, value)
```

`**kwargs` is similar to *args except it is used to tell a function to 
accept any number of keyword arguments, which can be called like this


```python
scoreboard("Space Invaders", player_a=98, player_b=250, player_c=176)

Space Invaders scores:
player_a 98
player_b 250
player_c 176
```

## Best Practices

### Single responsibility principle

This means that your functions should only focus on handling a single aspect of your program.

### Naming your functions

A well-named function should almost read like a sentence when used. When someone is reading the code it should be immediately obvious what is happening in the code. A good rule of thumb is to design and name your function so that it can be used to simplify a more complex set of operations into a single expression.

```python
def increment(num, by):
    return num + by

result = increment(5, 2)
print(result)
# 7
```

### Docstrings

When you write your Python functions you can write docstrings to add inline documentation to your functions. They can be one-liners or multi-line docstrings.

```python
def add(arg1, arg2):
    """Basic doc string format of reStructuredText

    :param int arg1: Description of the argument 1
    :param str arg2: Description of the argument 2
    :return int: Addition of two number
    """
    return arg1 + arg2
```

### Organizing your functions

Once you start writing multiple functions for your Python project you should think about how you want to organise them.

If it's a simple project with only a few functions you may want to define them at the beginning of your Python module. If your project size is a bit bigger you may want to put them into their own module so that they can be imported into your code and used wherever. You may also want to create methods for classes. 

## General Tips

### Check the memory of your python objects
When you create variables or data frames in python, often it becomes challenging if you are allocating a lot of data
into the variable. It is advised that you efficiently check the memory of your variables while writing your code,
so that you know how to deal with those variables. You can use the following code to see the memory of your objects.

```python
import sys
test_list = [x for x in range(0, 100000)]
print(sys.getsizeof(test_list))
```

### Return multiple values from Functions

```python
def get_product(id):
    # fetch product details from the database
    # some code here
    return name, category
 
name, category = get_product(101)
```

### Call external function from list comprehension

```python
def some_function(a):
    return (a + 5) / 2
    
my_formula = [some_function(i) for i in range(10)]
```

