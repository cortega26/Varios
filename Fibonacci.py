def fibonacci(n):
    a, b = 1, 1
    if n <= 2:
        return 1
    for i in range (n-2):
        nf = a + b
        a = b
        b = nf
    return nf

if __name__ == "__main__":
    fibonacci(50)
