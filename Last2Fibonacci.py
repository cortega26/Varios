# This code will give you the last 2 digits of any Fibonacci number in a fraction of a second


def Fibonacci(n):
    n1=n2=1
    if n == 0:
        return 0
    elif n <= 2:
        return 1
        #print(nf1)
    else:
        for i in range (n-2):
            nf=n1+n2
            n1=n2
            n2=nf
            #print(n2)
            #n2=str(n2)
            #for i in range(len(n2)):
            #    new =n2[:i]+n2[i+1:]
            #n2=int(n2)
    #print("El número es:",nf)
    return nf
    
def AdjustSize(n):
    n=str(n)
    #print(len(n))
    for i in range(len(n)):
        n=n[1:i]+n[i:]
        #print(n)
        if int(n) < 100:
            break
        else:
            pass
        #n=int(n)
        #len(n)=len(n)-1
        #n=str(n)
    n=int(n)
    return n
    
def newFib(n):
    n = n % 300
    #print(n)
    return AdjustSize(Fibonacci(n))

    
#T=int(input())
T=1
for i in range(T):
    #N=int(input())
    N=245896451
    print(newFib(N))
