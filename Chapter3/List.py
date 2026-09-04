# The first question here is what is the list

'''
A list is a collection of items in a particular order.
You can make a list that includes the letters of the alphabet, the digits from 0-9, or the names of 
all the people in you family. You can put anything you want into a list, and the items in you list don't have to be related in any particular way.
Because a list usually contains more than one element, it's a good idea to make the name of you list plural, such as letters, digits, or names.
'''

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Now let's learn how to access individual elements inside the list

print("\nThe first element of the list is ",end="")
print(bicycles[0])

print("\nThe first element of the list is ",end="")
print(bicycles[0].title())


print(bicycles[1])
print(bicycles[3])


print(bicycles[-1])



# Using Individual Values from a List

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)