#Geek created a random series and given a name geek-onacci series.
#Given four integers A, B, C, N. A, B, C represents the first three numbers of geek-onacci series.
#Find the Nth number of the series.
#The nth number of geek-onacci series is a sum of the last three numbers (summation of N-1th, N-2th, and N-3th geek-onacci numbers)
#
#Input:
#1. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
#2. The first line of each test case contains four space-separated integers A, B, C, and N.
#
#Output: For each test case, print Nth geek-onacci number


def Geekonacci():
    T=int(input())
    for i in range(T):
        A,B,C,N=input().split()
        A,B,C,N=[int(A),int(B),int(C),int(N)]
        for j in range(N-3):
            Geek=A+B+C
            A=B
            B=C
            C=Geek
        print(Geek)
        #print(a)
    

Geekonacci()
