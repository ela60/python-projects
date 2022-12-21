# import random //onk gula class take
from random import randint

for x in range(1,100):
    GuessNumber = int(input("Enter your Guess-number 1 to 100 :"))
    randomNumber: int = randint(1, 100)
    if GuessNumber == randomNumber:
        print("you have won")
    else:
        print("you have lost")
        print("random number was :",randomNumber)
