def commas(s):
        r=''
        for i in s:
            if i==",":
                r+='.'
            elif i==".":
                r+=','
            else:
                r+=i
        return r
s=input("enter the string:")
m=commas(s)
print(m)
			
                	     