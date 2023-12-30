def has_any_special(s):
	for c in s:
		if not(c.isalpha() or c.digit or c==' '):
			return True
	return False
    
   
s=input("enter the string:")
if has_any_special(s):
	print("special charcter contains")
else:
	print("not contain")     