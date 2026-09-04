# Now we will learn how can we work with a part of list

# In this we will learn about slicing 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])


# We can generate any subset of list usign slicing

print(players[1:4])

# This line will print ["martina", "michael", "florence"]


print(players[:4])


print(players[2:])


print(players[-3:])


# Looping Through a Slice

players = ['charles', 'marrtina', 'michael', 'florence', 'eli']

print("Here are the first three platers on my team: ")

for player in players[:3]:
    print(player.title())


# Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)


my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

friend_foods = my_foods # this doesn't work

