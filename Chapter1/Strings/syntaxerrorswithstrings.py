# So, here we go now we will learn how should we avoid some syntax error in strings


# First, Thing is when a syntax error is occured, A syntax error is occured basically when Python doesn't recognize a section of your program as valid Python code.

# For example if you use an apostrophe within single quotes, you'll produce an error


message = "One of Python's strengths is its diverse community"

print(message)


# But if we use single quotes, Python can't identify where the string should end

# message = 'One of Python's strengths is its diverse community.'
# print(message)

# This will produce an error

# File "apostrophe.py", line 1
#  message = 'One of Python's strengths is its diverse community.'
#  ^u
# SyntaxError: invalid syntax 


