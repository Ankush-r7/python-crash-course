# We are going to learn about the conditional statements

# imagine you have a list of cars

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Testing for equality is case-sensitive in Python

# car == 'Audi and car == 'audi' are two different things


# Checking for inequality

requested_topping = 'mushrooms'
if requested_topping != 'anchoivies':
    print("Hold the anchovies!")

# Numerical Comparisons

# age = 18
# age == 18

# we can use <, >, <=, >= also for comparison

# Now let's come to checking multiple conditions

age_0 = 22
age_1 = 18

print(age_0>=21 and age_1>=21)


# we can also use or

print(age_0>=21 or age_1>=21)


# Checking whether a value is in the list or not

requested_toppings = ['mushrooms', 'onions', 'pineapple']

if('mushrooms' in requested_toppings):
    print("True")


# Checking whether the value is not in the list

banned_users = ['andrew', 'carolina', 'david']

user = 'marie'

if user not in banned_users:
    print(user.title()+", you can post a response if you wish.")




