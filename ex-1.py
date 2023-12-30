list=[]
n=int(input("enter the size "))
for i in range(0,n):
	a=int(input("enter the number"))
	list.append(a)
print(list)
print("swapping")
list[0],list[-1]=list[-1],list[0]
print(list)
print("length of the list:",(len(list)))
if "5" in list:
	print("the element is exist")

print("cleared list:",list.clear())

       