#Given an unsorted array "arr" of size "n" that contains only non-negative integers
#find a continuous sub-array which adds to a given number "s".
#If no such subarray is found, return -1.


import random
def subArraySum(arr, n, s):
    firstposition=lastposition=1  
    while True:
        acc=0
        counter=0
        for i in range(firstposition,n+1):
            acc=acc+arr[lastposition-1]
            counter+=1
            #print(acc,counter)
            if s==acc:
                print("First position is:",firstposition,"Last position is:",lastposition)
                break
            else:
                lastposition+=1
        firstposition+=1
        lastposition=firstposition
        if firstposition == s:
          print("-1")
          break
        elif s==acc:
          break
        

    #print(arr,n,s)
    
subArraySum((5,7,8,2,4,4,1,9,5,3,2,8,5,1,8,3,6,4,2,8,6,7),22,65)
