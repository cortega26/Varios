#Geek's Paint Shop is one of the famous shop in Geekland, but 2014 Earthquake caused disarrangement of the items in his shop.
#Each item in his shop is a 40-digit alpha numeric code.
#Now Chunky wants to retain the reputation of his shop, for that he has to arrange all the distinct items in lexicographical order.
#Your task is to arrange the all the distinct items in lexicographical ascending order and print them along with their count.


def sortedStrings(N,A):
  A.sort()
  result=[]
  for i in range(N):
    partial=(A[i],A.count(A[i]))
    result.append(partial)
  res = [] 
  [res.append(x) for x in result if x not in res]
  return res

N = 5
A = ["2234597891 zmxvvxbcij 8800654113 jihgfedcba","1234567891 zxyabcvapo 0123434908 padmadngaa","1234567891 abcdefghij 9876543219 jihgfedcba","2234597891 zmxvvxbcij 8800654113 jihgfedcba","9120121291 zmxvvxbcij 0912114113 mnvxbedcba"]
 
print(sortedStrings(N,A))
