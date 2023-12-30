n=int(input("enter the size:"))
c=0
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end='')
	print('')
for i in range(1,n+1):
	for j in range(1,n+1):
        n-=1
		print(j,end='')
	print('')
    