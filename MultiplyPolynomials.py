#Given two polynomials represented by two arrays that contains the coefficients of poynomials
#returns the polynomial in form of array formed after multiplication of given polynomials.


def polyMultiply(Arr1,Arr2,M,N):
    res=[0]*(M+N-1)
    count1=0
    for i in range(M):
        count2=0
        for j in range(N):
            countf=count1+count2
            res[countf]+=Arr1[i]*Arr2[j]
            count2+=1
        count1+=1
    return res
    
Arr1=(1,3,7,4,2)
Arr2=(4,2,4,7,0,1,6)
M=5
N=7
polyMultiply(Arr1,Arr2,M,N)
