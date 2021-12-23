#!/usr/bin/python3
from random import randint

def diceRoller():
    turn = int(input("How many times you want to roll the dice: "))
    while turn>=0:
        num = randint(1,7)
        print("Dice Rolling Result: {}",str(num))
        turn -= 1


diceRoller()