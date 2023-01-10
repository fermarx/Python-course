from os import system
from random import randint

class Persona:
    
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance) -> None:
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            print(f"{cantidad}€ were taked.")
        else:
            print("Not enough money") 

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}. Your balance is of {self.balance}€."


def menu():
    lst = ["Deposit", "Take", "Close"]
    for n in range(0, len(lst)):
        print(f"[{n+1}] -  {lst[n]}")
    
    choice = int(input("What do you want to do? "))
    if choice > len(lst) or choice < 0:
        return -1
    return choice


def crear_cliente():
    name = input("Insert your name: ")
    surname = input("Insert your surname: ")
    
    system("cls")
    return Cliente(name, surname, randint(0, 10000), 10000)


def main():

    exit = 0
    
    system("cls")
    cliente = crear_cliente()

    while exit == 0:
        choice = menu()
        system("cls")

        if choice == -1:
            print("Choose a valid option.")
            continue
        elif choice == 1:
            dep = input("How much money (€) do you want to deposit? ")
            cliente.depositar(int(dep))
            print(f"{dep}€ were deposited.")

        elif choice == 2:
            dep = input("How much money (€) do you want to take? ")
            cliente.retirar(int(dep))

        else:
            print("See you soon.")
            exit = -1
        print(cliente)

if __name__ == "__main__":
    main()