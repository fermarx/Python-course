from numeros import decorar
from os import system

def menu():
    ret = "Coger ticket para:\n"

    lista = ["Perfumeria", "Farmacia", "Cosmetica"]

    for n in range(0, len(lista)):
        ret += f"[{n+1}] -  {lista[n]}\n"
    ret += ">>> "
    
    option = ""
    while option.isnumeric() == False:
        try:
            option = input(ret)
        except:
            print("Enter a number")
    
    option = int(option)
    if option > len(lista) or option < 1:
        return -1

    return option
    

def main():

    option = -1
    while True:
        while option == -1:
            option = menu()
            system("cls")
            if option == -1:
                print("Enter a valid option")
        decorar(option)
    

if __name__ == "__main__":
    main()