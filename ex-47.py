def val(num):
    if num<10:
        return num*3.00
    elif num < 100:
        return num*1.25
    else:
        return num*0.90

n=int(input())
print(val(n))