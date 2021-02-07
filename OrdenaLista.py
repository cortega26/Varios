# This code orders a list of N (given) integer numbers without using .sort()


def OrdenaNumeros(lista):    
    lista2=[] 
    for i in range (len(lista)):
        c=0
        for i in range(len(lista)): 
            if c==0:
                c+=1 
                menor=lista[0]
            if lista[i]<menor:
                menor=lista[i]
                indice=i
        lista2.append(menor)
        lista.remove(menor)
    return lista2

def DefineList():
    lista=[]
    N=int(input("How many elements are on the list: "))
    for i in range (N):
        element=int(input(f"insert element {i+1}: "))
        lista.append(element)
    return lista

print(OrdenaNumeros(DefineList()))
