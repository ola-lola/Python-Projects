import random
import time
from termcolor import colored


print("Hello there!")
time.sleep(1)
print("If you know some cities from Europe... ")
time.sleep(1)
print(colored("Let's play HANGMAN!", "green"))
time.sleep(1)

namey = input("What's your name?: ")

time.sleep(1)
print( "Hello " + namey + "!\n")
time.sleep(1)
print("Let's start a game!")
time.sleep(1)

print(colored("Please guess a one name of capital cities in Europe!", "green"))

cities = ("TIRANE","ANDORRA" , "VIENNA", "BAKU", "MINSK", "BRUSSELS", "SARAJEVO", "SOFIA", "ZAGREB", "PRAGUE", 
"COPENHAGEN", "TALLINN", "HELSINKI", "PARIS", "TIBILISI", "BELGIA", "ATHENS", "BUDAPEST", "ROME",
"RIGA", "REYKJAVIK", "LUXEMBURG", "OSLO", "AMSTERDAM", "BELFAST", "WARSAW", "LISBON", "MOSCOW",
"EDINBURG", "BRATISLAVA", "MADRID", "STOCKHOLM", "KIEV", "LONDON", "BELGRADE")


letters_guessed_by_user = ''
attemps_left = 10
city = random.choice(cities)

print(city)

for char in city:
    print("_ ", end = '' )


has_user_won = False

while attemps_left > 0 and not has_user_won :

    print("\nPlease enter a letter or word: ")
    letter = input("").upper()    # .upper() -  print only big letters
    
    if len(letter) == 1 :
        if letter in city:
            letters_guessed_by_user += letter
            everything_is_ok = True
        
            for char in city:
        
                if char in letters_guessed_by_user:
                    print(char, end = '')
                else:
                    everything_is_ok = False
                    print("_ ", end= '')
            if everything_is_ok == False:
                has_user_won = False
            else:
                has_user_won = True

        else:  
            attemps_left -=  1
            print("Only", attemps_left , "attemps left!")
    else:
        if letter == city:
            has_user_won = True
        
        else:
            attemps_left -= 1
            print("Only", attemps_left , "attemps left!")

if has_user_won:
    print(colored( "You won!", "red"))

else:
    print(colored("You lost!", "red"))
   
