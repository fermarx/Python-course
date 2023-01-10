"""
def decorar(funcion):
    def escribir():
        print("Su turno es:")
        funcion()
        print("Aguarde y será atendido")
    return escribir

@decorar
def perfumeria_gen():
    turno = 1
    while True:
        yield f"P-{turno}"
        turno +=1


@decorar
def farmacia_gen():
    turno = 1
    while True:
        yield f"F-{turno}"
        turno +=1


@decorar
def cosmetica_gen():
    turno = 1
    while True:
        yield f"C-{turno}"
        turno +=1
"""

def perfumeria_gen():
    turno = 1
    while True:
        yield f"P-{turno}"
        turno +=1


def farmacia_gen():
    turno = 1
    while True:
        yield f"F-{turno}"
        turno +=1


def cosmetica_gen():
    turno = 1
    while True:
        yield f"C-{turno}"
        turno +=1


perf = perfumeria_gen()
farm = farmacia_gen()
cos = cosmetica_gen()
    

def decorar(option):
    print("Su turno es:")
        
    if option == 1:
        print(next(perf))

    elif option == 2:
        print(next(farm))

    elif option == 3:
        print(next(cos))

    print("Aguarde y será atendido")
