def ordenar(str):
    
    lst = []

    for l in str:
        lst.append(l)
        
    lst = list(set(lst))
    lst.sort()
    return lst

ordenar("entretenido")