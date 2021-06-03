# Read From a File
Use the with open syntax to read from files. This will automatically close files for you.

## Bad
```python
f = open('file.txt')
a = f.read()
print(a)
f.close()
```

## Good
```python
with open('file.txt') as f:
    for line in f:
        print(line)
```

# Reading

## Reading File in Chunks

The `read()` (without argument) and` readlines()` methods reads the all data into memory at once. So don't use them to
read large files.

A better approach is to read the file in `chunks` using the `read()` or read the file line by line using the
`readline()`, as follows:

Reading file in chunks,

```python
>>> f = open("poem.txt", "r")
>>>
>>> chunk = 200
>>>
>>> while True:
...     data = f.read(chunk)
...     if not data:
...         break
...     print(data)
...
The caged bird sings
with a fearful trill
of things unknown
but longed for still
```

# Writing

## Writing Data writelines()

```python
>>> lines = [
... "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod",
... "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"
... "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo",
... "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse",
... "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non",
... "proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
... ]
>>>
>>>
>>> f = open("lorem.txt", "w")
>>>
>>> f.writelines(lines)
>>>
>>> f.close()
```
