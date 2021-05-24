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

# Writing
