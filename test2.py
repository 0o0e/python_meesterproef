# import colorama
# from colorama import Fore
from lingowords import words
import sys, random
from termcolor import colored, cprint

string = random.choice(words)
for i in range(5):
    print(string)
    teller = 0

    word = ""
    raad = input('raad het woord ')

    for element in string:
        print(element)
        if raad[teller] == element:
            word += colored((raad[teller]),"green")
            print(word)
            
            teller+=1
            continue
        if raad[teller] in string:

            word += colored((raad[teller]),"yellow")
            print(word)
            teller+=1
            continue


        if raad[teller] not in string:
            word += colored((raad[teller]),"red")
            print('vvv')
            teller+=1
            continue
        
    print(word)
