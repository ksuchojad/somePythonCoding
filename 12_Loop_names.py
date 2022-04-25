import random

names = []

while len(names) < 8:
    names.append( input( "Put a new name: " ) )

print("Picking a random name: ", names[random.randint(0,8)])
