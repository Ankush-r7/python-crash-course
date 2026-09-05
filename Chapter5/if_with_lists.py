# Checking for Special Items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding" + requested_topping + ".")

print("\nFinished making your pizza!")

# But what if pizzeria runs out of green peppers

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding "+ requested_topping + ".")

print("\nFinished making your pizza!")


# Checking that the list is not empty

requested_toppings = []

if requested_toppings:
    for requested_toppinh in requested_toppings:
        print("Adding "+ requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


# using multiple lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")