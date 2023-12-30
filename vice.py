list=[]
n=int(input("enter the size"))
for i in range(0,n):
	b=int(input())
	list.append(b)
list1=[]
for i in range(0,n):
	c=int(input())
	list1.append(c)
list1+=list
print(list1)