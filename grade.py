x=int(input("enter the UNIT:"))
if x<100:
	print("no amount")
elif(x>=100 and x<200):
    print((x-100)*5)
elif(x>=200 and x<300):
    print((x-100)*10)
else:
    print((x-100)*15)