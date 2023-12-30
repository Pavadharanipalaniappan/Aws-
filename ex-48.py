def val(m,n):
    a=-9.81
    c=a*m
    d=0.5*a*(m**2)
    ch=n-d
    return ch>0
    

m=int(input())
n=int(input())
print(val(m,n))