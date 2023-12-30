my=[1,2,3,4,5]
try:
 i=int(input("enter an integer:"))
 print("value at index",i,"is",my[i])
except IndexError:
	print("error:Index is out of range.")
