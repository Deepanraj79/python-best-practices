# Why use Exceptions?

They not only help solve popular problems like race conditions but are also very useful in controlling errors in areas like loops, file handling, database communication, network access and so on.

# Why use Try-Except/Try-Except-else Clause?

With the help of try-except and try-except-else, you can avoid many unknown problems that could arise from your code.

# Raising exceptions 

It means you can throw or raise an exception whenever it is needed. You can do it simply by calling [raise Exception(‘Test error!’)] from your code. Once raised, the exception will stop the current execution as usual and will go further up in the call stack until handled.

# How to Best Use Try-Except in Python

## How to handle an arbitrary exception

Sometimes, you may need a way to allow any arbitrary exception and also want to be able to display the error or exception message.

It is easily achievable using the Python exceptions. Check the below code. While testing, you can place the code inside the try block in the below example.

```python
try:
    #your code
except Exception as ex:
    print(ex)
```

## Catch multiple exceptions in one except block

You can catch multiple exceptions in a single except block. See the below example.

```python
except (Exception1, Exception2) as err:
    pass
```

## Handling multiple exceptions with one except block

There are many ways to handle multiple exceptions. The first of them requires placing all the exceptions which are likely to occur in the form of a tuple. Please see from below.

```python
try:
    file = open('input-file', 'open mode')
except (IOError, EOFError) as err:
    print("Testing multiple exceptions. {}".format(err.args[-1]))
```

The next method is to handle each exception in a dedicated except block. You can add as many except blocks as needed. See the below example.

```python
try:
    file = open('input-file', 'open mode')
except EOFError as err:
    print("Caught the EOF error.")
    raise err
except IOError as err:
    print("Caught the I/O error.")
    raise err
```

The last but not the least is to use the except without mentioning any exception attribute

```python
try:
    file = open('input-file', 'open mode')
except:
    # In case of any unhandled error, throw it away
    raise
```

This method can be useful if you don’t have any clue about the exception possibly thrown by your program.

## Re-raising exceptions in Python

Exceptions once raised keep moving up to the calling methods until handled. Though you can add an except clause which could just have a [raise] call without any argument. It’ll result in reraising the exception.

```python
try:
    # Intentionally raise an exception.
    raise Exception('I learn Python!')
except:
    print("Entered in except.")
    # Re-raise the exception.
    raise
```

**Output:**

```python
Entered in except.
Traceback (most recent call last):
  File "python", line 3, in <module>
Exception: I learn Python!
```

## When to use the else clause

Use an else clause right after the try-except block. The else clause will get hit only if no exception is thrown. The else statement should always precede the except blocks.

In else blocks, you can add code which you wish to run when no errors occurred.

See the below example. In this sample, you can see a while loop running infinitely. The code is asking for user input and then parsing it using the built-in [int()] function. If the user enters a zero value, then the except block will get hit. Otherwise, the code will flow through the else block.

```python
while True:
    # Enter integer value from the console.
    x = int(input())

    # Divide 1 by x to test error cases
    try:
        result = 1 / x
    except:
        print("Error case")
        exit(0)
    else:
        print("Pass case")
        exit(1)
```

## Make use of [finally clause]

If you have a code which you want to run in all situations, then write it inside the [finally block]. Python will always run the instructions coded in the [finally block]. It is the most common way of doing clean up tasks. You can also make sure the clean up gets through.

An error is caught by the try clause. After the code in the except block gets executed, the instructions in the [finally clause] would run.

Please note that a [finally block] will ALWAYS run, even if you’ve returned ahead of it.

See the below example.

```python
try:
    # Intentionally raise an error.
    x = 1 / 0
except:
    # Except clause:
    print("Error occurred")
finally:
    # Finally clause:
    print("The [finally clause] is hit")
```

**Output:**

```python
Error occurred
The [finally clause] is hit
```

## Use the As keyword to catch specific exception types

With the help of as <identifier>, you can create a new object. And you can also the exception object. Here, the below example, we are creating the IOError object and then using it within the clause.

```python
try:
    # Intentionally raise an error.
    f = open("no-file")
except IOError as err:
    # Creating IOError instance for book keeping.
    print("Error:", err)
    print("Code:", err.errno)
```

**Output:**

```python
('Error:', IOError(2, 'No such file or directory'))
('Code:', 2)
```

## Best practice for manually raising exceptions

Avoid raising generic exceptions because if you do so, then all other more specific exceptions have to be caught also. Hence, the best practice is to raise the most specific exception close to your problem.

**Bad example.**

```python
def bad_exception():
    try:
        raise ValueError('Intentional - do not want this to get caught')
        raise Exception('Exception to be handled')
    except Exception as error:
        print('Inside the except block: ' + repr(error))
        
bad_exception()
```

```python
Inside the except block: ValueError('Intentional - do not want this to get caught',)
```

**Best Practice:**

Here, we are raising a specific type of exception, not a generic one. And we are also using the args option to print the incorrect arguments if there is any. Let’s see the below example.

```python
try:
    raise ValueError('Testing exceptions: The input is in incorrect order', 'one', 'two', 'four') 
except ValueError as err:
    print(err.args)
```

```python
('Testing exceptions: The input is in incorrect order', 'one', 'two', 'four')
```

## How to skip through errors and continue execution

Ideally, you shouldn’t be doing this. But if you still want to do, then follow the below code to check out the right approach.

```python
try:
    assert False
except AssertionError:
    pass
print('Welcome to Prometheus!!!')
```

```python
Welcome to Prometheus!!!
```

# Tips

* Write custom exceptions - 
Generally, the only times you should be defining your own exceptions are when you have a specific case where raising a custom exception would be more appropriate than raising a existing Python exception.

```python
class NoInternetConnection(Exception):
    """Exception raised when there is no internet"""
```

* Do Use Inbuilt Exceptions

* Always try to Catch Specific Exceptions(ValueError, TypeError, MemoryError) 
  instead of 
  just general exception (Exception)

* In some cases we can use general exception. However, Address more specific 
  exceptions before more general ones,

```python
try:
    ...
except ValueError...:
    # handle exception
except KeyError...:
    # handle another exception
except Exception:
    # handle general exception
```

