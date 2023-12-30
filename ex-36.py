class customException(Exception):
	pass
vote=18
try:
 age=int(input())
 if age>vote:
    raise customException("eligible")
 else:
    print(" not eligible")
except customException as e:
   print(e)