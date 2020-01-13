import math
import random

a = []

a.append(random.randint(1, 99))
guessesA = 0
g = int(input("Enter an integer from 1 to 99: "))

while ( guessesA < 10):
    for i in range(len(a)):
        if a[i] != g and g < a[i] :
            print("guess is low")  
        elif a[i] != g and g > a[i]:
            print("guess is high")
        guessesA = guessesA + 1
    g = int(input("Enter an integer from 1 to 99: "))

    if a[i] == g:
        print("you guessed it!")
        break
    elif guessesA == 10:
        print("You lost")


b = []
b.append(random.randint(1, 49))
guessesB = 0
g = int(input("Enter an integer from 1 to 49: "))

while ( guessesB < 10):
    for i in range(len(a)):
        if b[i] != g and g < b[i] :
            print("guess is low")  
        elif b[i] != g and g > b[i]:
            print("guess is high")
        guessesB = guessesB + 1
    g = int(input("Enter an integer from 1 to 49: "))

    if b[i] == g:
        print("you guessed it!")
        break
    elif guessesB == 10:
        print("You lost")



#GUESSING GAME PART 2
'''

def main(number_min, number_max):
    number_list = [random.randint(number_min, number_max) for i in range(10)]
    for i in range(len(number_list)):
        number_guess = int(input(f"Enter an integer from {number_min} to {number_max}: ")) 
        while number_list[i] != number_guess: 
            if number_guess < number_list[i]: 
                print("guess is low") 
                number_guess = int(input(f"Enter an integer from {number_min} to {number_max}: ")) 
            elif number_guess > number_list[i]: 
                print("guess is high") 
                number_guess = int(input(f"Enter an integer from {number_min} to {number_max}: ")) 
            else: 
                break
        print("you guessed it!")

main(1,99)
main(1,49)
'''