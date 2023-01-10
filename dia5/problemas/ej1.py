def devolver_distintos(int1,int2,int3):
    
    sum=int1+int2+int3
    lista = [int1,int2,int3]

    lista.sort()   

    if sum < 15:
        return lista[2]

    elif sum < 10:
        return lista[0]
    else:
        return lista[1]

