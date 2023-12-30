def var(n):
  list1=[]
  for i in range(2,n+1):
    is_p=True
    for j in range(2,i):
       if i%j==0:
	       is_p=False
	       break
    if is_p:
	    list1.append(i)
  return list1
n=int(input())
print(var(n))