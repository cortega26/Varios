# This code sorts (ascending) a list of N (given) integer numbers without using .sort()

def OrdenaNumeros(lista):    
    lista_ordenada = [] 
    for i in range (len(lista)):
        flag = True
        for j in range(len(lista)): 
            if flag: 
                menor = lista[0]
                flag = False
            if lista[j] < menor:
                menor = lista[j]
        lista_ordenada.append(menor)
        lista.remove(menor)
    return lista_ordenada


def DefineList():
    lista=[]
    N=int(input("How many elements are on the list: "))
    for i in range (N):
        element=int(input(f"insert element {i+1}: "))
        lista.append(element)
    return lista

print(OrdenaNumeros(DefineList()))
