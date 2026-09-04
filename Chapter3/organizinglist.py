# Now we will learn how to organize a list


# with sort() method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)


# reverse order

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print(cars)


# temorarily sorting with sorted method

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again")
print(cars)


'''
Sorting a list alphabetically is a bit more complicated when all the values are not in
lowercase. There are several ways to interpret capital letters when you’re deciding on
a sort order, and specifying the exact order can be more complex than we want to deal
with at this time. However, most approaches to sorting will build directly on what you
learned in this section.
'''

# Printing a list in Reverse Order

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# Finding the length of the list

print(len(cars))

"Python counts the items in a list starting with one, so you shouldn’t run into any offby-one errors when determining the length of a list."

