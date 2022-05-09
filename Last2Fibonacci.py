# This code will give you the last 2 digits of any Fibonacci index

def Fibonacci(n):
    n1 = n2 = 1
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        for i in range (n-2):
            nf = n1 + n2
            n1 = n2
            n2 = nf
    return nf
    
def AdjustSize(n):
    n = str(n)
    for i in range(len(n)):
        n = n[1:i] + n[i:]
        if int(n) < 100:
            break
        else:
            pass
    n = int(n)
    return n
    
def newFib(n):
    n = n % 300
    return AdjustSize(Fibonacci(n))

    
#T=int(input())
T=1
for i in range(T):
    #N=int(input())
    N=245896451
    print(newFib(N))
