# range(stop)

When you pass only one argument to the range(), it will generate a sequence of integers starting from 0 to stop -1.

```python
# Print first 10 numbers

# stop = 10
for i in range(10):
    print(i, end=' ')
# Output 0 1 2 3 4 5 6 7 8 9
```

# range(start, stop)

When you pass two arguments to the range(), it will generate integers starting from the `start` number to `stop-1`
```python
# Numbers from 10 to 15
# start = 10
# stop = 16
for i in range(10, 16):
    print(i, end=' ')
# Output 10 11 12 13 14 15
```

# range(start, stop, step)

When you pass all three arguments to the range(), it will return a sequence of numbers, starting from the start number, increments by step number, and stops before a stop number.

```python
# Numbers from 10 to 15
# start = 10
# stop = 50
# step = 5
for i in range(10, 50, 5):
    print(i, end=' ')
# Output 10 15 20 25 30 35 40 45
```

# Using negative `step`

```python
# reverse range using negative step
# start = 5
# stop = -1
# step = -1
for i in range(5, -1, -1):
    print(i)
```

# Using `reversed()` function

```python
for i in reversed(range(10, 21)):
    print(i, end=' ')
# Output 19 18 17 16 15 14 13 12 11 10
```

# range attributes

```python
range1 = range(0, 10)

# access range() attributes
print(range1.start)  # 0
print(range1.stop)  # 10
print(range1.step)  # 1
```

# Indexing and Slicing

```python
range1 = range(0, 10)

# first number (start number) in range
print(range1[0])


# access 5th number in range
print(range1[5])
# Output 5

# access last number
print(range1[range1.stop - 1])
# Output 9
```