# Sorts a list a list of N (given) integer numbers using .sort()

def OrdenaNumeros():
    lista=[]
    N=int(input("How many elements are on the list: "))
    for i in range (N):
        element=int(input(f"insert element {i+1}: "))
        lista.append(element)
    lista.sort()
    return lista


#LdN2=[1,8,28,297,28,-4,0,-8,1000,3,-108,-12]

#LdN2=int(input())
#print(OrdenaNumeros(LdN2))

print(OrdenaNumeros())
