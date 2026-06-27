'''
1 for snake
-1 for water
0 for gun
'''

import random

random_number = random.choice([-1, 0, 1])
computer = random_number
youstr = input("enter your choice(s, w, g): ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

print(F"you choose {reverseDict[you]} and computer choose {reverseDict[computer]}")

if(computer == you): #draw
    print("its is a draw")
else:
    if(computer == -1 and you == 1): #the computer choose water and you choose snake
        print("You win!")

    elif(computer == -1 and you == 0): #the computer choose water and you choose gun
        print("You lose")

    elif(computer == 1 and you == -1): #the computer choose snake and you choose water
        print("You lose!")

    elif(computer == 1 and you == 0): #the computer choose snake and you choose gun
        print("You win!")

    elif(computer == 0 and you == -1): #the computer choose gun and you choose water
        print("You win!")

    elif(computer == 0 and you == 1): #the computer choose gun and you choose snake
        print("You lose")

    else:
        print("something went wrong") #should never happen