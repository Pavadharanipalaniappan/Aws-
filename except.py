numerator=int(input("enter the numerator:"))
denominator =int(input("enter the denominator:"))
try:
    
    result = numerator/denominator

    print('%.2f' %result)
except:
    print("Error: Denominator cannot be 0.")
