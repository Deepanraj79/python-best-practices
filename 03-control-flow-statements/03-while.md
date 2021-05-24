# `while` loop with `else` clause

```python
def while_else_demo():

    count = 0
    while count < 5 :
        num = int(input("Enter number between 0-100?"))
        if (num < 0) or (num > 100):
            print("Aborted while: You've entered an invalid number.")
            break
        count += 1
    else:
        print("While loop ended gracefully.")

while_else_demo()
```

# `while` loop with `break`

```python
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')
```

# 'while' loop with 'continue'

```python
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')
```