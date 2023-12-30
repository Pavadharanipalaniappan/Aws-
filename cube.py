n=int(input("enter the size:"))
list=[]
list1=[]
for i in range(0,n):
	x=int(input())
	list.append(x)
for i in list:
	list2=(i,(i**3))
	list1.append(list2)
print(list1)