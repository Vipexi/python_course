#! /usr/bin/python3

import random

number_of_sides=int(input("How many sided dice do you want to throw?"))    
number_of_throws=int(input("How many times do you want to throw?"))
def second_dice_game(number_of_sides):
    sum = 0
    for i in range(number_of_throws):
        roller = random.randint(1, number_of_sides +1)
        print(roller)
        sum = sum + roller
    print(sum)

second_dice_game(number_of_sides)

#Tonys way



