s=input("enter the string:")
c=set('aeiouAEIOU')
v=0
for i in s:
	if i in c:
		v+=1
print(v)