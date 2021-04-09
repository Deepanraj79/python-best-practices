'''Points to be considered in Dictionary

References:
https://towardsdatascience.com/15-things-you-should-know-about-dictionaries-in-python-44c55e75405c
'''

population = {'Berlin': 3748148, 'Hamburg': 1822445, 'Munich': 1471508, 'Cologne': 1085664, 'Frankfurt': 753056 }

# dictionary containing a list of products' prices
products = {'table': 120, 'chair': 40, 'lamp': 14, 'bed': 250, 'mattress': 100}

# dictionary containing students grades
grades = {'Alba': 9.5, 'Eduardo': 10, 'Normando': 3.5, 'Helena': 6.5, 'Claudia': 7.5}


# Create a dictionary with dict() constructor

'''
students_ages = dict(Amanda=27, Teresa=38, Paula=17, Mario=40)

print(students_ages)
# {'Amanda': 27, 'Teresa': 38, 'Paula': 17, 'Mario': 40}
'''

# We can also create a dictionary using another dictionary in combination with keyword arguments

'''
students_ages = dict({'Amanda': 27, 'Teresa': 38}, Paula=17, Mario=40)

print(students_ages)
# {'Amanda': 27, 'Teresa': 38, 'Paula': 17, 'Mario': 40}
'''


# Dictionary from iterable

'''
Alternatively, we can construct a dictionary using an iterable (e.g. list of tuples).
Each tuple must contain two objects.

students_ages = dict([('Amanda', 27), ('Teresa', 38), ('Paula', 17), ('Mario', 40)])
print(students_ages)
# {'Amanda': 27, 'Teresa': 38, 'Paula': 17, 'Mario': 40}
'''


# Create a dictionary using two lists.

'''
First, we have to build an iterator of tuples using zip(*iterables) function. Then, we employ
the dict([iterable, **kwarg]) function to construct the dictionary

# create a dictionary using two list
students = ['Amanda', 'Teresa', 'Paula', 'Mario']
ages = [27, 38, 17, 40]

# zip method --> iterator of tuples --> dict method --> dictionary
students_ages = dict(zip(students, ages))

print(students_ages)
# {'Amanda': 27, 'Teresa': 38, 'Paula': 17, 'Mario': 40}
'''

# Dictionary methods

# .get()

'''
# access population of Stuttgart using .get() method without default value
print(population.get('Stuttgart'))
# None

# access population of Stuttgart using .get() method with default value
print(population.get('Stuttgart', 'Not found'))
'''

# .update()

'''
# add shelf and sofa to the products dictionary using another dictionary object
products.update({'shelf': 70, 'sofa': 300})


# add three new items to the grades dictionary using keyword arguments
grades.update(Violeta=5.5, Marco=6.5, Paola=8)

# add two cities to the population dictionary using a list of tuples
population.update([('Stuttgart', 632743), ('Dusseldorf', 617280)])

'''


# .pop()

'''
# key exists - the item is removed and the value returned
population.pop('Stuttgart')


'''