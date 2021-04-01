# Integers

# In Python, you can’t use commas to group digits in integer literals, but you can use underscores (_)

print(1000000)
print(1_000_000)

# Floating point numbers

print(1000000.0)  # 1000000.0
print(1_000_000.0)  # 1000000.0

# Floating point using Exponential notation - E notation

print(1e6)  # 1000000.0

# Python also uses E notation to display large floating-point numbers:

print(200000000000000000.0)  # 2e+17

# When you reach the maximum floating-point number, Python returns a special float value, inf:

print(2e308)  # inf


# Math Functions and Number Methods

'''
1. round(), for rounding numbers to some number of decimal places
2. abs(), for getting the absolute value of a number
3. pow(), for raising a number to some power
'''


# round()

'''
>>> round(2.3)
2

>>> round(2.7)
3

round() has some unexpected behavior when the number ends in .5: Python 3 rounds numbers according to a
strategy called rounding ties to even. A tie is any number whose last digit is five. If that digit is even, then you
round down. If the digit is odd, then you round up.

>>> round(2.5)
2

>>> round(3.5)
4

You can round a number to a given number of decimal places by passing a second argument to round():

>>> round(3.14159, 3)
3.142

>>> round(2.71828, 2)
2.72

The second argument of round() must be an integer. If it isn’t, then Python raises a TypeError:

>>> round(2.65, 1.4)

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    round(2.65, 1.4)
TypeError: 'float' object cannot be interpreted as an integer
'''


# abs

'''
abs() always returns a positive number of the same type as its argument. That is, the absolute value of an
integer is always a positive integer, and the absolute value of a float is always a positive float.

>>> abs(3)
3

>>> abs(-5.0)
5.0
'''

# pow

'''
pow() takes two arguments. The first argument is the base, or the number to be raised to a power, and the
second argument is the exponent, or the power to which the number is to be raised.

>>> pow(2, 3)
8

Also the pow() accepts third optional argument. First, 2 is raised to the power 3 to get 8. Then 8 % 2 is calculated,
which is 0 because 2 divides 8 with no remainder.

>>> pow(2, 3, 2)
0

'''

# Check if a Float Is integral

'''
>>> num = 2.5
>>> num.is_integer()
False

>>> num = 2.0
>>> num.is_integer()
True
'''

# Print the number in style

'''
You can do this with f-strings by surrounding a variable assigned to a number with curly braces

>>> n = 7.125
>>> f"The value of n is {n}"
'The value of n is 7.125'

>>> n = 7.125
>>> f"The value of n is {n:.2f}"
'The value of n is 7.12'

>>> n = 7.126
>>> f"The value of n is {n:.2f}"
'The value of n is 7.13'

>>> n = 1
>>> f"The value of n is {n:.2f}"
'The value of n is 1.00'
>>> f"The value of n is {n:.3f}"
'The value of n is 1.000'

'''