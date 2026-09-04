# In this we are going to learn about some of the very import list methods


# by using this mehtods we can do various things with our list like changing it, adding something in it or removing som elements

# Ok, then let's start it 

# First is modifying the elements in the list


# It is pretty simple 

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

motorcycles[0] = 'ducati'

print(motorcycles)


# Adding a element in the list 

# appending elements to the end of the list 

print('\n')

print(motorcycles)
motorcycles.append('honda')

print(motorcycles)

print('\n')

# Inserting elements int o a list

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')

print('\n')
# removing elements from a list

# removing an element using del keyword


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]

print(motorcycles)
print('\n')

# using pop() method

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

print(motorcycles.pop())
print(motorcycles)


print("\n")

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
print('\n')

# Popping items from any positions

# We can pop out elements from any position by inserting the index inside pop method parenthisis

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)

print("The first motorcycle I owned was a "+ first_owned.title()+ ".")
print("\n")
# Removing an element by value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

'''

The remove() method deletes only the first occurrence of the value you specify. If there’s
a possibility the value appears more than once in the list, you’ll need to use a loop to
determine if all occurrences of the value have been removed. You’ll learn how to do
this in Chapter 7

'''