# The first thing that we are going to learn is looping through an entire list

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)


for magician in magicians:
    print(magician.title() + ", that was a great trick!")

print("\n")

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")



# anything that we do inside our for loop will be executed everytime the loop runs 

# but the important part you should take care of is indentation at everyline

# but now what will happen if we write some of the code outside the loop

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, "+ magician.title() + ".\n")

print("Thank you everyone. That was a great magic show!")


# if we forget indentation then we will recieve the error

