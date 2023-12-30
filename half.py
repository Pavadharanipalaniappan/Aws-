def half(s):
	l=len(s)
	a=l//2
	b=s[:a].upper()
	r=b+s[a:]
	return r
s=input("enter the string:")
m=half(s)
print(m)