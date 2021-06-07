# Nested function/Inner function/Closures

An inner function is simply a function that is defined inside another function.
The inner function is able to access the variables that have been defined
within the scope of the outer function, but it cannot change them.

There are a  number of reasons as to why we may need to create an inner 
function.  For instance, an inner function is protected from what happens 
outside it. Inner functions are also a good way of creating closures in 
Python.

# Defining a nester function

```python
#defining nested function
def outer(message):
    #text is having the scope of outer function
    text = message
    def inner():
        #using non-local variable text
        print(text)
    #return inner function
    return inner 

# main method
if __name__=='__main__':
    func = outer('Hello!')
    func()
```

In the above example, we have used a closure to access `inner()` function out of its scope, as the `inner()` function is only available inside the `outer()` function but by returning it, we can access it outside the `outer()` function.


# Why use Inner Functions?

## Encapsulation

A function can be created as an inner function in order to protect it from everything that is happening outside of the function. In that case, the function will be hidden from the global scope. Here is an example:

```python
def outer_function(x):
    # Hidden from the outer code
    def inner_increment(x):
        return x + 2
    y = inner_increment(x)
    print(x, y)

inner_increment(5)
#outer_function(5)
```

```python
Traceback (most recent call last):
  File "C:/Users/admin/inner.py", line 7, in <module>
    inner_increment(5)
NameError: name 'inner_increment' is not defined
```

In the above code, we are trying to call the `inner_increment()` function, but instead we got an error.

Now, comment out the call to `inner_increment()` and uncomment the call to `outer_function()` as shown below:

```python
def outer_function(x):
    # Hidden from the outer code
    def inner_increment(x):
        return x + 2
    y = inner_increment(x)
    print(x, y)

#inner_increment(5)
outer_function(5)`

>>> 5 7
```

The script above shows that the inner function, that is, `inner_increment()` is protected from what is happening outside it since the variable `x` inside the inner_increment function is not affected by the value passed to the parameter `x` of the `outer function`. In other words, the variables inside the inner function is `not accessible outside` it. There is a great advantage with such a design pattern. After checking all arguments in the outer function, we can safely skip error checking within the inner function.

## Closures and Factory Functions

We can bind/pass data to a function without necessarily passing the data to the function via parameters. This is done using a closure. It is a function object that is able to remember values in the enclosing scopes even when they are not available in the memory. This means that we have a closure when a nested function references a value that is in its enclosing scope.

The purpose of a closure is to make the inner function remember the state of its environment when it is called, even if it is not in the memory. A closure is caused by an inner function, but it's not the inner function. The closure works by closing the local variable on the stack, which stays around after the creation of the stack has finished executing.

The following are the conditions that are required to be met in order to create a closure in Python:

* There must be a nested function
* The inner function has to refer to a value that is defined in the 
  enclosing scope
* The enclosing function has to return the nested function

Consider the following example:

```python
def function1(name):
    def function2():
        print('Hello ' + name)
    return function2

func = function1('Nicholas')
func()
```

```python
# Output
Hello Nicholas
```

The above code demonstrates that with closures, we are able to generate and invoke a function from outside its scope via function passing. The scope of `function2()` is only inside `function1()`. However, with the use of closures, it was possible for us to extend this scope and invoke it from outside its scope.

Inner functions help us in defining factory functions. A factory function is a function that creates another object. For example:

```python
def power_generator(num):

    # Create the inner function
    def power_n(power):
        return num ** power

    return power_n

power_two = power_generator(2)
power_three = power_generator(3)
print(power_two(8))
print(power_three(4))
```

```python
# Output

256
81
```

In the script above, from the `power_n(power)` function, we have created two other objects, `power_two` and `power_three`. This makes `power_n(power)` a factory function since it generates the `power_two` and `power_three` functions for us using the parameter we pass it.