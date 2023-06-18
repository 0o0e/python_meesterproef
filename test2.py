# import colorama
# from colorama import Fore
from lingowords import words
import sys, random
from termcolor import colored, cprint

string = random.choice(words)
for i in range(5):
    print(string)
    raad = input('raad het woord ')
    while len(raad) != 5:
        raad = input('raad het woord ')


    teller = 0
    word = ""
    while True:
        for element in string:
            print("teller" + raad[teller])
            print(element)
            if raad == string:
                print('goedzo')
                break

            if raad[teller] == element:
                word += colored((raad[teller]),"green")
                teller+=1
                continue
            if raad[teller] in string:

                word += colored((raad[teller]),"yellow")
                teller+=1
                continue


            if raad[teller] not in string:
                word += colored((raad[teller]),"red")
                teller+=1
                continue
            if raad == string:
                print('goedzo')
                break
            
        print(word)
        break
