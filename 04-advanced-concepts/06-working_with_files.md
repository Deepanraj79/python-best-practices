## Directory Listing in Legacy Python Versions

In versions of Python prior to Python 3, `os.listdir()` is the method to use to get a directory listing:

```python
>>> import os
>>> entries = os.listdir('my_directory/')

>>> os.listdir('my_directory/')
['sub_dir_c', 'file1.py', 'sub_dir_b', 'file3.txt', 'file2.csv', 'sub_dir']

>>> entries = os.listdir('my_directory/')
>>> for entry in entries:
...     print(entry)
...
...
sub_dir_c
file1.py
sub_dir_b
file3.txt
file2.csv
sub_dir
```

## Directory Listing in Modern Python Versions

In modern versions of Python, an alternative to `os.listdir()` is to use `os.scandir()` and `pathlib.Path()`.

`os.scandir()` was introduced in `Python 3.5` and is documented in PEP 471. `os.scandir()` returns an iterator as
opposed to a list when called:

```python
>>> import os
>>> entries = os.scandir('my_directory/')
>>> entries
<posix.ScandirIterator object at 0x7f5b047f3690>
```

```python
import os

with os.scandir('my_directory/') as entries:
    for entry in entries:
        print(entry.name)
```

```python
from pathlib import Path

entries = Path('my_directory/')
for entry in entries.iterdir():
    print(entry.name)
```

## Listing All Files in a Directory

```python
import os

# List all files in a directory using os.listdir
basepath = 'my_directory/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)
```

```python
import os

# List all files in a directory using scandir()
basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
```

```python
from pathlib import Path

basepath = Path('my_directory/')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)
```

## Listing Subdirectories

```python
import os

# List all subdirectories using os.listdir
basepath = 'my_directory/'
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(entry)
```

```python
import os

# List all subdirectories using scandir()
basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)
```

```python
from pathlib import Path

# List all subdirectory using pathlib
basepath = Path('my_directory/')
for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)
```

## Getting File Attributes

The examples below show how to get the time the files in `my_directory/` were last modified. The output is in seconds:

```python
>>> import os
>>> with os.scandir('my_directory/') as dir_contents:
...     for entry in dir_contents:
...         info = entry.stat()
...         print(info.st_mtime)
...
1539032199.0052035
1539032469.6324475
1538998552.2402923
1540233322.4009316
1537192240.0497339
1540266380.3434134
```

```python
>>> from pathlib import Path
>>> current_dir = Path('my_directory')
>>> for path in current_dir.iterdir():
...     info = path.stat()
...     print(info.st_mtime)
...
1539032199.0052035
1539032469.6324475
1538998552.2402923
1540233322.4009316
1537192240.0497339
1540266380.3434134
```

## Making Directories

### Creating a Single Directory

```python
import os

os.mkdir('example_directory/')
```

```python
from pathlib import Path

p = Path('example_directory/')
p.mkdir()
```

If the path already exists, `mkdir()` raises a `FileExistsError`:

```python
from pathlib import Path

p = Path('example_directory')
try:
    p.mkdir()
except FileExistsError as exc:
    print(exc)
```
Alternatively, you can ignore the `FileExistsError` by passing the `exist_ok=True` argument to .mkdir():

```python
from pathlib import Path

p = Path('example_directory')
p.mkdir(exist_ok=True)
```

###Creating Multiple Directories

```python
import os


os.makedirs('2018/10/05')
```

```python
$ tree -p -i .
.
[drwxrwx---]  2018
[drwxrwx---]  10
[drwxrwx---]  05
```

```python
import pathlib

p = pathlib.Path('2018/10/05')
p.mkdir(parents=True)
```

## Filename Pattern Matching

### Using String Methods
Two of these methods, `.startswith()` and `.endswith()`, are useful when you’re searching for patterns in filenames.

```python
>>> import os

>>> # Get .txt files
>>> for f_name in os.listdir('some_directory'):
...     if f_name.endswith('.txt'):
...         print(f_name)
```
###Simple Filename Pattern Matching Using fnmatch
String methods are limited in their matching abilities. `fnmatch` has more advanced functions and methods for pattern
matching. We will consider `fnmatch.fnmatch()`, a function that supports the use of wildcards such as * and ? to match
filenames. For example, in order to find all `.txt` files in a directory using `fnmatch`, you would do the following:

```python
>>> import os
>>> import fnmatch

>>> for file_name in os.listdir('some_directory/'):
...     if fnmatch.fnmatch(file_name, '*.txt'):
...         print(file_name)
```

