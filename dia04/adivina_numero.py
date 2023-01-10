from random import *

Fail = True

name = input("Introduzca su nombre: ")

print("Guess the number I'm thinking, between 1 and 100.\nYou have 8 tries.\n")

n_guess = randint(0,100)

guess = int(input("Tell me a number: "))

for tries in range(0,8):

    if guess > 100 or guess < 0:
        print("The number shoud be between 0 and 100.")

    elif guess == n_guess:
        print(f"Congrats! You guessed that the number was {n_guess} in {tries+1} tries.")
        Fail = False
        break

    elif guess > n_guess:
        print("The number I thought is lesser.")

    elif guess < n_guess:
        print("The number I thought is bigger.")
    
    guess = int(input("Tell me another number: "))

if Fail == True:
    print(f"Sorry! The number I thought was {n_guess}")