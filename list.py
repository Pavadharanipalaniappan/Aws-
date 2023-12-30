list=[]
n=int(input("enter the total elemnets"))
for i in range(0,n):
	a=int(input())
	list.append(a)
print(list)
list[0],list[-1]=list[-1],list[0]
print(list)
print(len(list))
if "5" in list:
  	print("true")
print("clear list:",list.clear())
