def special(s):
	for i in s:
		if not (i.isalpha() or i.isdigit() or i==' '):
			return True
	return False
s=input("enter the string:")
if special(s):
	print("the string contains special character")
else:
	print("the string not contain special character")
          