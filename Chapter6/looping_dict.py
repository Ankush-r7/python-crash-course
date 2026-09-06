# So, now we are going to learn about looping in dictionary


user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi'
}

for key, value in user_0.items():
    print("\nKey:"+key)
    print("Value: "+value)

# Note : the output will not be in the same order as it is stored inside the dictionary

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is "+language.title()+".")


# Looping through all the keys

for name in favorite_languages.keys():
    print(name.title())


friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi "+name.title()+", I see your favorite language is "+favorite_languages[name].title()+"!")


# Looping Through a Dictionary's Keys in Order

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping Through all values in a Dictionary


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

    