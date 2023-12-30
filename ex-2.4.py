str=input("enter the string:")
stop="!"
res=""
for i in str:
	if i==stop:
		break
	res+=i
print(res)