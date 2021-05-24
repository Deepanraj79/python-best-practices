# Check the memory of your python objects
When you create variables or data frames in python, often it becomes challenging if you are allocating a lot of data
into the variable. It is advised that you efficiently check the memory of your variables while writing your code,
so that you know how to deal with those variables. You can use the following code to see the memory of your objects.

```python
import sys
test_list = [x for x in range(0, 100000)]
print(sys.getsizeof(test_list))
```

# Return multiple values from Functions

```python
def get_product(id):
    # fetch product details from the database
    # some code here
    return name, category
 
name, category = get_product(101)
```

# Call external function from list comprehension

```python
def some_function(a):
    return (a + 5) / 2
    
my_formula = [some_function(i) for i in range(10)]
```
