from random import *
import string
from os import system

def elegir_palabra():
    """palabras = ["lugar", "mancha", "nombre", "acordarme", "mucho", "tiempo", "vivia", "hidalgo", "lanza", "astillero", "adarga", "antigua", "rocin", "flaco", "galgo", "corredor"]
    return choice(palabras)"""
    word =  input("Insert a word to guess: ")
    for l in word:
        if l not in string.ascii_lowercase:
            print("Not valid word.")
            return "", False
    system("cls")
    return word, True


def guiones(palabra):
    prt = ""
    for n in range(0,len(palabra)):
        prt += "_ "
    print (f"The word is: {prt}")
    return prt

def incorrecto(letra, list_incorrecto):
    if letra in list_incorrecto:
        print("You already tried that letter!.")
        print(list_incorrecto)
        return False
    print("Sorry! this letter is not in the secret word.")
    list_incorrecto.append(letra)
    print(list_incorrecto)
    return False

def pedir_letra(palabra):
    letra = input("Try a letter: ").lower()
    if letra not in string.ascii_lowercase:
        print("Not valid symbol.")
        return "_ "
    elif letra not in palabra:
        return letra, "mal"
    else:
        return letra, "correcto"

def imprimir_letra(letra, palabra, list_correcto):
    ret_palabra = ""
    for n in range(0,len(palabra)):
        if palabra[n] in list_correcto:
            ret_palabra +=  palabra[n] 
        else:
            ret_palabra += "_ "
    print(ret_palabra)
    return ret_palabra

def main():

    list_incorrecto = []
    list_correcto = []
    caso = False
    vidas = 10
    
    while caso != True:
        palabra, caso = elegir_palabra()

    correcto = guiones(palabra)

    while "_ " in correcto:

        letra, estado = pedir_letra(palabra)
        if letra == "_ ":
            continue 
        
        elif estado != "correcto":
            if letra not in list_incorrecto:
                vidas -= 1
                print(f"You have {vidas} lives left.")
            incorrecto(letra, list_incorrecto)
            if vidas == 0:
                print(f"You ran out of lives! :( The word was {palabra.upper()}")
                return
        
        if letra in palabra:
            list_correcto.append(letra)
        
        correcto = imprimir_letra(letra, palabra, list_correcto)
        

        print("\n")
    
    print(f"You guessed that the word was {palabra.upper()}!!! With {vidas} lives left!")

if __name__ == "__main__":
    main()