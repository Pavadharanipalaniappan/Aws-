s={'ACDEFGH'}
s1={'IJKLMNOP'}
concat_str=0
for i in s:
	for j in s1:
		concat_str=i+j
		if len(set(concat_str))==26:
			print("complte pair")
		else:
			print("not a complete pair")