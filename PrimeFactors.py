#Prime factors of a list of numbers

def primeFactors(array):

    import math
    prime_factors=[]
    for j in array:
      
      while j % 2 == 0: 
          prime_factors.append(2) 
          j = j / 2
           
    
      for i in range(3,int(math.sqrt(j))+1,2):
        while j % i== 0:
          prime_factors.append(i)
          j = j / i 
                
      prime_factors.append(j)
      

    res = [] 
    [res.append(int(x)) for x in prime_factors if x not in res]
    print(res)

array=[1,2,3,4,5,6,7,8]
primeFactors(array)
