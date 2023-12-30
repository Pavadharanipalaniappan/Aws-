n=[(5,6),(5,7),(5,8),(6,10),(7,12)]
a=[]
s=[]
for i in n:
	if i[0] not in s:
		s.append(i[0])
for i in s:
	p=[]
	p.append(i)
	for j in n:
		if i==j[0]:
			p.append(j[1])
	a.append(p)
print(str(a))