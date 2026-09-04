# now we will be learning about numerical lists

# Use of range() function

for value in range(1,5):
    print(value)

# using range to make a list of numbers 

numbers = list(range(1,6))

print(numbers)


# we can also skip some numbers while counting

even_nums = list(range(2,11,2))
print("Even numbers from 1 to 10 are :",even_nums)


# You can create almost every set of numbers using range function

squares = []

for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# Simple Statistics with list of numbers

digits = list(range(0,11))

print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehensions

# Earlier we made a list of squares using 3 4 lines of code now we will be creating the same list using single line of code
squares = [value**2 for value in range(1,11)]
print(squares)
