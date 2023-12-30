def has_special_char(s):
	for c in s:
		if not (c.isalpha() or c.isdigit() or c == ' '):
			return True
	return False



s =input("enter the string:")
if has_special_char(s):
	print("The string contains special characters.")
else:
	print("The string does not contain special characters.")

