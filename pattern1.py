for i in range(1,6):
	for j in range(1,i+1):
		print(j,end='')
	print('')
n=5
for i in range(n,0,-1):
	for j in range(n,n-i,-1):
		print(j,end='')
	print('')