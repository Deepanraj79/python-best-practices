# Modules
The cool thing about modules written in Python is that they are exceedingly straightforward to build. All you need to do is create a file that contains legitimate Python code and then give the file a name with a .py extension. That’s it!

For example, suppose you have created a file called `mod.py` containing the following:

```python
s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass
```


## The Module Search Path

Continuing with the above example, let’s take a look at what happens when Python executes the statement:

```python
import mod
```

When the interpreter executes the above import statement, it searches for `mod.py` in a list of directories assembled from the following sources:

* The directory from which the input script was run or the current directory 
if the interpreter is being run interactively.
* The list of directories contained in the `PYTHONPATH` environment variable, 
if it is set. (The format for `PYTHONPATH` is OS-dependent but should mimic the `PATH` environment variable.)
* An installation-dependent list of directories configured at the time 
Python is installed.
  
The resulting search path is accessible in the Python variable `sys.path`, which is obtained from a module named `sys`:

```python
>>> import sys
>>> sys.path
['', 'C:\\Users\\john\\Documents\\Python\\doc', 'C:\\Python36\\Lib\\idlelib',
'C:\\Python36\\python36.zip', 'C:\\Python36\\DLLs', 'C:\\Python36\\lib',
'C:\\Python36', 'C:\\Python36\\lib\\site-packages']
```

Once a module has been imported, you can determine the location where it was found with the module’s `__file__` attribute:

```python
>>> import mod
>>> mod.__file__
'C:\\Users\\john\\mod.py'

>>> import re
>>> re.__file__
'C:\\Python36\\lib\\re.py'
```

## The import Statement

### `import <module_name>`

```python
import <module_name>
```

```python
>>> import mod
>>> mod
<module 'mod' from 'C:\\Users\\john\\Documents\\Python\\doc\\mod.py'>
>>> mod.s
'If Comrade Napoleon says it, it must be right.'
>>> mod.foo('quux')
arg = quux
```

### `from <module_name> import <name(s)>`

An alternate form of the import statement allows individual objects from the module to be imported directly into the caller’s symbol table:

```python
from <module_name> import <name(s)>
```

```python
>>> from mod import s, foo
>>> s
'If Comrade Napoleon says it, it must be right.'
>>> foo('quux')
arg = quux

>>> from mod import Foo
>>> x = Foo()
>>> x
<mod.Foo object at 0x02E3AD50>
```

```python
>>> a = ['foo', 'bar', 'baz']
>>> a
['foo', 'bar', 'baz']

>>> from mod import a
>>> a
[100, 200, 300]
```

### `from <module_name> import <name> as <alt_name>`

It is also possible to import individual objects but enter them into the local symbol table with alternate names:

```python
from <module_name> import <name> as <alt_name>[, <name> as <alt_name> …]
```

This makes it possible to place names directly into the local symbol table but avoid conflicts with previously existing names:

```python
>>> s = 'foo'
>>> a = ['foo', 'bar', 'baz']

>>> from mod import s as string, a as alist
>>> s
'foo'
>>> string
'If Comrade Napoleon says it, it must be right.'
>>> a
['foo', 'bar', 'baz']
>>> alist
[100, 200, 300]
```

### `import <module_name> as <alt_name>`

You can also import an entire module under an alternate name:

```python
import <module_name> as <alt_name>
```

```python
>>> import mod as my_module
>>> my_module.a
[100, 200, 300]
>>> my_module.foo('qux')
arg = qux
```

## The `dir()` Function

The built-in function dir() returns a list of defined names in a namespace. Without arguments, it produces an alphabetically sorted list of names in the current `local symbol table`:

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']

>>> qux = [1, 2, 3, 4, 5]
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'qux']

>>> class Bar():
...     pass
...
>>> x = Bar()
>>> dir()
['Bar', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'qux', 'x']
```

This can be useful for identifying what exactly has been added to the namespace by an import statement:

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']

>>> import mod
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'mod']
>>> mod.s
'If Comrade Napoleon says it, it must be right.'
>>> mod.foo([1, 2, 3])
arg = [1, 2, 3]

>>> from mod import a, Foo
>>> dir()
['Foo', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'a', 'mod']
>>> a
[100, 200, 300]
>>> x = Foo()
>>> x
<mod.Foo object at 0x002EAD50>

>>> from mod import s as string
>>> dir()
['Foo', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'a', 'mod', 'string', 'x']
>>> string
'If Comrade Napoleon says it, it must be right.'
```

```python
>>> import mod
>>> dir(mod)
['Foo', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__spec__', 'a', 'foo', 's']
```

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']
>>> from mod import *
>>> dir()
['Foo', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'a', 'foo', 's']
```

## Reloading a Module

If you make a change to a module and need to reload it, you need to either `restart the interpreter` or use a function called reload() from module `importlib`:

```python
>>> import mod
a = [100, 200, 300]

