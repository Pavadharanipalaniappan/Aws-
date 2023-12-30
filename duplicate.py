x=input("enter the string")
l=''
for i in x:
	if i not in l:
		l=l+i
print(l)