def Fibonacci(n):
    nf=1
    n1=n2=1
    if n==1 or n==2:
        print("El número es 1")
    else:
        for i in range (n-2):
            nf=n1+n2
            n1=n2
            n2=nf
    print(nf)

n=int(input("¿Qué índice de Fibonacci busca? "))
Fibonacci(n)
