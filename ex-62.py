class ComNum:
    def __init__(self, real):
        self.real = real
    def __add__(self, other):
        real_sum = self.real +" "+ other.real
        return real_sum
str1 =input("Enter first String: ")
c1 = ComNum(str1)
str2 =input("Enter Second String: ")
c2 = ComNum(str2)
result = c1 + c2
print("Result:", result)