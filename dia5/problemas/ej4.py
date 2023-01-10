def es_primo(num):
    for n in range(2, num):
        if num%n==0:
            return False
    return True
            

def contar_primos(int):
    
    n_primos = 0
    for n in range(2,int):
        if es_primo(n) == True:
            n_primos += 1
            print(n)

    return n_primos

print(contar_primos(50))