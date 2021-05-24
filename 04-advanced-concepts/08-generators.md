# Generators

`generator` functions are a special kind of function that return a lazy iterator. These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory.

## File reading memory error with normal function

```python
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

csv_gen = csv_reader("some_csv.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")
```

```python
Traceback (most recent call last):
  File "ex1_naive.py", line 22, in <module>
    main()
  File "ex1_naive.py", line 13, in main
    csv_gen = csv_reader("file.txt")
  File "ex1_naive.py", line 6, in csv_reader
    result = file.read().split("\n")
MemoryError
```

In this case, `open()` returns a generator object that you can lazily iterate through line by line. However, `file.read().split()` loads everything into memory at once, causing the `MemoryError`.

Before that happens, you’ll probably notice your computer slow to a crawl. You might even need to kill the program with a KeyboardInterrupt. So, how can you handle these huge data files? Take a look at a new definition of `csv_reader()`:

## File reading through generator function

```python
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```

```python
>>> Row count is 64186394
```

## Building Generators With Generator Expressions

```python
>>> nums_squared_lc = [num**2 for num in range(5)]
>>> nums_squared_gc = (num**2 for num in range(5))
```
```python
>>> nums_squared_lc
[0, 1, 4, 9, 16]
>>> nums_squared_gc
<generator object <genexpr> at 0x107fbbc78>
```

## Using Advanced Generator Methods

* .send()
* .throw()
* .close()

### How to Use .throw()

.throw() allows you to throw exceptions with the generator. In the below example, you raise the exception in line 6. This code will throw a ValueError once digits reaches 5:

```python
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))
```

```python
11
111
1111
10101
Traceback (most recent call last):
  File "advanced_gen.py", line 47, in <module>
    main()
  File "advanced_gen.py", line 41, in main
    pal_gen.throw(ValueError("We don't like large palindromes"))
  File "advanced_gen.py", line 26, in infinite_palindromes
    i = (yield num)
ValueError: We don't like large palindromes
```

### How to Use .close()

As its name implies, .close() allows you to stop a generator. This can be especially handy when controlling an infinite sequence generator. Let’s update the code above by changing .throw() to .close() to stop the iteration:

```python
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()
    pal_gen.send(10 ** (digits))
```

```python
11
111
1111
10101
Traceback (most recent call last):
  File "advanced_gen.py", line 46, in <module>
    main()
  File "advanced_gen.py", line 42, in main
    pal_gen.send(10 ** (digits))
StopIteration
```