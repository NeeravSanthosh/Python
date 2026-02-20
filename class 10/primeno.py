#print prime numbers
L = int(input("enter the lower limit :"))
U = int(input("enter the upper limit :"))
print(f"the prime number form {L} to {U}")
for n in range(L,U+1):
    if n >1:
        for j in range(2,n):
            if n%j == 0:
                break
        else:
            print(n)