###More Advanced Pattern Matching

Let’s suppose you want to find .txt files that meet certain criteria. For example, you could be only interested in
finding `.txt` files that contain the word data, a number between a set of underscores, and the word backup in their
filename. Something similar to `data_01_backup`, `data_02_backup`, or `data_03_backup`.

Using fnmatch.fnmatch(), you could do it this way:

```python
>>> for filename in os.listdir('.'):
...     if fnmatch.fnmatch(filename, 'data_*_backup.txt'):
...         print(filename)
```

### Filename Pattern Matching Using glob

Another useful module for pattern matching is glob.

.glob() in the glob module works just like fnmatch.fnmatch(), but unlike fnmatch.fnmatch(), it treats files beginning with a period (.) as special.

```python
>>> import glob
>>> glob.glob('*.py')
['admin.py', 'tests.py']
```
`glob.glob('*.py')` searches for all files that have the `.py` extension in the current directory and returns them as a
list. glob also supports shell-style wildcards to match patterns:

```python
>>> import glob
>>> for name in glob.glob('*[0-9]*.txt'):
...     print(name)
```

`glob` makes it easy to search for files `recursively` in subdirectories too:

```python
>>> import glob
>>> for file in glob.iglob('**/*.py', recursive=True):
...     print(file)
```

`pathlib` contains similar methods for making flexible file listings. The example below shows how you can use
`.Path.glob()` to list file types that start with the letter `p`:

```python
>>> from pathlib import Path
>>> p = Path('.')
>>> for name in p.glob('*.p*'):
...     print(name)

admin.py
scraper.py
docs.pdf
```

##Traversing Directories and Processing Files
A common programming task is walking a directory tree and processing files in the tree. Let’s explore how the built-in
Python function os.walk() can be used to do this. `os.walk()` is used to generate filename in a directory tree by walking the tree either top-down or bottom-up.

`os.walk()` defaults to traversing directories in a top-down manner:

```python
# Walking a directory tree and printing the names of the directories and files
for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)
```

To traverse the directory tree in a bottom-up manner, pass in a `topdown=False` keyword argument to os.walk():
```python
for dirpath, dirnames, files in os.walk('.', topdown=False):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)
```

## Making Temporary Files and Directories
Python provides a handy module for creating temporary files and directories called `tempfile`.

```python
from tempfile import TemporaryFile
with TemporaryFile('w+t') as fp:
    fp.write('Hello universe!')
    fp.seek(0)
    fp.read()
# File is now closed and removed
```

## Deleting Files and Directories

You can delete single files, directories, and entire directory trees using the methods found in the `os, shutil, and
pathlib` modules. The following sections describe how to delete files and directories that you no longer need.

### Deleting Files in Python

To delete a single file, use `pathlib.Path.unlink()`, `os.remove()`. or `os.unlink()`.

```python
import os

data_file = 'home/data.txt'

# If the file exists, delete it
if os.path.isfile(data_file):
    os.remove(data_file)
else:
    print(f'Error: {data_file} not a valid filename')
```

```python
import os

data_file = 'home/data.txt'

# Use exception handling
try:
    os.remove(data_file)
except OSError as e:
    print(f'Error: {data_file} : {e.strerror}')
```

```python
from pathlib import Path

data_file = Path('home/data.txt')

try:
    data_file.unlink()
except IsADirectoryError as e:
    print(f'Error: {data_file} : {e.strerror}')
```

### Deleting Single Directory

To delete a single directory or folder, use `os.rmdir()` or `pathlib.rmdir()`. 

```python
import os

trash_dir = 'my_documents/bad_dir'

try:
    os.rmdir(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
```

```python
from pathlib import Path

trash_dir = Path('my_documents/bad_dir')

try:
    trash_dir.rmdir()
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
```

### Deleting Entire Directory Trees
To delete non-empty directories and entire directory trees, Python offers `shutil.rmtree()`:

```python
import shutil

trash_dir = 'my_documents/bad_dir'

try:
    shutil.rmtree(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
```

## Copying, Moving, and Renaming Files and Directories

Python ships with the `shutil` module. shutil is short for shell utilities. It provides a number of high-level
operations on files to support copying, archiving, and removal of files and directories. In this section, you’ll learn
how to move and copy files and directories.

## Archiving

Archives are a convenient way to package several files into one. The two most common archive types are ZIP and TAR.
The Python programs you write can create, read, and extract data from archives.

The `zipfile` and `tarfile` module is a low level module that is part of the Python Standard Library. It is used to perform the
Archive operation.
