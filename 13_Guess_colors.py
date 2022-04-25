import random

answer = "yes"

colors = ["black", "yellow", "red", "white", "blue", "purple"]
guess = random.randint(0,random.randint(0,len(colors)-1)

while answer == "yes":
    print(colors)
    color = int(input( "Guess a color: 1-6 " ))
    
    if ((color-1) == guess):
        print( colors[guess])
    else:
        continue
    answer = input( "Would you like to play again?: yes/no " ).lower()

    
