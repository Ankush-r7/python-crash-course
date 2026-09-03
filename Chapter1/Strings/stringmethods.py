# Ok now we will learn about the different string methods that we use in python

# Changinf Case in a String with Methods

name = "ada lovelace"
print(name.title()) # Ada Lovelace

# method is an action that python can perform on a piece of data

# upper and lower method

print(name.upper()) # ADA LOVELACE
print(name.lower()) # ada lovelace



# Combining or Concatenating Strings

first_name = "Ankush"
last_name = "Rawat"

full_name = first_name + " " + last_name
print(full_name) # Ankush Rawat

# Python uses + symbol to combine Strings

# This method of combining String is called Concatenation

# Adding Whitespace to Strings with Tabs or Newline

# in programming whitespaces refers to any nonprinting character such as tabs, spaces, and end-of-line symbols

# Adding a tab

print("Python") # Python
print("\tPython") #     Python

# Adding a newline

print("Languages:\nPython\nC\nJavascript")


# We can also combine tabs and newlines in single string

print("Languages:\n\tPython\n\tC\n\tJavaScript")



# Stripping WhiteSpace

favorite_language = 'python '
print(favorite_language) # python<space>

print(favorite_language.rstrip()) # python

print(favorite_language) # python<space>

# the rstrip() method removes the space temporarily



