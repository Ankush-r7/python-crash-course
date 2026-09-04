# List work well for storing sets of items that can change throughout the life of a program.

# But sometimes we want to create a list that we can't change in the future

# Tuples are immutable

# Python refers to values that cannot change as immutable and immutable ist is called tuple


# Defining Tuple

'''
A tuple looks just like a list except you use parentheses instead of square
brackets. Once you define a tuple, you can access individual elements by
using each item’s index, just as you would for a list.
'''

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 #n not supported
"TypeError: 'tuple' object does not support item assignment"


# Looping Through all values in a tuple

for dimension in dimensions:
    print(dimension)

# Writing over a Tuple

'''
Although you can’t modify a tuple, you can assign a new value to a variable
that holds a tuple. So if we wanted to change our dimensions, we could
redefine the entire tuple:
'''

dimensions = (200, 50)
print("Orginal dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)