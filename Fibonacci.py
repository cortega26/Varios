def Fibonacci(n):
    n1=n2=1
    if n<=2:
        nf=1
    else:
        for i in range (n-2):
            nf=n1+n2
            n1=n2
            n2=nf
    print("El número es:",nf)

n=int(input("¿Qué índice de Fibonacci busca? "))
Fibonacci(n)
