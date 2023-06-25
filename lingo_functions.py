from termcolor import colored, cprint



def minimaal_5():
    raad = input('raad het woord ')
    while len(raad) != 5:
        print(colored("minimaal 5 woorden!","red"))
        raad = input('raad het woord ')
    return raad

def letters(string,raad,teller,word):
    for element in string:
        if raad == string:
            print('dat is goed! ')
            word += colored((raad),"green")
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
    return word