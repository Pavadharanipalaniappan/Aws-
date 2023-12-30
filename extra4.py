def date(dd,mm,yyyy):
 thirtyone=[1,3,5,7,8,10,12]
 thirty=[4,6,11,9]
 if yyyy%4==0 and mm==2 and dd<=29:
     print("valid") 
 elif mm in thirtyone and dd<=31:
     print("valid")
 elif mm in thirty and dd<=30:
     print("valid")
 elif mm==2 and dd<=28:
     print("valid")
 else:
     print("invalid")  
           
dd=int(input("enter the date:"))
mm=int(input("enter the month:"))
yyyy=int(input("enter the year:"))
date(dd,mm,yyyy)
