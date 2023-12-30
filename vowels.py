def vowels(s):
	for i in s:
        	if i in 'a e i o u A E I O U ':
           		return True
	return False
s=input("enter the string:")
if vowels(s):
	print("vowels are present")
else:
	print("vowels are not present")