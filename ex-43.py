def primes(num):
    list1=[]
    for i in range(2, num+1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            list1.append(i)
    return list1

n=int(input("Enter the range: "))
print(primes(n))