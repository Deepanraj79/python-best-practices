# Line Continuations
When a logical line of code is longer than the accepted limit, you need to split it over multiple physical lines.

## Bad

```python
my_very_big_string = """For a long time I used to go to bed early. Sometimes, \
    when I had put out my candle, my eyes would close so quickly that I had not even \
    time to say “I’m going to sleep.”"""

from some.deep.module.inside.a.module import a_nice_function, another_nice_function, \
    yet_another_nice_function
```

## Good
```python
my_very_big_string = (
    "For a long time I used to go to bed early. Sometimes, "
    "when I had put out my candle, my eyes would close so quickly "
    "that I had not even time to say “I’m going to sleep.”"
)

from some.deep.module.inside.a.module import (
    a_nice_function, another_nice_function, yet_another_nice_function)
```

# Create an ignored variable

If you need to assign something (for instance, in Unpacking) but will not need that variable, use `_` or use `__`:

```python
filename = 'foobar.txt'
basename, _, ext = filename.rpartition('.')
```

The issue is that “_” is commonly used as an alias for the gettext() function, and is also used at the interactive
prompt to hold the value of the last operation
```python
filename = 'foobar.txt'
basename, __, ext = filename.rpartition('.')
```

Example of gettext,

```python
import gettext
gettext.bindtextdomain('myapplication', '/path/to/my/language/directory')
gettext.textdomain('myapplication')
_ = gettext.gettext
# ...
print(_('This is a translatable string.'))
```

# Quick Snippet

## Find a length of each element in a array

```python
>>> list(map(len, ['abc', 'de', 'fghi']))
[3, 2, 4]
```

