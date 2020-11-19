#! /usr/bin/python3

# first import random module


"""roll_dice = "yes"
while roll_dice:
    if roll_dice == "yes":
        print("dice is rolling ...")
        print("value is : " ,random.randint(1 , 6))
        repeat = input("play again , yes or no")
        if repeat == "no":
            break"""

# This time we use the list Comprehension, to make a list
"""Easy
define a function that takes in a number of sides in dice as an argument
and returns a list that has all numbers of dice
Ask from the user how many sided dice he or she wants to cast
Call the function with the user given answer
roll the dice by taking random member from the list and return answer to the user using print

Normal
Same as easy plus

also ask how many rolls the user want to do,
Make as many function calls that are need, to have all the rolls.
and print separate results and also the sum of results"""



"""def dice_game():
    number_of_sides_in_dice = int(input("How many sided dice do you want to cast?"))
    dice_d6 =[i for i in range(1, number_of_sides_in_dice+1)]
    dice_cast=int(input("How many times do you want to cast?"))
    sum = 0
    for x in range(dice_cast):
        answer=random.choice(dice_d6)
        print(answer)
        sum = sum + answer
    print(sum)
dice_game()"""

"""second_dice_game(number_of_sides)
answer=input("Do you want to play again?")
    while:
        if answer =="yes":
            second_dice_game(number_of_sides)
        elif answer == "no":
            print("goodbye!")
            break"""

"""def dice_decider():
    number_of_sides = int(input("How many sided dice do you want to cast?"))
    dice_cast=int(input("How many times do you want to throw?"))
    sum = 0
        for i in range(0,number_of_dice):
        roll = random.randint(1,number_of_sides + 1)
    sum = sum + roll
    for x in range(dice_cast):
        print(random.choice(dice))
        print(sum(dice))
    
      
dice_decider()       
        
        
        

for i in range(dice_cast):
        result=random.choice(dice_d6)
        sum=0
        for i in (result):
            sum+=int(i)
            print(sum)"""
   
        
       
"""dice_game()"""


"""dice_cast=int(input("How many times do you want to cast?"))
number_of_sides_in_dice = int(input("How many sided dice do you want to cast?"))
dice_d6 =[i for i in range(1, number_of_sides_in_dice+1)]
result=[]
answer=(random.choice(dice_d6))
answer=random.choice(dice_d6)
print(answer)
result.append(answer)
print(result)
number_of_sides_in_dice=int(input("How many sided-dice do you want to cast?"))

        
Hard
Same as normal plus

after result as from user if she or he wants to roll again,
or change dice, number of rolls or both
if the user answers end, end program.

Ubuntuserver new username:
niceuser 
Tomaatti1"""
import copy

x=[1,2,3]

y=x
x[0]=69
print(x)
print(id(x))
print(id(y))

z=copy.deepcopy(x)
print(id(z))
