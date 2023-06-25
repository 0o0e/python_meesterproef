# import colorama
# from colorama import Fore
from lingowords import words
from lingo_functions import *
import random
from termcolor import colored

opnieuw = "ja"
while opnieuw == "ja":
    string = random.choice(words)
    amount_forloop = 5
    beurten  = amount_forloop
    for i in range(amount_forloop):
        raad = minimaal_5()        
        teller = 0
        word = ""

        word =letters(string,raad,teller,word)
        print(word)
        beurten-=1
        if raad == string:
            break
        if beurten == 0 and raad != string:
            print(f"u heeft het woord niet kunnen raden. het woord was {string}")
        else:
            print(f"nog {beurten} beurten")
    opnieuw = input("wilt u opnieuw spelen? (ja/nee) ")