>>> import mod

>>> import importlib
>>> importlib.reload(mod)
a = [100, 200, 300]
<module 'mod' from 'C:\\Users\\john\\Documents\\Python\\doc\\mod.py'>
```


# Python Packages

Packages allow for a hierarchical structuring of the module namespace using dot notation. In the same way that modules help avoid collisions between global variable names, packages help avoid collisions between module names.

## The `import` statement

```python
from <package_name> import <modules_name>[, <module_name> ...]
from <package_name> import <module_name> as <alt_name>
```

```python
>>> from pkg import mod1
>>> mod1.foo()
[mod1] foo()

>>> from pkg import mod2 as quux
>>> quux.bar()
[mod2] bar()
```

## Package Initialization

If a file named `__init__.py` is present in a package directory, it is invoked when the package or a module in the package is imported. This can be used for execution of package initialization code, such as initialization of `package-level` data.

For example, consider the following `__init__.py` file:

```python
print(f'Invoking __init__.py for {__name__}')
A = ['quux', 'corge', 'grault']
```

Let’s add this file to the pkg directory from the above example:

![Alt text](../images/package.png?raw=true "Title")

Now when the package is imported, the global list A is initialized:

```python
>>> import pkg
Invoking __init__.py for pkg
>>> pkg.A
['quux', 'corge', 'grault']
```

`__init__.py` can also be used to effect automatic importing of modules from a package. For example, earlier you saw that the statement `import pkg` only places the name pkg in the caller’s local symbol table and doesn’t import any modules. But if `__init__.py` in the pkg directory contains the following:

```python
# __ini__.py

print(f'Invoking __init__.py for {__name__}')
import pkg.mod1, pkg.mod2
```

then when you execute import pkg, modules mod1 and mod2 are imported automatically:

```python
>>> import pkg
Invoking __init__.py for pkg
>>> pkg.mod1.foo()
[mod1] foo()
>>> pkg.mod2.bar()
[mod2] bar()
```

**Note,**
Starting with `Python 3.3,` Implicit Namespace Packages were introduced. These allow for the creation of a package `without any __init__.py` file. Of course, it can still be present if package initialization is needed. But it is no longer required.


## Importing `*` From a Package

![Alt text](../images/package.png?raw=true "Title")

```python
>>> from pkg import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']
```
The `*` It will import all the modules by default.  if the __init__.py file 
in the package directory contains a list named `__all__`, it is taken to be a
list of modules that should be imported when the statement `from <package_name> import *`
is encountered.

```python
# pkg/__init__.py

__all__ = [
        'mod1',
        'mod2',
        'mod3',
        'mod4'
        ]

```

Now from pkg `import *` imports all four modules:

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']

>>> from pkg import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'mod1', 'mod2', 'mod3', 'mod4']
>>> mod2.bar()
[mod2] bar()
>>> mod4.Qux
<class 'pkg.mod4.Qux'>
```

Using `import *` still `isn’t considered terrific form`, any more for packages than for modules. But this facility at least gives the creator of the package some control over what happens when import * is specified.

By the way, `__all__` can be defined in a `module` as well and serves the same purpose: to control what is imported with `import *`. For example, modify mod1.py as follows:

```python
# pkg/mod1.py

__all__ = ['foo']

def foo():
    print('[mod1] foo()')

class Foo:
    pass
```

Now an `import *` statement `from pkg.mod1` will only import what is contained in `__all__`:

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__']

>>> from pkg.mod1 import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
'__package__', '__spec__', 'foo']

>>> foo()
[mod1] foo()
>>> Foo
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    Foo
NameError: name 'Foo' is not defined
```

**In summary,** `__all__` is used by both packages and modules to control what 
is imported when `import *` is specified. But the default behavior differs:

* For a package, when __all__ is not defined, import * does not import 
  anything.
* For a module, when __all__ is not defined, import * imports everything 
  (except—you guessed it—names starting with an underscore).
  
## Subpackages

Packages can contain nested subpackages to arbitrary depth. For example, let’s make one more modification to the example package directory as follows:

![Alt text](../images/subpackages.webp?raw=true "Title")

Importing still works the same as shown previously. Syntax is similar, but additional dot notation is used to separate package name from subpackage name:

```python
>>> from pkg.sub_pkg1 import mod2
>>> mod2.bar()
[mod2] bar()

>>> from pkg.sub_pkg2.mod3 import baz
>>> baz()
[mod3] baz()

>>> from pkg.sub_pkg2.mod4 import qux as grault
>>> grault()
[mod4] qux()
```

